from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS


class CriminalViewModel:
    name: str
    nickname: str
    description: str
    gender: GENDER
    region: REGION
    blood_type: BLOOD_TYPE
    age: int
    weight: float
    height: float

    def __init__(self, criminal: Criminal):
        self.name = criminal.name
        self.nickname = criminal.nickname
        self.age = criminal.age
        self.blood_type = criminal.blood_type
        self.description = criminal.description
        self.gender = criminal.gender
        self.height = criminal.height
        self.weight = criminal.weight
        self.region = criminal.region

    def to_dict(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "age": self.age,
            "blood_type": self.blood_type,
            "description": self.description,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "region": self.region
        }


class CrimeViewModel:
    crime_id: str
    description: str
    date: int
    criminal: Criminal
    crime_type: CRIME_TYPE
    region: REGION
    seriousness: SERIOUSNESS

    def __init__(self, crime: Crime):
        self.crime_id = crime.crime_id
        self.crime_type = crime.crime_type
        self.criminal = CriminalViewModel()
        self.date = crime.date
        self.description = crime.description
        self.region = crime.region
        self.seriousness = crime.seriousness

    def to_dict(self):
        return {
            "crime_id": self.crime_id,
            "crime_type": self.crime_type,
            "criminal": self.criminal.to_dict(),
            "date": self.date,
            "description": self.description,
            "region": self.region,
            "seriousness": self.seriousness
        }


class CriminalRecordViewModel:
    criminal_record_id: str
    danger_score: int
    criminal: Criminal
    is_arrested: bool
    prison: PRISON
    crime_list: list[Crime]

    def __init__(self, criminal_record: CriminalRecord):
        self.criminal_record_id = criminal_record.criminal_record_id
        self.crime_list = criminal_record.crime_list
        self.criminal = criminal_record.criminal
        self.danger_score = criminal_record.danger_score
        self.is_arrested = criminal_record.is_arrested
        self.prison = criminal_record.prison

    def to_dict(self):
        return {
            'criminal_record_id': self.criminal_record_id,
            'crime_list': self.crime_list,
            'criminal': self.criminal,
            'danger_score': self.danger_score,
            'is_arrested': self.is_arrested,
            'prison': self.prison,
            'message': "the criminal_record was deleted successfully"
        }
