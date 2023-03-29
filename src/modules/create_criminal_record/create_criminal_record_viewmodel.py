from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS

class CrimeViewmodel:
    """View Model for a crime"""

    crime_id: str
    """The unique crime_id of the crime. \n
            Example: c303282d-f2e6-46ca-a04a-35d3d873712d 
    """

    crime_description: str
    """The description of how the crime occurred. \n
            Example: The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.
    """

    date: int  # miliseconds
    """The date the crime occurred. \n
            Example: 1585312648914
    """

    responsible_criminal: Criminal
    """The author of the crime. \n
            Example: Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)
    """

    crime_type: CRIME_TYPE
    """The type of the crime. \n
            Example: Murder
    """

    crime_region: REGION
    """The region in which the crime ocurred. \n
            Example: Industrial District. 
    """

    seriousness: SERIOUSNESS
    """The seriousness of the crime. \n
            Example: High. 
    """

    def __init__(self, crime: Crime):
        self.crime_id = crime.crime_id
        self.crime_description = crime.crime_description
        self.date = crime.date
        self.responsible_criminal = crime.responsible_criminal
        self.crime_type = crime.crime_type
        self.crime_region = crime.crime_region
        self.seriousness = crime.seriousness

    def to_dict(self) -> dict:
        return {
            "crime_id": self.crime_id,
            "crime_description": self.crime_description,
            "date": self.date,
            "responsible_criminal": self.responsible_criminal,
            "crime_type": self.crime_type,
            "crime_region": self.crime_region,
            "seriousness": self.seriousness,
        }

class CriminalViewmodel:
    """View Model for a criminal"""

    name: str
    """The name of the criminal. \n
            Example: Jack Oswald White 
    """

    nickname: str
    """The name in which the criminal is known for. \n
            Example: Joker 
    """

    criminal_description: str
    """The description of the criminal. It is not required. \n
            Example: A complete psychopath with no moral compass whatsoever, the Joker, is characterized by his chalk-white skin, green hair and a permanent rictus grin stretched across his face. But there isn’t a single thing funny about this particular clown, who only finds humor in the suffering of others. 
    """

    gender: GENDER
    """The gender of the crimminal, if there is one. \n
            Example: Male. 
    """

    region: REGION
    """The territory in which the criminal apears the most. \n
            Example: Industrial District. 
    """

    blood_type: BLOOD_TYPE
    """The blood type of the criminal. \n
            Example: A+. 
    """

    age: int
    """The age of the criminal. \n
            Example: 45. 
    """

    weight: float
    """The weight of the criminal in kilograms. \n
            Example: 80. 
    """

    height: float
    """The weight of the criminal in meters. \n
            Example: 1.80. 
    """

    def __init__(self, criminal: Criminal):
        """Criminal Viewmodel constructor"""
        self.name = criminal.name
        self.nickname = criminal.nickname
        self.criminal_description = criminal.criminal_description
        self.gender = criminal.gender
        self.criminal_region = criminal.criminal_region
        self.blood_type = criminal.blood_type
        self.age = criminal.age
        self.weight = criminal.weight
        self.height = criminal.height

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "nickname": self.nickname,
            "criminal_description": self.criminal_description,
            "gender": self.gender,
            "criminal_region": self.criminal_region,
            "blood_type": self.blood_type,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
        }

class CriminalRecordViewmodel:
    """View Model for a criminal record"""

    criminal_record_id: str
    """The unique id of the criminal record. \n
            Example: c303282d-f2e6-46ca-a04a-35d3d873712d 
    """

    danger_score: int
    """The danger score of the criminal with this criminal record. It varies between 1 to 5 as 5 being the most dangerous. \n
            Example: 4. 
    """

    criminal_owner: Criminal
    """The author of the crime. \n
            Example: Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)
    """

    is_arrested: bool
    """A bool value representing if the criminal is arrested at the moment.\n
            Example: true. 
    """

    prison: PRISON
    """The prison in which the criminal is arrested, it can only exist if the bool isArrested is true.\n
            Example: PRISON.BLACKGATE. 
    """


    def __init__(self, criminal_record: CriminalRecord):
        self.criminal_record_id = criminal_record.criminal_record_id
        self.danger_score = criminal_record.danger_score
        self.criminal_owner = criminal_record.criminal_owner
        self.is_arrested = criminal_record.is_arrested
        self.prison = criminal_record.prison

def to_dict(self) -> dict:
        return {
            "criminal_record_id": self.criminal_record_id,
            "danger_score": self.danger_score,
            "criminal_owner": self.criminal_owner,
            "is_arrested": self.is_arrested,
            "prison": self.prison,
        }

class CreateCriminalRecordViewlModel:
    """A function that creates a Criminal Record and emits a message if completed"""

    def __init__(self, criminal_record: CriminalRecord):
        self.criminal_record = CriminalRecordViewmodel(criminal_record)

    def to_dict(self) -> dict:
        return {
            "criminal_record": self.criminal_record.to_dict(),
            "message": "the criminal record was created"
        }    
       