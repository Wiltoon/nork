from src.utils.services import CustomerService
from src.database.exceptions.exception import VehicleLimit, CustomerNotFound
from tests.src.tasks import (
    customer_payload_validated,
    vehicle_payload_validated,
    customer_orm_model,
    vehicle_orm_model,
)

# Standards
from unittest.mock import patch

# Third party
import pytest




@pytest.mark.asyncio
@patch("src.utils.services.ClientService.repository")
@patch.object(CustomerService, "check_if_customer_can_have_more_vehicles")
@patch.object(CustomerService, "check_if_customer_exists")
async def test_when_new_linking_car_with_successfully_then_return_true(
    mock_check_customer, mock_validate_vehicles, mock_repository
):
    result = await CustomerService.linking_vehicle_to_owner(
        payload_validated=vehicle_payload_validated, customer_id=5
    )

    mock_check_customer.assert_called_once_with(customer_id=5)
    mock_validate_vehicles.assert_called_once_with(customer_id=5)
    mock_repository.insert_vehicle.assert_called_once()
    mock_repository.update_sale_opportunity_status.assert_called_once_with(customer_id=5)
    assert result is True


@pytest.mark.asyncio
@patch("src.utils.services.config", return_value=2)
@patch("src.utils.services.CustomerService.repository")
async def test_when_customer_can_have_more_vehicles_then_proceed(
    mock_repository, mock_decouple
):
    result = await CustomerService.check_if_customer_can_have_more_vehicles(customer_id=8)

    assert result is None



@pytest.mark.asyncio
@patch("src.utils.services.ClientService.repository")
async def test_when_customer_exists_then_proceed(mock_repository):
    result = await CustomerService.check_if_customer_exists(customer_id=7)

    mock_repository.get_customer_by_id.assert_called_once_with(customer_id=7)
    assert result is None



@pytest.mark.asyncio
@patch("src.utils.services.ClientService.repository")
async def test_when_new_customer_register_with_success(
    mock_repository,
):
    result = await CustomerService.register_new_customer(
        payload_validated=customer_payload_validated
    )

    mock_repository.insert_customer.assert_called_once()
    assert result is True


@pytest.mark.asyncio
@patch("src.utils.services.config", return_value=2)
@patch(
    "src.utils.services.ClientService.repository.get_all_vehicles_by_id",
    return_value=[1, 1, 1],
)
async def test_when_customer_exceeded_limit_vehicles(
    mock_repository, mock_decouple
):
    with pytest.raises(VehicleLimit):
        await CustomerService.check_if_customer_can_have_more_vehicles(customer_id=8)



@pytest.mark.asyncio
@patch(
    "src.utils.services",
    return_value=vehicle_orm_model,
)
async def test_when_get_all_vehicles_with_success(
    mock_repository,
):
    result = await CustomerService.get_all_vehicles()

    mock_repository.assert_called_once_with()
    assert isinstance(result, dict)

@pytest.mark.asyncio
@patch(
    "src.utils.services.ClientService.repository.get_customer_by_id",
    return_value=None,
)
async def test_when_customer_exists_then_proceed(mock_repository):
    with pytest.raises(CustomerNotFound):
        await CustomerService.check_if_customer_exists(customer_id=7)


@pytest.mark.asyncio
@patch(
    "src.utils.services.ClientService.repository.get_all_customers",
    return_value=customer_orm_model,
)
async def test_when_get_all_customers_with_success(
    mock_repository,
):
    result = await CustomerService.get_all_customers()

    mock_repository.assert_called_once_with()
    assert isinstance(result, dict)

