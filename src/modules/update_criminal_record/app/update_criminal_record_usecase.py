from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateCriminalRecordUsecase:
    """Usecase of the route Update Criminal Record"""

    def __init__(self, repo: ICriminalRecordRepository):
        """Update Criminal Record Usecase constructor instantiating the repository"""
        self.repo = repo

    def __call__(self, criminal_record_id: str, new_danger_score: int, new_criminal_owner: Criminal, new_is_arrested: bool, new_prison: PRISON) -> CriminalRecord:

        # validation if the criminal_record_id is valid using the function validade_criminal_record_id. It raises a entity error if returns false
        if not CriminalRecord.validate_criminal_record_id(criminal_record_id=criminal_record_id):
            raise EntityError("criminal_record_id")

        # get the criminal record in the repository mock with the id passed
        criminal_record = self.repo.get_criminal_record(
            criminal_record_id=criminal_record_id)

        # validation if the criminal_record_id exists. It raises a no items found if it doesn't exists
        if criminal_record is None:
            raise NoItemsFound("criminal_record")

        # validation the business rule that can't exist a prison if the criminal isn't arrested and if the criminal is arrested must exist a prison
        if new_is_arrested == False and new_prison != None:
            raise EntityError("new_prison")
        if new_is_arrested == True and criminal_record.prison == None and new_prison == None:
            raise EntityError("new_prison")

        # validation if the new_prison is valid using the function validade_prison. It raises a entity error if returns false
        if not CriminalRecord.validate_prison(new_prison):
            raise EntityError("new_prison")

        # validation if the new_danger_score is valid using the function validade_danger_score It raises a entity error if returns false
        if not CriminalRecord.validate_danger_score(new_danger_score):
            raise EntityError("new_danger_score")

        # validation if the new_criminal_owner is valid using the function validade_criminal_owner It raises a entity error if returns false
        if not CriminalRecord.validate_criminal_owner(new_criminal_owner):
            raise EntityError("new_criminal_owner")

        # validation if the new_is_arrested is valid using the function validade_is_arrested. It raises a entity error if returns false
        if not CriminalRecord.validate_is_arrested(new_is_arrested):
            raise EntityError("new_is_arrested")

        return self.repo.update_criminal_record(criminal_record_id=criminal_record_id, new_criminal_owner=new_criminal_owner, new_danger_score=new_danger_score, new_is_arrested=new_is_arrested, new_prison=new_prison)
