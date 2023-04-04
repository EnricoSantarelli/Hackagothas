from .get_criminal_record_usecase import GetCriminalRecordUsecase
from .get_criminal_record_viewmodel import GetCriminalRecordViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, OK
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class GetCriminalRecordController:
    """Controller of the route Get Criminal Record"""

    def __init__(self, usecase: GetCriminalRecordUsecase):
        """CriminalRecordController contructor instantiating the usecase"""
        self.getCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            # validation if the criminal_record_id is None. It raises a missing parameters if returns false
            if request.data.get("criminal_record_id") == None:
                raise MissingParameters("criminal_record_id")

            criminal_record_response = self.getCriminalRecordUsecase(
                criminal_record_id=request.data.get("criminal_record_id"))
            viewmodel = GetCriminalRecordViewmodel(
                criminal_record=criminal_record_response)

            return OK(body=viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
