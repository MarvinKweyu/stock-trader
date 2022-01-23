import json

# import factory
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from localstore.models import Product, Reorder
from localstore.serializers import ProductSerializer, ReorderSerializer
from localstore.views import ProductViewSet, ReorderViewset

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()


class ProductTestcase(APITestCase):
    def test_product_list(self):
        url = reverse("products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        product = Product.objects.create(
            name="Test Product", price=100, inventory=10, re_order_level=5
        )
        url = reverse("products-detail", args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_create(self):
        # url = reverse('products-create')
        data = {
            "name": "Test Product",
            "price": 100,
            "inventory": 10,
            "re_order_level": 5,
        }
        response = self.client.post("/api/v1/store/products/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_update(self):
        product = Product.objects.create(
            name="Test Product", price=100, inventory=10, re_order_level=5
        )
        url = reverse("products-detail", args=[product.id])
        data = {
            "name": "Test Product",
            "price": 100,
            "inventory": 3,
            "re_order_level": 5,
        }

        # using viewset

        # view = ProductViewSet.as_view(
        #     {'patch': 'partial_update'})

        # request = self.client.patch(url, data)

        # response = view(request, pk=product.id).render()

        # using viewset
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print("Database reorders", Reorder.objects.all())

        reorder_url = reverse("reorders-list")
        reorder_response = self.client.get(reorder_url)
        print(json.loads(reorder_response.content))
        # self.assertEqual(json.loads(reorder_response.content), second)


# @pytest.mark.django_db
# def test_product_quantity_is_updated_when_reorder_is_processed(reorder_factory):

#     product = Reorder.objects.get(pk=1)
#     print(product.inventory)


@pytest.mark.django_db
def test_products_are_created(multiple_new_products):
    """
    Test that 10 new products are created
    """
    assert Product.objects.count() == 10


@pytest.mark.django_db
def test_reorder_is_created_when_inventory_is_low(new_product):

    product = Product.objects.get(pk=1)
    print(product.inventory)


#     aoo = User.objects.get(username='aoo')
#     client = APIClient()
#     client.force_authenticate(user=aoo)
#     url = reverse('api:role-list')

#     old_currency = CurrencyFactory.build()
#     new_currency = CurrencyFactory.build()
#     currency_dict = {
#         'code': new_currency.code,
#         'name': new_currency.name,
#         'symbol': new_currency.symbol
#     }
#     url = reverse('currency-detail', kwargs={'pk': old_currency.id})
#     request = rf.put(
#         url,
#         content_type='application/json',
#         data=json.dumps(currency_dict)
#     )
#     mocker.patch.object(
#         CurrencyViewSet, 'get_object', return_value=old_currency
#     )
#     mocker.patch.object(
#         Currency, 'save'
#     )
#     view = CurrencyViewSet.as_view(
#         {'put': 'update'}
#     )

#     response = view(request, pk=old_currency.id).render()

#     assert response.status_code == 200
#     assert json.loads(response.content) == currency_dict

#     singh = Company.objects.get(name='Singh')
#     data = {
#         'name': 'HairCut',
#         'type': Role.RoleType.admin,
#         'company': singh.id,  # Must be his companyid. Reason is in the RoleSerializer docstring
#     }
#     response = client.post(url, data, format='json')

#     assert 201 == response.status_code


# def test_admin_can_create_role(userprofiles, aoo_admin, bug_manager, note_admin):
#     aoo = User.objects.get(username='aoo')
#     client = APIClient()
#     client.force_authenticate(user=aoo)
#     url = reverse('api:role-list')
#     singh = Company.objects.get(name='Singh')
#     data = {
#         'name': 'HairCut',
#         'type': Role.RoleType.admin,
#         'company': singh.id,  # Must be his companyid. Reason is in the RoleSerializer docstring
#     }
#     response = client.post(url, data, format='json')

#     assert 201 == response.status_code

# class TestProductViewset():

#     def test_update(self, mocker, rf):
#         old_currency = CurrencyFactory.build()
#         new_currency = CurrencyFactory.build()
#         currency_dict = {
#             'code': new_currency.code,
#             'name': new_currency.name,
#             'symbol': new_currency.symbol
#         }
#         url = reverse('currency-detail', kwargs={'pk': old_currency.id})
#         request = rf.put(
#             url,
#             content_type='application/json',
#             data=json.dumps(currency_dict)
#         )
#         mocker.patch.object(
#             CurrencyViewSet, 'get_object', return_value=old_currency
#         )
#         mocker.patch.object(
#             Currency, 'save'
#         )
#         view = CurrencyViewSet.as_view(
#             {'put': 'update'}
#         )

#         response = view(request, pk=old_currency.id).render()

#         assert response.status_code == 200
#         assert json.loads(response.content) == currency_dict

#     @pytest.mark.parametrize('field', [
#         ('code'),
#         ('name'),
#         ('symbol'),
#     ])
#     def test_partial_update(self, mocker, rf, field):
#         currency = CurrencyFactory.build()
#         currency_dict = {
#             'code': currency.code,
#             'name': currency.name,
#             'symbol': currency.symbol
#         }
#         valid_field = currency_dict[field]
#         url = reverse('currency-detail', kwargs={'pk': currency.id})
#         request = rf.patch(
#             url,
#             content_type='application/json',
#             data=json.dumps({field: valid_field})
#         )
#         mocker.patch.object(
#             CurrencyViewSet, 'get_object', return_value=currency
#         )
#         mocker.patch.object(
#             Currency, 'save'
#         )
#         view = CurrencyViewSet.as_view(
#             {'patch': 'partial_update'}
#         )

#         response = view(request).render()

#         assert response.status_code == 200
#         assert json.loads(response.content)[field] == valid_field
