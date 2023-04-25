from src.shared.helpers.external_interfaces.http_codes import OK
from .update_criminal_record_usecase import UpdateCriminalRecordUsecase
from .update_criminal_record_viewmodel import UpdateCriminalRecordViewmodel
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
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
            # validation if the criminal_data is a dict when is not None. It raises a missing parameters if returns false
            criminal_data = request.data.get('new_criminal_owner')
            if not isinstance(criminal_data, dict) and criminal_data:
                raise EntityError('new_criminal_owner')
            
            # validation if the criminal_record_id is None. It raises a missing parameters if returns false
            if not request.data.get('criminal_record_id'):
                raise MissingParameters('criminal_record_id')
            if request.data.get('new_criminal_owner'):
                # validation if the criminal_region is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('criminal_region'):
                    raise MissingParameters('criminal_region')
                # validation if the blood_type is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('blood_type'):
                    raise MissingParameters('blood_type')
                # validation if the age is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('age'):
                    raise MissingParameters('age')
                # validation if the name is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('name'):
                    raise MissingParameters('name')
                # validation if the nickname is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('nickname'):
                    raise MissingParameters('nickname')
                # validation if the criminal_description is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('criminal_description'):
                    raise MissingParameters('criminal_description')
                # validation if the height is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('height'):
                    raise MissingParameters('height')
                # validation if the weight is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('weight'):
                    raise MissingParameters('weight')
                # validation if the gender is None. It raises a missing parameters if returns false
                if not request.data.get('new_criminal_owner').get('gender'):
                    raise MissingParameters('gender')
            
            if(request.data.get('new_danger_score')):
                # validation if the danger_score is decimal. It raises a entity error if returns false
                new_danger_score = request.data.get('new_danger_score')
                if not new_danger_score.isdecimal():
                    raise EntityError('new_danger_score')
                else:
                    new_danger_score = int(new_danger_score)
            else:
                new_danger_score = None

            if(request.data.get('new_criminal_owner').get('age') and request.data.get('new_criminal_owner')):
                # validation if the age is decimal. It raises a entity error if returns false
                new_age = request.data.get('new_criminal_owner').get('age')
                if not new_age.isdecimal():
                    raise EntityError('new_age')
                else:
                    new_age = int(new_age)

            if(request.data.get('new_criminal_owner').get('height') and request.data.get('new_criminal_owner')):
                # validation if the height is float. It raises a entity error if returns false
                new_height = request.data.get('new_criminal_owner').get('height')
                try:
                    new_height = float(new_height)
                except:
                    raise EntityError('new_height')

            if(request.data.get('new_criminal_owner').get('weight') and request.data.get('new_criminal_owner')):
                # validation if the weight is float. It raises a entity error if returns false
                new_weight = request.data.get('new_criminal_owner').get('weight')
                try:
                    new_weight = float(new_weight)
                except:
                    raise EntityError('new_weight')

            if(request.data.get('new_is_arrested')):
                # validation if the new_is_arrested is bool. It raises a entity error if returns false
                new_is_arrested = request.data.get('new_is_arrested')
                if new_is_arrested.lower() != 'true' and new_is_arrested.lower() != 'false':
                    raise EntityError('new_is_arrested')
                else:
                    if(new_is_arrested == 'True'):
                        new_is_arrested = True
                    else:
                        new_is_arrested = False
            else:
                new_is_arrested = None

            if(request.data.get('new_prison')):
            # validation if the type of the new_prison is wrong. It raises a entity error if returns false
                if request.data.get("new_prison") not in [prison_value.value for prison_value in PRISON]:
                    raise EntityError('new_prison')
                new_prison = PRISON[request.data.get("new_prison")]
            else:
                new_prison = None
            if(request.data.get('new_criminal_owner').get('criminal_region') and request.data.get('new_criminal_owner')):
                # validation if the type of the criminal_region is wrong. It raises a entity error if returns false
                if request.data.get("new_criminal_owner").get("criminal_region") not in [region_value.value for region_value in REGION]:
                    raise EntityError('criminal_region')
                new_region = REGION[request.data.get(
                    "new_criminal_owner").get("criminal_region")]
            if(request.data.get('new_criminal_owner').get('blood_type') and request.data.get('new_criminal_owner')):
                # validation if the type of the blood_type is wrong. It raises a entity error if returns false
                if request.data.get(
                        "new_criminal_owner").get("blood_type") not in [blood_type.value for blood_type in BLOOD_TYPE]:
                    raise EntityError('blood_type')
                new_blood_type = BLOOD_TYPE[request.data.get(
                    "new_criminal_owner").get("blood_type")]
            if(request.data.get('new_criminal_owner').get('gender') and request.data.get('new_criminal_owner')):
                # validation if the type of the gender is wrong. It raises a entity error if returns false
                if request.data.get(
                        "new_criminal_owner").get("gender") not in [gender.value for gender in GENDER]:
                    raise EntityError('gender')
                new_gender = GENDER[request.data.get(
                    "new_criminal_owner").get("gender")]

            if(request.data.get('new_criminal_owner')):
                valid_keys = ['name', 'nickname', 'age', 'blood_type', 'gender',
                            'criminal_description', 'height', 'weight', 'criminal_region']
                if not all(key in valid_keys for key in request.data.get('new_criminal_owner').keys()):
                    raise EntityError('new_criminal_owner')

            if(request.data.get('new_criminal_owner')):
                try:
                    new_criminal_owner = Criminal(age=new_age, blood_type=new_blood_type, name=request.data.get('new_criminal_owner').get('name'), nickname=request.data.get('new_criminal_owner').get('nickname'), criminal_description=request.data.get('new_criminal_owner').get('criminal_description'),
                                                criminal_region=new_region, gender=new_gender, height=new_height, weight=new_weight)
                except:
                    raise EntityError('new_criminal_owner')
            else:
                new_criminal_owner = None
            

            new_criminal_record = self.updateCriminalRecordUsecase(new_criminal_owner=new_criminal_owner, criminal_record_id=request.data.get(
                "criminal_record_id"), new_danger_score=new_danger_score, new_is_arrested=new_is_arrested, new_prison=new_prison)

            viewmodel = UpdateCriminalRecordViewmodel(new_criminal_record)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
