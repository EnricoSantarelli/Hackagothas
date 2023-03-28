import abc

from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.helpers.errors.domain_errors import EntityError


class Crime(abc.ABC):
    """Entity responsible for characterize a crime"""

    crime_id: str
    """The unique crime_id of the crime. \n
            Example: c303282d-f2e6-46ca-a04a-35d3d873712d 
    """

    description: str
    """The description of how the crime occurred. \n
            Example: The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.
    """

    date: int  # miliseconds
    """The date the crime occurred. \n
            Example: 1585312648914
        """

    criminal: Criminal
    """The author of the crime. \n
            Example: Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)
    """

    crime_type: CRIME_TYPE
    """The type of the crime. \n
            Example: Murder
    """

    region: REGION
    """The region in which the crime ocurred. \n
            Example: Industrial District. 
    """

    seriousness: SERIOUSNESS
    """The seriousness of the crime. \n
            Example: High. 
    """

    ID_LENGTH = 36
    """The string lenght is equal to 36. \n"""

    def __init__(self, crime_id: str, date: int, criminal: Criminal, crime_type: CRIME_TYPE, region: REGION, seriousness: SERIOUSNESS, description: str = None):
        """Crime class constructor"""

        # validation if the id is valid using the function validade_id. It raises a entity error if returns false
        if not Crime.validate_crime_id(crime_id):
            raise EntityError("crime_id")
        self.crime_id = crime_id

        # validation if the description is valid using the function validade_description. It raises a entity error if returns false
        if not Crime.validate_description(description):
            raise EntityError("description")
        self.description = description

        # validation if the date is valid using the function validade_date. It raises a entity error if returns false
        if not Crime.validate_date(date):
            raise EntityError("date")
        self.date = date

        # validation if the criminal is valid using the function validade_criminal. It raises a entity error if returns false
        if not Crime.validate_criminal(criminal):
            raise EntityError("criminal")
        self.criminal = criminal

        # validation if the crime_type is valid using the function validade_crime_type. It raises a entity error if returns false
        if not Crime.validate_crime_type(crime_type):
            raise EntityError("crime_type")
        self.crime_type = crime_type

        # validation if the region is valid using the function validade_region. It raises a entity error if returns false
        if not Crime.validate_region(region):
            raise EntityError("region")
        self.region = region

        # validation if the seriousness is valid using the function validade_seriousness. It raises a entity error if returns false
        if not Crime.validate_seriousness(seriousness):
            raise EntityError("seriousness")
        self.seriousness = seriousness

    @staticmethod
    def validate_crime_id(crime_id: str) -> bool:
        """The function that validates the id, it returns false if the id is none, the type is wrong or if its diferent of the necessary size. \n
            Example: crime_id = 2.3 -> False 
            Example: crime_id = None -> False 
            Example: crime_id = "c303282d-f2e6-46ca-a04a-35d3" -> False
            Example: crime_id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> True 
        """
        if crime_id is None:
            return False
        elif type(crime_id) != str:
            return False
        elif len(crime_id) != Crime.ID_LENGTH:
            return False
        return True

    @staticmethod
    def validate_description(description: str) -> bool:
        """The function that validates the description, it returns false if the type is wrong. \n
            Example: decription = 30 -> False 
            Example: decription = "The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind." -> True 
        """
        if type(description) != str:
            return False
        return True

    @staticmethod
    def validate_date(date: int) -> bool:
        """The function that validates the date, it returns false if the type is wrong, if the date is none or if its not betwenn is not in the range of 1000000000000 to 10000000000000. \n
            Example: date = "1585312648914" -> False 
            Example: date = 158531 -> False 
            Example: date = 1585312648914-> True 
        """
        if date is None:
            return False
        elif type(date) != int:
            return False
        elif not 1000000000000 < date < 10000000000000:
            return False
        return True

    @staticmethod
    def validate_criminal(criminal: Criminal) -> bool:
        """The function that validates the criminal, it returns false if the type is wrong. \n
            Example: criminal = "1585312648914" -> False 
            Example: Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90) -> True 
        """
        if type(criminal) != Criminal:
            return False
        elif criminal is None:
            return
        return True

    @staticmethod
    def validate_crime_type(crime_type: CRIME_TYPE) -> bool:
        """The function that validates the crime_type, it returns false if the type is wrong or if it is None. \n
            Example: crime_type = 15 -> False 
            Example: crime_type = None -> False 
            Example: crime_type = CRIME_TYPE.MURDER -> True 
        """
        if crime_type is None:
            return False
        elif type(crime_type) != CRIME_TYPE:
            return False
        return True

    @staticmethod
    def validate_region(region: REGION) -> bool:
        """The function that validates the region, it returns false if the type is wrong or if it is None. \n
            Example: region = 15 -> False 
            Example: region = None -> False 
            Example: region = REGION.BLEAK_ISLAND -> True 
        """
        if region is None:
            return False
        elif type(region) != REGION:
            return False
        return True

    @staticmethod
    def validate_seriousness(seriousness: SERIOUSNESS) -> bool:
        """The function that validates the seriousness, it returns false if the type is wrong or if it is None. \n
            Example: seriousness = 15 -> False 
            Example: seriousness = None -> False 
            Example: seriousness = SERIOUSNESS.HIGH -> True 
        """
        if seriousness is None:
            return False
        elif type(seriousness) != SERIOUSNESS:
            return False
        return True
