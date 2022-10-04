from src.database.enums.enums import Colors, VehicleModelTypes

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class VehicleModel(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    name = Column(String(15))
    color = Column(String(8), nullable=False)
    model = Column(String(15), nullable=False)

    def __init__(self, customer_id: int, color: Colors, model: VehicleModelTypes, name: str):
        self.customer_id = customer_id
        self.color = color
        self.name = name
        self.model = model

    def as_dict(self):
        vehicle = {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "model": self.model,
            "customer_id": self.customer_id,
        }
        return vehicle