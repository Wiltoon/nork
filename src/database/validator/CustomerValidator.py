from pydantic import BaseModel, constr, Extra
from src.database.enums.enums import Colors, VehicleModelTypes

class CustomerValidator(BaseModel):
    name: constr(max_length=50)
    phone: constr(max_length=16)
    id_city: constr(max_length=9)

    sale_opportunity: bool = True

    class Config:
        extra = Extra.forbid