from accounts.models import CustomUser
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.response import Response

from localstore.models import Product, Reorder
from localstore.permissions import IsWarehouseAttendeeOrReadOnly
from localstore.serializers import ProductSerializer, ReorderSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product viewset details
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]

    def update(self, request, *args, **kwargs):
        """
        Simulate sale. When an item is sold beyond the threshold, a reorder item for this product is created
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # print("user data", request.user,
        #       CustomUser.objects.filter(role='R'))

        #   check if inventory is lower tnan re_order_level then create reorder

        if(instance.inventory < instance.re_order_level):
            print("Creating reorder")
            # reorder = Reorder.objects.create(product=instance)
            reorder = Reorder(product=instance,
                              quantity=instance.re_order_level - instance.inventory)
            reorder.save()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ReorderViewset(viewsets.ModelViewSet):
    """
    Reorder viewset details
    """
    queryset = Reorder.objects.all()
    serializer_class = ReorderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'status']
    # permission_classes = (permissions.IsAuthenticated,
    #                       )

    def update(self, request, *args, **kwargs):
        """
        Dispatch a reorder to the store, modifying the product inventory in the process
        This happens when the status is changed to processed
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        product_status = None

        try:
            product_status = request.data.get('status')
        except:
            pass

        product_id = instance.product.id

        if product_status == 'Proc':
            product = Product.objects.get(id=product_id)
            #  update product quantity by threshold plus current quantity
            product.inventory += product.re_order_level
            product.save()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
