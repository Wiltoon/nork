from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from src.controllers.routes import ListVehicles,ListCustomers,LinkVehicles,EspecificCustomer
from src.utils.infra import PostgreSQLInfrastructure

# Third party
from asgiref.wsgi import WsgiToAsgi

# Inicializar objeto central app do Flask.
app = Flask(__name__)

# Incializar objeto central db do SQLAlchemy.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:0254@localhost:5433/norktown'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret string'
db = SQLAlchemy(app)

api = Api(app)

api.add_resource(ListCustomers, '/customers')
api.add_resource(EspecificCustomer, '/customers/<int:id>')
api.add_resource(LinkVehicles, '/vehicle/<int:customer_id>')
api.add_resource(ListVehicles, '/vehicles')
# Definir debug, endereço e porta.
if __name__ == '__main__':
    from waitress import serve
    with app.app_context():
        db.create_all()
    # app.run()
    app.run(
        host='0.0.0.0',
        port=8080
    )
    # app.config.update(
    #     SESSION_COOKIE_SECURE=True,
    #     SESSION_COOKIE_HTTPONLY=True,
    #     SESSION_COOKIE_SAMESITE='Lax',
    # )
