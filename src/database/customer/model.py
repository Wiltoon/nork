from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class CustomerModel(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, index=True)
    phone = db.Column(db.String(16))
    idcity = db.Column(db.String(9), nullable=False)
    sale_opportunity = db.Column(db.Integer)

    def __init__(self, name, sale_opportunity, phone, idcity):
        self.name = name
        self.sale_opportunity = sale_opportunity
        self.phone = phone
        self.idcity = idcity

    @staticmethod
    def serialize_list(unserialized_citizens_list):
        serialized_citizens_list = []
        for CustomerModel in unserialized_citizens_list:
            serialized_citizens_list.append(CustomerModel.as_dict())
        return serialized_citizens_list

    def as_dict(self):
        customer = {
            "id": self.id,
            "idcity": self.idcity,
            "name": self.name,
            "phone": self.phone,
            "sale_opportunity": self.sale_opportunity,
        }
        return customer