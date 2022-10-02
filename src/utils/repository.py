from src.database.customer.model import CustomerModel
from src.database.vehicle.model import VehicleModel
from src.utils.infra import SqliteInfrastructure


class SqliteRepository:

    infra = SqliteInfrastructure

    @classmethod
    def insert_customer(cls, customer: CustomerModel):
        session = cls.infra.get_session()
        session.add(customer)
        session.commit()
        session.close()

    @classmethod
    def insert_vehicle(cls, vehicle: VehicleModel):
        session = cls.infra.get_session()
        session.add(vehicle)
        session.commit()
        session.close()

    @classmethod
    def update_sale_opportunity_status(cls, customer_id: int):
        session = cls.infra.get_session()
        client = session.query(CustomerModel).get(customer_id)
        client.sale_opportunity = False
        session.commit()
        session.close()

    @classmethod
    def get_all_vehicles_by_id(cls, customer_id: int):
        session = cls.infra.get_session()
        vehicles = session.query(VehicleModel).filter(VehicleModel.customer_id == customer_id)
        return vehicles

    @classmethod
    def get_customer_by_id(cls, customer_id: int):
        session = cls.infra.get_session()
        client = session.query(CustomerModel).get(customer_id)
        return client

    @classmethod
    def get_all_customers(cls):
        session = cls.infra.get_session()
        customers = session.query(CustomerModel).all()
        return customers

    @classmethod
    def get_all_vehicles(cls):
        session = cls.infra.get_session()
        customers = session.query(VehicleModel).all()
        return customers