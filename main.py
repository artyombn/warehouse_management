from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.models import Product
from domain.services import WarehouseService
from infrastructure.orm import Base, ProductORM, OrderORM
from infrastructure.repositories import SqlAlchemyProductRepository, SqlAlchemyOrderRepository
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.database import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def main():
    session = SessionFactory()
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    uow = SqlAlchemyUnitOfWork(session)

    warehouse_service = WarehouseService(product_repo, order_repo)
    with uow:
        new_product1 = warehouse_service.create_product(name="test1", quantity=1, price=100)
        new_product2 = warehouse_service.create_product(name="test2", quantity=1, price=300)
        new_product3 = warehouse_service.create_product(name="test3", quantity=1, price=500)
        uow.commit()
        print(f"--- Products created: {[new_product1, new_product2, new_product3]}")
        new_order = warehouse_service.create_order([new_product1, new_product2, new_product3])
        uow.commit()
        print(f"--- Order created: {new_order}")

        get_product1 = warehouse_service.get_product(1)
        get_product2 = warehouse_service.get_product(2)
        get_product3 = warehouse_service.get_product(3)
        print(f"--- Got product with id=1: {get_product1}")
        print(f"--- Got product with id=2: {get_product2}")
        print(f"--- Got product with id=3: {get_product3}")
        get_products_list = warehouse_service.get_product_list()
        print(f"--- Got product list: {get_products_list}")
        update_product = warehouse_service.update_product(1, "new_name", 10, 150)
        print(f"--- Product updated: {update_product}")
        delete_product = warehouse_service.delete_product(2)
        print(f"--- Deleted product: {get_product2}")
        print(f"--- Current products list: {warehouse_service.get_product_list()}")

        get_order = warehouse_service.get_order(1)
        print(f"--- Got order with id=1: {get_order}")
        new_order2 = warehouse_service.create_order([get_product3])
        get_order_list = warehouse_service.get_order_list()
        print(f"--- Got order list: {get_order_list}")
        update_order = warehouse_service.update_order(1, [get_product1])
        print(f"--- Order updated: {update_order}")
        print(f"--- Current order list: {warehouse_service.get_order_list()}")


        get_order2 = warehouse_service.get_order(2)
        delete_order = warehouse_service.delete_order(2)
        print(f"--- Deleted order: {get_order2}")
        print(f"--- Current order list: {warehouse_service.get_order_list()}")



if __name__ == "__main__":
    main()


