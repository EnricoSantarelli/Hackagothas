import abc
from typing import List

from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.helpers.errors.domain_errors import EntityError


class CriminalRecord(abc.ABC):
    """Entity responsible for characterize a criminal record"""

    criminal_record_id: str
    """The unique id of the criminal record. \n
            Example: c303282d-f2e6-46ca-a04a-35d3d873712d 
    """

    danger_score: int
    """The danger score of the criminal with this criminal record. It varies between 1 to 5 as 5 being the most dangerous. \n
            Example: 4. 
    """

    criminal: Criminal
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

    crime_list: list[Crime]
    """The list of crimes the criminal commited. 
        Example: [Crime(id="c303282d-f2e6-46ca-a04a-35d3d873712d", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
              date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
              crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH, Crime(id="c303282d-f2e6-46ca-a04a-35d3d873712d", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
              date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
              crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH))]
    """

    MIN_DANGER_SCORE = 1
    """The minimun value the danger score can be. \n"""

    MAX_DANGER_SCORE = 5
    """The maximum value the danger score can be. \n"""

    ID_LENGTH = 36

    def __init__(self, criminal: Criminal, criminal_record_id: str, danger_score: int, is_arrested: bool,  crime_list: list[Crime], prison: PRISON = None):
        """Criminal Record class constructor"""

        # validation if the criminal is valid using the function validade_criminal. It raises a entity error if returns false
        if not CriminalRecord.validate_criminal(criminal):
            raise EntityError("criminal")
        self.criminal = criminal

        # validation if the isArrested is valid using the function validade_isArrested. It raises a entity error if returns false
        if not CriminalRecord.validate_is_arrested(is_arrested):
            raise EntityError("is_arrested")
        self.is_arrested = is_arrested

        # validation if the prison is valid using the function validade_prison. It raises a entity error if returns false
        if not CriminalRecord.validate_prison(prison):
            raise EntityError("prison")
        self.prison = prison

        # validation if the criminal_record_id is valid using the function validade_criminal_record_id. It raises a entity error if returns false
        if not CriminalRecord.validate_criminal_record_id(criminal_record_id):
            raise EntityError("criminal_record_id")
        self.criminal_record_id = criminal_record_id

        # validation if the prison is valid using the function validade_crime_list. It raises a entity error if returns false
        if not CriminalRecord.validate_crime_list(crime_list):
            raise EntityError("crime_list")
        self.crime_list = crime_list

        # validation if the prison is valid using the function validade_danger_score It raises a entity error if returns false
        if not CriminalRecord.validate_danger_score(danger_score):
            raise EntityError("danger_score")
        self.danger_score = danger_score

    @staticmethod
    def validate_criminal_record_id(criminal_record_id: str) -> bool:
        """The function that validates the id, it returns false if the id is none, the type is wrong or if its diferent of the necessary size. \n
            Example: criminal_record_i = 2.3 -> False 
            Example: criminal_record_i = None -> False 
            Example: criminal_record_i = "c303282d-f2e6-46ca-a04a-35d3" -> False
            Example: criminal_record_i = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> True 
        """
        if criminal_record_id is None:
            return False
        elif type(criminal_record_id) != str:
            return False
        elif len(criminal_record_id) != CriminalRecord.ID_LENGTH:
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
        return True

    @staticmethod
    def validate_danger_score(danger_score: int) -> bool:
        """The function that validates the danger score, it returns false if the danger score is wrong, if the danger score is none or if its not betwenn is not in the range of 1 to 5. \n
            Example: danger score = "1585312648914" -> False 
            Example: danger score = 0 -> False 
            Example: danger score = 6 -> False 
            Example: danger score = 5-> True 
        """
        if danger_score is None:
            return False
        elif type(danger_score) != int:
            return False
        elif not CriminalRecord.MIN_DANGER_SCORE <= danger_score <= CriminalRecord.MAX_DANGER_SCORE:
            return False
        return True

    @staticmethod
    def validate_prison(prison: PRISON) -> bool:
        """The function that validates the prison, it returns false if the type is wrong or if it is None. \n
            Example: prison = 15 -> False 
            Example: prison = None -> False 
            Example: prison = PRISON.BLACKGATE -> True 
        """
        if type(prison) != PRISON and prison != None:
            return False
        return True

    @staticmethod
    def validate_is_arrested(is_arrested: bool) -> bool:
        """The function that validates the isArrested, it returns false if the type is wrong or if it is None. \n
            Example: isArrested = 15 -> False 
            Example: isArrested = None -> False 
            Example: isArrested = False -> True 
        """
        if is_arrested is None:
            return False
        elif type(is_arrested) != bool:
            return False
        return True

    @staticmethod
    def validate_crime_list(crime_list: List[Crime]) -> bool:
        """The function that validates the crime_list, it returns false if the type is wrong, if it is None or the list is Empty. \n
            Example: crime_list = 15 -> False 
            Example: crime_list = None -> False 
            Example: crime_list = "" -> False 
            Example: crime_list = False -> True 
        """
        if crime_list is None:
            return False
        elif not all([type(crime) == Crime for crime in crime_list]):
            return False
        elif crime_list == []:
            return False
        return True
