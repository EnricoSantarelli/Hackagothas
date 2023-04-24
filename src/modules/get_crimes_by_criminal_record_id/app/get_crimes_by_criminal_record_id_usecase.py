from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetCrimesByCriminalRecordIdUsecase:
    def __init__(self, repo: ICriminalRecordRepository):
        self.repo = repo

    def __call__(self, criminal_record_id: str):
        if not CriminalRecord.validate_criminal_record_id(criminal_record_id):
            raise EntityError("criminal_record_id")

        return self.repo.get_crimes_by_criminal_record_id(criminal_record_id)
