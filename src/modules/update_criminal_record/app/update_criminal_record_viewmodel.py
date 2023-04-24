from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION


class CriminalViewmodel:
    """Viewmodel responsible for translate the criminal into a json"""
    name: str
    nickname: str
    criminal_description: str
    gender: GENDER
    criminal_region: REGION
    blood_type: BLOOD_TYPE
    age: int
    weight: float
    height: float

    def __init__(self, criminal: Criminal):
        """Criminal Viewmodel constructor"""
        self.name = criminal.name
        self.nickname = criminal.nickname
        self.age = criminal.age
        self.blood_type = criminal.blood_type.value
        self.criminal_description = criminal.criminal_description
        self.gender = criminal.gender.value
        self.height = criminal.height
        self.weight = criminal.weight
        self.criminal_region = criminal.criminal_region.value

    def to_dict(self):
        """
            Function responsible to translate the criminal into a json
        """
        return {
            "name": self.name,
            "nickname": self.nickname,
            "age": self.age,
            "blood_type": self.blood_type,
            "criminal_description": self.criminal_description,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "criminal_region": self.criminal_region
        }


class CriminalRecordViewmodel:
    """Viewmodel responsible for translate the criminal record into a json"""
    criminal_record_id: str
    danger_score: int
    criminal_owner: CriminalViewmodel
    is_arrested: bool
    prison: PRISON

    def __init__(self, criminal_record: CriminalRecord):
        """Criminal Record Viewmodel constructor"""
        self.criminal_record_id = criminal_record.criminal_record_id
        self.criminal_owner = CriminalViewmodel(criminal_record.criminal_owner)
        self.danger_score = criminal_record.danger_score
        self.is_arrested = criminal_record.is_arrested
        if (criminal_record.prison == None):
            self.prison = None
        else:
            self.prison = criminal_record.prison.value

    def to_dict(self):
        """
            Function responsible to translate the criminal record into a json
        """
        return {
            'criminal_record_id': self.criminal_record_id,
            'criminal_owner': self.criminal_owner.to_dict(),
            'danger_score': self.danger_score,
            'is_arrested': self.is_arrested,
            'prison': self.prison,
        }


class UpdateCriminalRecordViewmodel:
    """Viewmodel responsible for translate the criminal record with a message into a json when the criminal record is updated"""
    criminal_record: CriminalRecordViewmodel

    def __init__(self, criminal_record: CriminalRecord):
        """Update Criminal Record Viewmodel constructor"""
        self.criminal_record = CriminalRecordViewmodel(criminal_record)

    def to_dict(self):
        """
            Function responsible to translate the criminal record with a message into a json when the criminal record is updated
        """
        return {
            "criminal_record": self.criminal_record.to_dict(),
            "message": 'the criminal record was updated'
        }
