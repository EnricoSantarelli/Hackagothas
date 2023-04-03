from abc import ABC, abstractmethod
from ast import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.prison_enum import PRISON


class ICriminalRecordRepository(ABC):

    @abstractmethod
    def get_criminal_record(self, criminal_record_id: str) -> CriminalRecord:
        """
            Abstract function that returns the criminal record of the passed criminal record id
        """
        pass

    @abstractmethod
    def create_criminal_record(self, criminal_record: CriminalRecord) -> CriminalRecord:
        """
            Abstract function that creates and return a new criminal record
        """
        pass

    @abstractmethod
    def update_criminal_record(self, criminal_record_id: str, new_danger_score: int = None, new_criminal_owner: Criminal = None, new_is_arrested: bool = None, new_prison: PRISON = None) -> CriminalRecord:
        """
            Abstract Function that updates and return a new criminal record of the passed criminal record id
        """
        pass

    @abstractmethod
    def delete_criminal_record(self, criminal_record_id: str) -> CriminalRecord:
        """
            Abstract function that delete a criminal record of the list criminal_records
        """
        pass

    @abstractmethod
    def get_all_criminal_records(self) -> list[CriminalRecord]:
        """
            Abstract function that returns all the criminal records
        """
        pass
