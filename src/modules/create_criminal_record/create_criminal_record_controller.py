from src.shared.domain.enums.prison_enum import PRISON
from .create_criminal_record_usecase import CreateCriminalRecordUsecase
from .create_criminal_record_viewmodel import CreateCriminalRecordViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import Created, NotFound, BadRequest, InternalServerError, OK
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class DeleteCriminalRecordController:
    """Controller of the route Delete Criminal Record"""

    def __init__(self, usecase: CreateCriminalRecordUsecase):
        """CriminalRecordController contructor instantiating the usecase"""
        self.createCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            # validation if the criminal_record_id is None. It raises a missing parameters if returns false
            if request.data.get("criminal_record_id") == None:
                raise MissingParameters("criminal_record_id")
            
            if request.data.get("danger_score") == None:
                raise MissingParameters("danger_score")
            
            if request.data.get("criminal_owner") == None:
                raise MissingParameters("criminal_owner")
            
            is_arrested = request.data.get("is_arrested")

            if is_arrested is None:   
                raise MissingParameters("is_arrested")
            
            
            prison =  request.data.get("prison")
            if prison is None:
                raise MissingParameters("prison")
            if prison not in [prison_value.value for prison_value in PRISON]:
                raise EntityError["prison"]
            
            
            

            criminal_record_response = self.createCriminalRecordUsecase(
                criminal_record_id=request.data.get("criminal_record_id"),
                danger_score=request.data.get("danger_score"),
                criminal_owner=request.data.get("criminal_owner"),
                is_arrested=request.data.get("is_arrested"),
                prison=request.data.get("prison"))

            viewmodel = CreateCriminalRecordViewmodel(criminal_record_response)

            return Created(body=viewmodel.to_dict())


        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])