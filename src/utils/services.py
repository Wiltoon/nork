from decouple import config

from src.database.validator.CustomerValidator import CustomerValidator
from src.database.validator.VehicleValidator import VehicleValidator
from src.database.customer.model import CustomerModel
from src.database.vehicle.model import VehicleModel
from src.database.exceptions.exception import VehicleLimit, CustomerNotFound
from src.utils.repository import SqliteRepository


class CustomerService:

    repository = SqliteRepository

    @classmethod
    async def register_new_customer(cls, payload_validated: CustomerValidator):
        new_customer = CustomerModel(
            name=payload_validated.name,
            id_city=payload_validated.id_city,
            sale_opportunity=payload_validated.sale_opportunity,
            phone=payload_validated.phone,
        )
        cls.repository.insert_customer(customer=new_customer)
        return True

    @classmethod
    async def linking_vehicle_to_owner(
        cls, payload_validated: VehicleValidator, customer_id: int
    ) -> bool:
        await cls.check_if_customer_exists(customer_id=customer_id)
        await cls.check_if_customer_can_have_more_vehicles(customer_id=customer_id)
        color = payload_validated.color.value
        model = payload_validated.model.value
        new_vehicle_linking = VehicleModel(color=color, model=model, client_id=customer_id)
        cls.repository.insert_vehicle(vehicle=new_vehicle_linking)
        cls.repository.update_sale_opportunity_status(customer_id=customer_id)
        return True

    @classmethod
    async def check_if_customer_can_have_more_vehicles(cls, customer_id: int):
        vehicles = cls.repository.get_all_vehicles_by_id(customer_id=customer_id)
        result = [vehicle for vehicle in vehicles]
        if len(result) >= int(config("VEHICLE_LIMIT")):
            raise VehicleLimit

    @classmethod
    async def check_if_customer_exists(cls, customer_id: int):
        customer = cls.repository.get_customer_by_id(customer_id=customer_id)
        if not customer:
            raise CustomerNotFound

    @classmethod
    async def get_all_customers(cls):
        customers = cls.repository.get_all_customers()
        result = {"customers": [customer.as_dict() for customer in customers]}
        return result

    @classmethod
    async def get_all_vehicles(cls):
        vehicles = cls.repository.get_all_vehicles()
        result = {"vehicles": [vehicle.as_dict() for vehicle in vehicles]}
        return result