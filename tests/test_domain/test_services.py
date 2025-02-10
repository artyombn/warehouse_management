from service_mock import service_mock, product_repo_mock, order_repo_mock
from domain.models import Product, Order

def test_create_product():
    service = service_mock()
    product = service.create_product(name="product_name", quantity=1, price=100.0)
    assert isinstance(product, Product)
    assert isinstance(product.name, str) and product.name == "product_name"
    assert isinstance(product.quantity, int) and product.quantity == 1
    assert isinstance(product.price, float) and product.price == 100.0

def test_get_product():
    fake_product = Product(id=1, name="fake_product", quantity=1, price=50)
    product_repo_mock.get.return_value = fake_product
    service = service_mock()
    product = service.get_product(1)
    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name == "fake_product"
    assert product.quantity == 1
    assert product.price == 50

def test_get_product_list():
    fake_product_list = [
        Product(id=1, name="fake_product_1", quantity=10, price=100),
        Product(id=2, name="fake_product_2", quantity=5, price=50),
        Product(id=3, name="fake_product_3", quantity=20, price=200),
    ]

    product_repo_mock.list.return_value = fake_product_list
    service = service_mock()
    product_list = service.get_product_list()
    assert isinstance(product_list, list)
    assert all(isinstance(product, Product) for product in product_list)
    assert len(fake_product_list) == len(product_list)

def test_update_product():
    fake_product = Product(id=1, name="fake_product", quantity=1, price=50)
    updated_product = Product(1, "new_fake_name", quantity=2, price=100)

    product_repo_mock.get.return_value = updated_product
    service = service_mock()
    product = service.update_product(1, "new_fake_name", quantity=2, price=100)
    assert isinstance(product, Product)
    assert product.name == "new_fake_name"
    assert product.quantity == 2
    assert product.price == 100

def test_delete_product():
    fake_product_list = [
        Product(id=1, name="fake_product_1", quantity=10, price=100),
        Product(id=2, name="fake_product_2", quantity=5, price=50),
        Product(id=3, name="fake_product_3", quantity=20, price=200),
    ]

    product_repo_mock.delete.return_value = fake_product_list[:2]
    service = service_mock()
    result = service.delete_product(3)
    assert isinstance(result, list)
    assert len(result) == len(fake_product_list) - 1
    assert result[0] == fake_product_list[0] and result[1] == fake_product_list[1]




