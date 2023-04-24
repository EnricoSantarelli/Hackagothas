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


class CreateCrimeViewmodel:
    """Viewmodel responsible for translate the criminal record with a message into a json when a crime is created"""
    crime_description: str
    crime_type: CRIME_TYPE
    date: int
    seriousness: SERIOUSNESS
    crime_region: REGION
    responsible_criminal: CriminalViewmodel

    def __init__(self, crime_description: str, crime_type: CRIME_TYPE, date: int, seriousness: SERIOUSNESS, crime_region: REGION, responsible_criminal: Criminal):
        """Create Crime Viewmodel constructor"""
        self.crime_description = crime_description
        self.crime_type = crime_type.value
        self.date = date
        self.seriousness = seriousness.value
        self.crime_region = crime_region.value
        self.responsible_criminal = CriminalViewmodel(
            criminal=responsible_criminal)

    def to_dict(self):
        """
            Function responsible to translate the criminal record with a message into a json when the all criminal records is getted
        """
        return {
            "crime": {
                "crime_description": self.crime_description,
                "crime_type": self.crime_type,
                "date": self.date,
                "seriousness": self.seriousness,
                "crime_region": self.crime_region,
                "responsible_criminal": self.responsible_criminal.to_dict()
            },
            "message": 'the crime was created'
        }
