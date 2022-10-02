from pydantic import BaseModel, constr, Extra
from src.database.enums.enums import Colors, VehicleModelTypes

class VehicleValidator(BaseModel):
    color: Colors
    model: VehicleModelTypes

    class Config:
        extra = Extra.forbid