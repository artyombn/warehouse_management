from unittest.mock import Mock
from domain.services import WarehouseService

product_repo_mock = Mock()
order_repo_mock = Mock()

def service_mock():
    return WarehouseService(product_repo_mock, order_repo_mock)