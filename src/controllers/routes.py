from json import dumps
from http import HTTPStatus

from flask import Response, request, Flask, jsonify
from flask_restful import Resource

from src.database.exceptions.exception import VehicleLimit, CustomerNotFound
from src.database.validator.CustomerValidator import CustomerValidator
from src.database.validator.VehicleValidator import VehicleValidator
from src.utils.services import CustomerService

from loguru import logger


class ListCustomers(Resource):
    def post(self) -> Response:
        try:
            raw_payload = request.json
            payload_validated = CustomerValidator(**raw_payload)
            success = CustomerService.register_new_customer(
                payload_validated=payload_validated
            )
            response = {
                "success": success, 
                "message": "Customer registered with success!"
            }
            return Response(dumps(response), status=HTTPStatus.CREATED)

        except ValueError as ex:
            logger.error(ex)
            response = {"result": False, "message": "Invalid params"}
            return Response(dumps(response), status=HTTPStatus.BAD_REQUEST)

        except Exception as ex:
            logger.error(ex)
            print(ex)
            response = {"success": False, "message": "Error on register new client"}
            return Response(dumps(response), status=HTTPStatus.INTERNAL_SERVER_ERROR)
    def get(self):
        try:
            result = CustomerService.get_all_customers()
            response = {
                "success": True,
                "result": result
            }
            return Response(dumps(response), status=HTTPStatus.OK)

        except Exception as ex:
            logger.error(ex)
            response = {"success": False, "message": "Error on get customers"}
            return Response(dumps(response), status=HTTPStatus.INTERNAL_SERVER_ERROR)

class EspecificCustomer(Resource):
    def get(self, id) -> Response:
        try:
            result = CustomerService.get_customer_by_id(id)
            response = {
                "success": True, 
                "message": result
            }
            return Response(dumps(response), status=HTTPStatus.OK)

        except ValueError as ex:
            logger.error(ex)
            response = {"result": False, "message": "NOT FOUND"}
            return Response(dumps(response), status=HTTPStatus.NOT_FOUND)

        except Exception as ex:
            logger.error(ex)
            response = {"success": False, "message": "Error for search by id_customer"}
            return Response(dumps(response), status=HTTPStatus.NOT_FOUND)
    def put(self, id) -> Response:
        try:
            raw_payload = request.json
            payload_validated = CustomerValidator(**raw_payload)
            result = CustomerService.update_customer_by_id(
                payload_validated=payload_validated,
                id=id
            )
            response = {
                "success" : True,
                "message" : result
            }
            return Response(dumps(response), status=HTTPStatus.OK)

        except ValueError as ex:
            logger.error(ex)
            response = {"result": False, "message": "NOT FOUND"}
            return Response(dumps(response), status=HTTPStatus.NOT_FOUND)

        except Exception as ex:
            logger.error(ex)
            response = {"success": False, "message": "Error for search by id_customer"}
            return Response(dumps(response), status=HTTPStatus.NOT_FOUND)

class LinkVehicles(Resource):
    async def post(self, customer_id: int) -> Response:
        try:
            raw_payload = request.json
            payload_validated = VehicleValidator(**raw_payload)
            result = await CustomerService.linking_vehicle_to_owner(
                customer_id=customer_id, payload_validated=payload_validated
            )
            response = {"success": result, "message": "Vehicle registered successfully!"}
            return Response(dumps(response))

        except VehicleLimit as ex:
            logger.info(ex)
            response = {
                "success": False,
                "message": "Customer cannot have more than three cars, by Nork Town mayor.",
            }
            return Response(dumps(response), status=HTTPStatus.OK)

        except CustomerNotFound as ex:
            logger.info(ex)
            response = {"result": False, "message": "Customer not found."}
            return Response(dumps(response), status=HTTPStatus.NOT_FOUND)

        except ValueError as ex:
            logger.error(ex)
            response = {"success": False, "message": "Invalid params"}
            return Response(dumps(response), status=HTTPStatus.BAD_REQUEST)

        except Exception as ex:
            logger.error(ex)
            response = {"success": False, "message": "Error on linking vehicle on the owner"}
            return Response(dumps(response), status=HTTPStatus.INTERNAL_SERVER_ERROR)

class ListVehicles(Resource):
    async def get(self) -> Response:
        try:
            result = await CustomerService.get_all_vehicles()
            response = {
                "success": True,
                "result": result,
            }
            return Response(dumps(response), status=HTTPStatus.OK)

        except Exception as ex:
            logger.error(ex)
            response = {"success": False, "message": "Error on get vehicles list"}
            return Response(dumps(response), status=HTTPStatus.INTERNAL_SERVER_ERROR)