from src.database.enums.enums import Colors, VehicleModelTypes
from src.database.validator.VehicleValidator import VehicleValidator
from src.database.validator.CustomerValidator import CustomerValidator
from src.database.customer.model import CustomerModel
from src.database.vehicle.model import VehicleModel


customer_payload = {
    "name": "Gustavo",
    "idcity":"NT0002401",
    "phone": "12912344321",
    "sale_opportunity":1
}

vehicle_payload = {
    "name": "Camaro",
    "color": Colors.YELLOW,
    "model": VehicleModelTypes.CONVERTIBLE
}

customer_payload_validated = CustomerValidator(**customer_payload)
vehicle_payload_validated = VehicleValidator(**vehicle_payload)

vehicle_orm_model = [
    VehicleModel(
        customer_id=10,
        name=vehicle_payload_validated.name,
        color=vehicle_payload_validated.color.value,
        model=vehicle_payload_validated.model.value,
    )
]
customer_orm_model = [
    CustomerModel(
        name=customer_payload_validated.name,
        idcity=customer_payload_validated.idcity,
        phone=customer_payload_validated.phone,
        sale_opportunity=customer_payload_validated.sale_opportunity,
    )
]