import abc
import dataclasses

from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION

from src.shared.helpers.errors.domain_errors import EntityError


class Criminal(abc.ABC):
    """Entity responsible for characterize a criminal"""

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

    criminal_region: REGION
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

    MIN_NAME_LENGTH = 2
    """The minimum string lenght is equal to 2. \n"""

    def __init__(self, name: str, gender: GENDER, criminal_region: REGION, blood_type: BLOOD_TYPE, age: int, weight: float, height: float, nickname: str = None, criminal_description: str = None):
        """Criminal class constructor"""

        # validation if the name is valid using the function validade_name. It raises a entity error if returns false
        if not Criminal.validate_name(name):
            raise EntityError("name")
        self.name = name

        # validation if the description is valid using the function validade_description. It raises a entity error if returns false
        if not Criminal.validate_criminal_description(criminal_description):
            raise EntityError("criminal_description")
        self.criminal_description = criminal_description

        # validation if the nickname is valid using the function validade_nickname. It raises a entity error if returns false
        if not Criminal.validate_nickname(nickname):
            raise EntityError("nickname")
        self.nickname = nickname

        # validation if the weight is valid using the function validade_weight. It raises a entity error if returns false
        if not Criminal.validate_weight(weight):
            raise EntityError("weight")
        self.weight = weight

        # validation if the height is valid using the function validade_height. It raises a entity error if returns false
        if not Criminal.validate_height(height):
            raise EntityError("height")
        self.height = height

        # validation if the region is valid using the function validade_region. It raises a entity error if returns false
        if not Criminal.validate_criminal_region(criminal_region):
            raise EntityError("criminal_region")
        self.criminal_region = criminal_region

        # validation if the gender is valid using the function validade_gender. It raises a entity error if returns false
        if not Criminal.validate_gender(gender):
            raise EntityError("gender")
        self.gender = gender

        # validation if the blood_type is valid using the function validade_blood_type. It raises a entity error if returns false
        if not Criminal.validate_blood_type(blood_type):
            raise EntityError("blood_type")
        self.blood_type = blood_type

        # validation if the age is valid using the function validade_age. It raises a entity error if returns false
        if not Criminal.validate_age(age):
            raise EntityError("age")
        self.age = age

    @staticmethod
    def validate_name(name: str) -> bool:
        """The function that validates the name, it returns false if the name is none, the type is wrong or if its too small. \n
            Example: name = 2.3 -> False 
            Example: name = None -> False 
            Example: name = "b" -> False
            Example: name = "Gabriel Godoy" -> True 
        """
        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) < Criminal.MIN_NAME_LENGTH:
            return False
        return True

    @staticmethod
    def validate_nickname(nickname: str) -> bool:
        """The function that validates the nickname, it returns false if the type is wrong or if it is too small. \n
            Example: nickname = 30 -> False 
            Example: nickname = "a" -> False 
            Example: nickname = "Joker" -> True 
        """
        if type(nickname) != str:
            return False
        elif len(nickname) < Criminal.MIN_NAME_LENGTH:
            return False
        return True

    @staticmethod
    def validate_criminal_description(criminal_description: str) -> bool:
        """The function that validates the description, it returns false if the type is wrong. \n
            Example: decription = 30 -> False 
            Example: decription = "This guys is pika" -> True 
        """
        if type(criminal_description) != str:
            return False
        return True

    @staticmethod
    def validate_weight(weight: float) -> bool:
        """The function that validates the weight, it returns false if the weight is none, the type is wrong or if its negative. \n
            Example: weight = -15 -> False 
            Example: weight = None -> False 
            Example: weight = 10 -> True 
        """
        if weight is None:
            return False
        elif type(weight) != float:
            return False
        elif weight < 0:
            return False
        return True

    @staticmethod
    def validate_height(height: float) -> bool:
        """The function that validates the height, it returns false if the height is none, the type is wrong or if its negative. \n
            Example: height = -15 -> False 
            Example: height = None -> False 
            Example: height = 80 -> True 
        """
        if height is None:
            return False
        elif type(height) != float:
            return False
        elif height < 0:
            return False
        return True

    @staticmethod
    def validate_criminal_region(criminal_region: REGION) -> bool:
        """The function that validates the region, it returns false if the type is wrong or if it is None. \n
            Example: region = 15 -> False 
            Example: region = None -> False 
            Example: region = "MC Pipokinha" -> False 
            Example: region = REGION.BLEAK_ISLAND -> True 
        """
        if criminal_region is None:
            return False
        elif type(criminal_region) != REGION:
            return False
        return True

    @staticmethod
    def validate_gender(gender: GENDER) -> bool:
        """The function that validates the gender, it returns false if the gender is none or the type is wrong. \n
            Example: gender = 19 -> False 
            Example: gender = None -> False 
            Example: gender = GENDER.Male -> True 
        """
        if gender is None:
            return False
        elif type(gender) != GENDER:
            return False
        return True

    @staticmethod
    def validate_blood_type(blood_type: BLOOD_TYPE) -> bool:
        """The function that validates the blood_type, it returns false if the type is wrong or if it is None. \n
            Example: blood_type = 15 -> False 
            Example: blood_type = None -> False 
            Example: blood_type = "MC Guimé" -> False 
            Example: blood_type = BLOOD_TYPE.A_PLUS -> True 
        """
        if blood_type is None:
            return False
        elif type(blood_type) != BLOOD_TYPE:
            return False
        return True

    def validate_age(age: int) -> bool:
        """The function that validates the age, it returns false if the age is none or the type is wrong. \n
            Example: age = "19" -> False 
            Example: age = None -> False 
            Example: age = 19 -> True 
        """
        if age is None:
            return False
        elif type(age) != int:
            return False
        elif age < 0:
            return False
        return True
