from http.client import OK
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUsecase
from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewmodel
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
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
            # validation if the danger_score is None. It raises a missing parameters if returns false
            if not request.data.get('danger_score'):
                raise MissingParameters('danger_score')
            # validation if the criminal_owner is None. It raises a missing parameters if returns false
            if not request.data.get('criminal_owner'):
                raise MissingParameters('criminal_owner')
            # validation if the is_arrested is None. It raises a missing parameters if returns false
            if not request.data.get('is_arrested'):
                raise MissingParameters('is_arrested')
            # validation if the age is None. It raises a missing parameters if returns false
            if not request.data.get('age'):
                raise MissingParameters('age')
            # validation if the criminal_description is None. It raises a missing parameters if returns false
            if not request.data.get('criminal_description'):
                raise MissingParameters('criminal_description')
            # validation if the name is None. It raises a missing parameters if returns false
            if not request.data.get('name'):
                raise MissingParameters('name')
            # validation if the nickname is None. It raises a missing parameters if returns false
            if not request.data.get('nickname'):
                raise MissingParameters('nickname')
            # validation if the weight is None. It raises a missing parameters if returns false
            if not request.data.get('weight'):
                raise MissingParameters('weight')

            gender_values = [val.value for val in GENDER]
            if request.data.get("gender") not in gender_values:
                raise EntityError("gender")
            gender = GENDER[request.data.get("gender")]

            criminal_region_values = [val.value for val in REGION]
            if request.data.get("criminal_region") not in criminal_region_values:
                raise EntityError("criminal_region")
            criminal_region = REGION[request.data.get("criminal_region")]

            crime_region_values = [val.value for val in REGION]
            if request.data.get("crime_region") not in crime_region_values:
                raise EntityError("crime_region")
            crime_region = REGION[request.data.get("criminal_region")]

            blood_type_values = [val.value for val in BLOOD_TYPE]
            if request.data.get("blood_type") not in blood_type_values:
                raise EntityError("blood_type")
            blood_type = BLOOD_TYPE[request.data.get("blood_type")]

            prison_values = [val.value for val in PRISON]
            if request.data.get("prison") not in prison_values:
                raise EntityError("prison")
            prison = PRISON[request.data.get("prison")]

            criminal = Criminal(age=request.data.get("age"), blood_type=blood_type, criminal_description=request.data.get("criminal_description"), criminal_region=criminal_region,
                                gender=gender, height=request.data.get("height"), name=request.data.get("name"), nickname=request.data.get("nickname"), weight=request.data.get("weight"))
            criminal_record = CriminalRecord(criminal_owner=criminal, criminal_record_id=request.data.get(
                "criminal_record_id"), danger_score=request.data.get("danger_score"), is_arrested=request.data.get("is_arrested"), prison=prison)
            viewmodel = UpdateCriminalRecordViewmodel(criminal_record)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
