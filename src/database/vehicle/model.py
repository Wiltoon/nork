from flask_sqlalchemy import SQLAlchemy

from src.database.enums.enums import Colors, VehicleModelTypes

db = SQLAlchemy()

class VehicleModel(db.Model):
    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    name = db.Column(db.String(15))
    color = db.Column(db.String(8), nullable=False)
    model = db.Column(db.String(15), nullable=False)

    def __init__(self, customer_id: int, color: Colors, model: VehicleModelTypes, name: str):
        self.customer_id = customer_id
        self.color = color
        self.name = name
        self.model = model

    @staticmethod
    def serialize_list(unserialized_vehicles_list):
        serialized_vehicles_list = []
        for VehicleModel in unserialized_vehicles_list:
            serialized_vehicles_list.append(VehicleModel.as_dict())
        return serialized_vehicles_list

    def as_dict(self):
        vehicle = {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "model": self.model,
            "customer_id": self.customer_id,
        }
        return vehicle