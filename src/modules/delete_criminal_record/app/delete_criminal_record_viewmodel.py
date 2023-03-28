from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS


class CriminalViewmodel:
    """Viewmodel responsible for translate the criminal into a json"""
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
        """Criminal Viewmodel constructor"""
        self.name = criminal.name
        self.nickname = criminal.nickname
        self.age = criminal.age
        self.blood_type = criminal.blood_type.value
        self.description = criminal.description
        self.gender = criminal.gender.value
        self.height = criminal.height
        self.weight = criminal.weight
        self.region = criminal.region.value

    def to_dict(self):
        """
            Function responsible to translate the criminal into a json
        """
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


class CrimeViewmodel:
    """Viewmodel responsible for translate the crime into a json"""
    crime_id: str
    description: str
    date: int
    criminal: CriminalViewmodel
    crime_type: CRIME_TYPE
    region: REGION
    seriousness: SERIOUSNESS

    def __init__(self, crime: Crime):
        """Crime Viewmodel constructor"""
        self.crime_id = crime.crime_id
        self.crime_type = crime.crime_type.value
        self.criminal = CriminalViewmodel(crime.criminal)
        self.date = crime.date
        self.description = crime.description
        self.region = crime.region.value
        self.seriousness = crime.seriousness.value

    def to_dict(self):
        """
            Function responsible to translate the crime into a json
        """
        return {
            "crime_id": self.crime_id,
            "crime_type": self.crime_type,
            "criminal": self.criminal.to_dict(),
            "date": self.date,
            "description": self.description,
            "region": self.region,
            "seriousness": self.seriousness
        }


class CriminalRecordViewmodel:
    """Viewmodel responsible for translate the criminal record into a json"""
    criminal_record_id: str
    danger_score: int
    criminal: CriminalViewmodel
    is_arrested: bool
    prison: PRISON
    crime_list: list[CrimeViewmodel]

    def __init__(self, criminal_record: CriminalRecord):
        """Criminal Record Viewmodel constructor"""
        self.criminal_record_id = criminal_record.criminal_record_id
        self.crime_list = [CrimeViewmodel(crime)
                           for crime in criminal_record.crime_list]
        self.criminal = CriminalViewmodel(criminal_record.criminal)
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
            'crime_list': [(crime.to_dict()) for crime in self.crime_list],
            'criminal': self.criminal.to_dict(),
            'danger_score': self.danger_score,
            'is_arrested': self.is_arrested,
            'prison': self.prison,
        }


class DeleteCriminalRecordViewmodel:
    """Viewmodel responsible for translate the criminal record with a message into a json when the criminal record is deleted"""
    criminal_record: CriminalRecordViewmodel

    def __init__(self, criminal_record: CriminalRecord):
        """Delete Criminal Record Viewmodel constructor"""
        self.criminal_record = CriminalRecordViewmodel(criminal_record)

    def to_dict(self):
        """
            Function responsible to translate the criminal record with a message into a json when the criminal record is deleted
        """
        return {
            "criminal_record": self.criminal_record.to_dict(),
            "message": 'the criminal record was deleted'
        }
