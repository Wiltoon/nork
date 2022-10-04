from flask_restful import Api

from src.controllers.routes import ListVehicles,ListCustomers,LinkVehicles, app
from src.utils.infra import SqliteInfrastructure

# Third party
from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)


SqliteInfrastructure.script_create_customer_table()
SqliteInfrastructure.script_create_vehicle_table()

api = Api(app)

api.add_resource(ListCustomers, '/customers')
api.add_resource(LinkVehicles, '/vehicle/<int:customer_id>')
api.add_resource(ListVehicles, '/vehicles')

app.run()
