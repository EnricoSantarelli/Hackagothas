from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository


class UpdateCriminalRecordUsecase:
    """Usecase of the route Update Criminal Record"""

    def __init__(self, repo: ICriminalRecordRepository):
        self.repo = repo

    def __call__(self, criminal_record_id: str, new_danger_score: int, new_criminal: Criminal, new_is_arrested: bool, new_prison: PRISON, new_crime_list: list[Crime]) -> CriminalRecord:
        
