from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ExcededParameters, NoItemsFound


class CreateCriminalRecordUsecase:
    def __init__(self, repo_criminal_record: ICriminalRecordRepository):
        self.repo_criminal_record = repo_criminal_record

    def __call__(self, new_criminal_record_id: str, new_danger_score: int, new_criminal_owner: Criminal, new_is_arrested: bool, new_prison: PRISON) -> CriminalRecord:
        if not CriminalRecord.validate_criminal_record_id(new_criminal_record_id):
            raise EntityError("criminal_record_id")

        # validation if the new_prison is valid using the function validade_prison. It raises a entity error if returns false
        if not CriminalRecord.validate_prison(new_prison):
            raise EntityError("prison")

        # validation if the new_danger_score is valid using the function validade_danger_score It raises a entity error if returns false
        if not CriminalRecord.validate_danger_score(new_danger_score):
            raise EntityError("danger_score")

        # validation if the new_criminal_owner is valid using the function validade_criminal_owner It raises a entity error if returns false
        if not CriminalRecord.validate_criminal_owner(new_criminal_owner):
            raise EntityError("criminal_owner")

        # validation if the new_is_arrested is valid using the function validade_is_arrested. It raises a entity error if returns false
        if not CriminalRecord.validate_is_arrested(new_is_arrested):
            raise EntityError("is_arrested")
        
        # validation the business rule that can't exist a prison if the criminal isn't arrested and if the criminal is arrested must exist a prison
        if new_is_arrested == False and new_prison != None:
            raise ExcededParameters(
                "The parameter is_arrested must be true if you pass a prison!")
        if new_is_arrested == True and new_prison == None:
            raise MissingParameters("new_prison")

        return self.repo_criminal_record.create_criminal_record(new_criminal_record_id=new_criminal_record_id, new_criminal_owner=new_criminal_owner, new_danger_score=new_danger_score, new_is_arrested=new_is_arrested, new_prison=new_prison)

      
    