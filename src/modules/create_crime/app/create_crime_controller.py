from .create_crime_usecase import CreateCrimeUsecase
from .create_crime_viewmodel import CreateCrimeViewmodel
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class CreateCrimeController:
    """Controller of the route Create Crime"""

    def __init__(self, usecase: CreateCrimeUsecase):
        """CreateCrimeController contructor instantiating the usecase"""
        self.createCrimeUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:

            # validation if the criminal_data is a dict when is not None. It raises a missing parameters if returns false
            criminal_data = request.data.get('responsible_criminal')
            if not isinstance(criminal_data, dict) and criminal_data:
                raise EntityError('responsible_criminal')

            # validation if the crime_type is None. It raises a missing parameters if returns false
            if not request.data.get("crime_type"):
                raise MissingParameters("crime_type")

            # validation if the date is None. It raises a missing parameters if returns false
            if not request.data.get("date"):
                raise MissingParameters("date")

            # validation if the crime_description is None. It raises a missing parameters if returns false
            if not request.data.get("crime_description"):
                raise MissingParameters("crime_description")

            # validation if the responsible_criminal is None. It raises a missing parameters if returns false
            if not request.data.get("responsible_criminal"):
                raise MissingParameters("responsible_criminal")

            # validation if the crime_region is None. It raises a missing parameters if returns false
            if not request.data.get("crime_region"):
                raise MissingParameters("crime_region")

            # validation if the seriousness is None. It raises a missing parameters if returns false
            if not request.data.get("seriousness"):
                raise MissingParameters("seriousness")

            # validation if the criminal_region is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('criminal_region'):
                raise MissingParameters('criminal_region')

            # validation if the blood_type is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('blood_type'):
                raise MissingParameters('blood_type')

            # validation if the age is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('age'):
                raise MissingParameters('age')

            # validation if the name is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('name'):
                raise MissingParameters('name')

            # validation if the nickname is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('nickname'):
                raise MissingParameters('nickname')

            # validation if the criminal_description is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('criminal_description'):
                raise MissingParameters('criminal_description')

            # validation if the height is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('height'):
                raise MissingParameters('height')

            # validation if the weight is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('weight'):
                raise MissingParameters('weight')

            # validation if the gender is None. It raises a missing parameters if returns false
            if not request.data.get('responsible_criminal').get('gender'):
                raise MissingParameters('gender')

            # validation if the type of the crime_region is wrong. It raises a entity error if returns false
            if request.data.get("crime_region") not in [region_value.value for region_value in REGION]:
                raise EntityError('crime_region')
            crime_region = REGION[request.data.get(
                "crime_region")]

            # validation if the type of the seriousness is wrong. It raises a entity error if returns false
            if request.data.get("seriousness") not in [seriousness_value.value for seriousness_value in SERIOUSNESS]:
                raise EntityError('seriousness')
            seriousness = SERIOUSNESS[request.data.get(
                "seriousness")]

            # validation if the type of the crime_type is wrong. It raises a entity error if returns false
            if request.data.get("crime_type") not in [crime_type_value.value for crime_type_value in CRIME_TYPE]:
                raise EntityError('crime_type')
            crime_type = CRIME_TYPE[request.data.get(
                "crime_type")]

            # validation if the type of the criminal_region is wrong. It raises a entity error if returns false
            if request.data.get(
                    "responsible_criminal").get("criminal_region") not in [criminal_region.value for criminal_region in REGION]:
                raise EntityError('criminal_region')
            criminal_region = REGION[request.data.get(
                "responsible_criminal").get("criminal_region")]

            # validation if the type of the blood_type is wrong. It raises a entity error if returns false
            if request.data.get(
                    "responsible_criminal").get("blood_type") not in [blood_type.value for blood_type in BLOOD_TYPE]:
                raise EntityError('blood_type')
            blood_type = BLOOD_TYPE[request.data.get(
                "responsible_criminal").get("blood_type")]
            # validation if the type of the gender is wrong. It raises a entity error if returns false
            if request.data.get(
                    "responsible_criminal").get("gender") not in [gender.value for gender in GENDER]:
                raise EntityError('gender')
            gender = GENDER[request.data.get(
                "responsible_criminal").get("gender")]

            valid_keys = ['name', 'nickname', 'age', 'blood_type', 'gender',
                          'criminal_description', 'height', 'weight', 'criminal_region']
            if not all(key in valid_keys for key in request.data.get('responsible_criminal').keys()):
                raise EntityError('responsible_criminal')

            # validation if the date is decimal. It raises a entity error if returns false
            date = request.data.get('date')
            if not date.isdecimal():
                raise EntityError('date')
            else:
                date = int(date)

            # validation if the age is decimal. It raises a entity error if returns false
            age = request.data.get('responsible_criminal').get('age')
            if not age.isdecimal():
                raise EntityError('age')
            else:
                age = int(age)

            # validation if the height is float. It raises a entity error if returns false
            height = request.data.get('responsible_criminal').get('height')
            try:
                height = float(height)
            except:
                raise EntityError('height')

            # validation if the weight is float. It raises a entity error if returns false
            weight = request.data.get('responsible_criminal').get('weight')
            try:
                weight = float(weight)
            except:
                raise EntityError('weight')

            try:
                responsible_criminal = Criminal(age=age, blood_type=blood_type, name=request.data.get('responsible_criminal').get('name'), nickname=request.data.get('responsible_criminal').get('nickname'), criminal_description=request.data.get('responsible_criminal').get('criminal_description'),
                                                criminal_region=criminal_region, gender=gender, height=height, weight=weight)
            except:
                raise EntityError('new_criminal_owner')

            crime = self.createCrimeUsecase(crime_description=request.data.get('crime_description'), crime_region=crime_region,
                                            crime_type=crime_type, date=date, seriousness=seriousness, responsible_criminal=responsible_criminal)

            viewmodel = CreateCrimeViewmodel(crime_description=request.data.get('crime_description'), crime_region=crime_region,
                                             crime_type=crime_type, date=date, seriousness=seriousness, responsible_criminal=responsible_criminal)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
