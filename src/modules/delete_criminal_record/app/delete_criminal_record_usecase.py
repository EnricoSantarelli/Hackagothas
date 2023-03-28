from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteCriminalRecordUsecase:
    """Usecase of the route Delete Criminal Record"""

    def __init__(self, repo: ICriminalRecordRepository):
        """Delete Criminal Record Usecase constructor instantiating the repository"""
        self.repo = repo

    def __call__(self, criminal_record_id: str) -> CriminalRecord:

        # validation if the criminal_record_id is valid using the function validade_criminal_record_id. It raises a entity error if returns false
        if not CriminalRecord.validate_criminal_record_id(criminal_record_id=criminal_record_id):
            raise EntityError("criminal_record_id")

        # get the criminal record in the repository mock with the id passed
        criminal_record = self.repo.get_criminal_record(
            criminal_record_id=criminal_record_id)

        # validation if the criminal_record_id exists. It raises a no items found if it doesn't exists
        if criminal_record is None:
            raise NoItemsFound("criminal_record")

        # delete the criminal record if all the validation pass
        criminal_record = self.repo.delete_criminal_record(
            criminal_record_id=criminal_record_id)

        return criminal_record
