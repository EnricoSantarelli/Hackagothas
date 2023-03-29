from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, OK, Forbidden
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
            if request.data.get("criminal_region") == None:
                raise MissingParameters("criminal_region")
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
            if request.data.get("crime_region") == None:
                raise MissingParameters("crime_region")
            if request.data.get("seriousness") == None:
                raise MissingParameters("seriousness")

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
            seriousness_values = [val.value for val in SERIOUSNESS]
            if request.data.get("seriousness") not in seriousness_values:
                raise EntityError("seriousness")
            seriousness = SERIOUSNESS[request.data.get("seriousness")]
            prison_values = [val.value for val in PRISON]
            if request.data.get("prison") not in prison_values:
                raise EntityError("prison")
            prison = PRISON[request.data.get("prison")]
            crime_type_values = [val.value for val in CRIME_TYPE]
            if request.data.get("crime_type") not in crime_type_values:
                raise EntityError("crime_type")
            crime_type = CRIME_TYPE[request.data.get("crime_type")]

            criminal = Criminal(age=request.data.get("age"), blood_type=blood_type, criminal_description=request.data.get("criminal_description"), criminal_region=criminal_region,
                                gender=gender, height=request.data.get("height"), name=request.data.get("name"), nickname=request.data.get("nickname"), weight=request.data.get("weight"))
            crime = Crime(crime_description=request.data.get("description"), crime_id=request.data.get("crime_id"), crime_region=crime_region, crime_type=crime_type,
                          date=request.data.get("date"), responsible_criminal=criminal, seriousness=seriousness)
            criminal_record = CriminalRecord(crime_list=[crime], criminal_owner=criminal, criminal_record_id=request.data.get(
                "criminal_record_id"), danger_score=request.data.get("danger_score"), is_arrested=request.data.get("is_arrested"), prison=prison)

            criminal_record_response = self.DeleteCriminalRecordUsecase(
                criminal_record_id=criminal_record.criminal_record_id)
            viewmodel = DeleteCriminalRecordViewmodel(
                criminal_record=criminal_record_response)

            return OK(body=viewmodel.to_dict())

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
