from session_fixture import db_session

from infrastructure.orm import OrderORM, ProductORM


def test_create_product(db_session):
    product = ProductORM(name="product1", quantity=1, price=100)
    db_session.add(product)
    db_session.commit()

    is_product = db_session.query(ProductORM).filter_by(name="product1").one()
    assert is_product is not None
    assert product == is_product


def test_create_order(db_session):
    products = [
        ProductORM(name="product1", quantity=1, price=100),
        ProductORM(name="product2", quantity=1, price=50),
        ProductORM(name="product3", quantity=1, price=200),
    ]
    db_session.add_all(products)
    db_session.commit()

    order = OrderORM(products=products)
    db_session.add(order)
    db_session.commit()

    is_order = db_session.query(OrderORM).filter_by(id=1).one()
    assert is_order is not None
    assert is_order == order
    assert is_order.products == products
