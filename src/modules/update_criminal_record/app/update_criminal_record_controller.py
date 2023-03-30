from http.client import OK
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUsecase
from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewmodel
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class UpdateCriminalRecordController:
    """Controller of the route Update Criminal Record"""

    def __init__(self, usecase: UpdateCriminalRecordUsecase):
        """CriminalRecordController contructor instantiating the usecase"""
        self.updateCriminalRecordUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            # validation if the criminal_record_id is None. It raises a missing parameters if returns false
            if not request.data.get('criminal_record_id'):
                raise MissingParameters('criminal_record_id')
            # validation if the new_danger_score is None. It raises a missing parameters if returns false
            if not request.data.get('new_danger_score'):
                raise MissingParameters('new_danger_score')
            # validation if the new_criminal_owner is None. It raises a missing parameters if returns false
            if not request.data.get('new_criminal_owner'):
                raise MissingParameters('new_criminal_owner')
            # validation if the new_is_arrested is None. It raises a missing parameters if returns false
            if not request.data.get('new_is_arrested'):
                raise MissingParameters('new_is_arrested')
            # validation if the new_prison is None. It raises a missing parameters if returns false
            if not request.data.get('new_prison'):
                raise MissingParameters('new_prison')

            if request.data.get("new_prison") not in [prison_value.value for prison_value in PRISON]:
                raise EntityError('new_prison')
            new_prison = PRISON[request.data.get("new_prison")]

            new_criminal_owner = request.data.get("new_criminal_owner")
            new_criminal_record = self.updateCriminalRecordUsecase(new_criminal_owner=new_criminal_owner, criminal_record_id=request.data.get(
                "criminal_record_id"), new_danger_score=request.data.get("new_danger_score"), new_is_arrested=request.data.get("new_is_arrested"), new_prison=new_prison)

            viewmodel = UpdateCriminalRecordViewmodel(
                criminal_record=new_criminal_record)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
