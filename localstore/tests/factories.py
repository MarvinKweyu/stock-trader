import factory
from faker import Faker
from model_bakery import baker

from localstore.models import Product, Reorder

fake = Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = fake.name()
    price = fake.random_number(digits=2)
    # inventory = fake.random_number(digits=2)
    # re_order_level = fake.random_number(digits=2)

    inventory = 10
    re_order_level = 5


class ReorderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reorder

    # ProductFactory is a sub-factory. It will create a product and assign it to the reorder.
    product = factory.SubFactory(ProductFactory)
    quantity = fake.random_number(digits=2)
    status = "Pend"
    # status = fake.random_element(('Proc', 'Pend'))
    re_order_level = fake.date()
