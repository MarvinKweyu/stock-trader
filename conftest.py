# test configuration file.
# include fixtures here

# pytest will look for this file before running tests

import pytest
from pytest_factoryboy import register

from localstore.tests.factories import ProductFactory, ReorderFactory


register(factory_class=ProductFactory)
register(factory_class=ReorderFactory)


@pytest.fixture
def multiple_new_products(db, product_factory):
    """Create multiple new products for testing."""
    return product_factory.create_batch(10)


@pytest.fixture
def new_product(db, product_factory):
    """Create a new product for testing."""
    return product_factory.create()


@pytest.fixture
def new_reorder(db, reorder_factory):
    """Create a new reorder for testing."""
    return reorder_factory.create()


@pytest.fixture
def new_reorder(db, reorder_factory):
    """Create a new reorder for testing."""
    return reorder_factory.create()
