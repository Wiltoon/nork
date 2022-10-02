from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = "CUSTOMER"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(16), nullable=False)
    id_city = Column(String(9))
    sale_opportunity = Column(Boolean, nullable=False)

    def __init__(self, name, sale_opportunity, phone, id_city):
        self.name = name
        self.sale_opportunity = sale_opportunity
        self.phone = phone
        self.id_city = id_city

    def as_dict(self):
        customer = {
            "id": self.id,
            "id_city": self.id_city,
            "name": self.name,
            "phone": self.phone,
            "sale_opportunity": self.sale_opportunity,
        }
        return customer