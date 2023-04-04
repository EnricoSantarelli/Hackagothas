from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ExcededParameters


class CreateCrimeUsecase():
    """Usecase of the route Create Crime Record"""

    def __init__(self, repo: ICriminalRecordRepository):
        self.repo = repo

    def __call__(self, crime_type: CRIME_TYPE, date: int, crime_description: str, responsible_criminal: Criminal, crime_region: REGION, seriousness: SERIOUSNESS) -> Crime:

        # validation the business rule that can't exist a crime with a inexistent criminal
        criminal_records = self.repo.get_all_criminal_records()
        for criminal_record in criminal_records:
            if criminal_record.criminal_owner == responsible_criminal:
                break
            raise ExcededParameters(
                "The criminal owner of the crime must be registered")

        # validation if the crime_region is valid using the function validade_crime_region. It raises a entity error if returns false
        if not Crime.validate_crime_region(crime_region):
            raise EntityError("crime_region")

        # validation if the seriousness is valid using the function validade_seriousness. It raises a entity error if returns false
        if not Crime.validate_seriousness(seriousness):
            raise EntityError("seriousness")

        # validation if the crime_type is valid using the function validade_crime_type. It raises a entity error if returns false
        if not Crime.validate_crime_type(crime_type):
            raise EntityError("crime_type")

        # validation if the date is valid using the function validade_date. It raises a entity error if returns false
        if not Crime.validate_date(date):
            raise EntityError("date")

        # validation if the crime_description is valid using the function validade_crime_description. It raises a entity error if returns false
        if not Crime.validate_crime_description(crime_description):
            raise EntityError("crime_description")

        # validation if the responsible_criminal is valid using the function validade_responsible_criminal. It raises a entity error if returns false
        if not Crime.validate_responsible_criminal(responsible_criminal):
            raise EntityError("responsible_criminal")

        return self.repo.create_crime(crime_type=crime_type, date=date, crime_description=crime_description, responsible_criminal=responsible_criminal, crime_region=crime_region, seriousness=seriousness)
