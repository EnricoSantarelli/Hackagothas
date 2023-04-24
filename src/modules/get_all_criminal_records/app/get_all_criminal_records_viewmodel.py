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


class CrimeViewmodel:
    """Viewmodel responsible for translate the crime into a json"""
    crime_id: str
    crime_description: str
    date: int
    responsible_criminal: CriminalViewmodel
    crime_type: CRIME_TYPE
    crime_region: REGION
    seriousness: SERIOUSNESS

    def __init__(self, crime: Crime):
        """Crime Viewmodel constructor"""
        self.crime_id = crime.crime_id
        self.crime_type = crime.crime_type.value
        self.responsible_criminal = CriminalViewmodel(
            crime.responsible_criminal)
        self.date = crime.date
        self.crime_description = crime.crime_description
        self.crime_region = crime.crime_region.value
        self.seriousness = crime.seriousness.value

    def to_dict(self):
        """
            Function responsible to translate the crime into a json
        """
        return {
            "crime_id": self.crime_id,
            "crime_type": self.crime_type,
            "responsible_criminal": self.responsible_criminal.to_dict(),
            "date": self.date,
            "crime_description": self.crime_description,
            "crime_region": self.crime_region,
            "seriousness": self.seriousness
        }


class CriminalRecordViewmodel:
    """Viewmodel responsible for translate the criminal record into a json"""
    criminal_record_id: str
    danger_score: int
    criminal_owner: CriminalViewmodel
    is_arrested: bool
    prison: PRISON
    crime_list: list[CrimeViewmodel]

    def __init__(self, criminal_record: CriminalRecord):
        """Criminal Record Viewmodel constructor"""
        self.criminal_record_id = criminal_record.criminal_record_id
        self.crime_list = [CrimeViewmodel(crime)
                           for crime in criminal_record.crime_list]
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
            'crime_list': [(crime.to_dict()) for crime in self.crime_list],
            'criminal_owner': self.criminal_owner.to_dict(),
            'danger_score': self.danger_score,
            'is_arrested': self.is_arrested,
            'prison': self.prison,
        }


class GetAllCriminalRecordsViewmodel:
    """Viewmodel responsible for translate the criminal record with a message into a json when all criminal records is getted"""
    criminal_records: list[CriminalRecordViewmodel]

    def __init__(self, criminal_records_list: list[CriminalRecord]):
        """Delete Criminal Record Viewmodel constructor"""
        self.criminal_records = [CriminalRecordViewmodel(
            crimina_record) for crimina_record in criminal_records_list]

    def to_dict(self):
        """
            Function responsible to translate the criminal record with a message into a json when the all criminal records is getted
        """
        return {
            "criminal_records": [criminal_record.to_dict() for criminal_record in self.criminal_records],
            "message": 'all criminal records were found'
        }
