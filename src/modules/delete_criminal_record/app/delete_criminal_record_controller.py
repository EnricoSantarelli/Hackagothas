from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created, Forbidden
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class DeleteCriminalRecordController:

    def __init__(self, usecase: DeleteCriminalRecordUsecase):
        self.DeleteCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.data.get("criminal_record_id") == None:
                raise MissingParameters("criminal_record_id")
            if request.data.get("danger_score") == None:
                raise MissingParameters("danger_score")
            if request.data.get("criminal") == None:
                raise MissingParameters("criminal")
            if request.data.get("name") == None:
                raise MissingParameters("name")
            if request.data.get("gender") == None:
                raise MissingParameters("gender")
            if request.data.get("region") == None:
                raise MissingParameters("region")
            if request.data.get("blood_type") == None:
                raise MissingParameters("blood_type")
            if request.data.get("age") == None:
                raise MissingParameters("age")
            if request.data.get("weight") == None:
                raise MissingParameters("weight")
            if request.data.get("height") == None:
                raise MissingParameters("height")
            if request.data.get("is_arrested") == None:
                raise MissingParameters("is_arrested")
            if request.data.get("crime_list") == None:
                raise MissingParameters("crime_list")
            if request.data.get("crime_id") == None:
                raise MissingParameters("crime_id")
            if request.data.get("crime_type") == None:
                raise MissingParameters("crime_type")
            if request.data.get("region") == None:
                raise MissingParameters("region")
            if request.data.get("seriousness") == None:
                raise MissingParameters("seriousness")

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
