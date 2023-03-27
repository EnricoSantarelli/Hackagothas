from src.shared.domain.entities.criminal import Criminal
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION


class Test_Criminal:
    def test_criminal(self):
        """The function that tests the constructor of the class Criminal, it fails if any attribute is passed wrong \n
            Example: name = 30 -> Fail 
            Example: height = "20" -> Fail 
            Example: region =  "BLOOD_TYPE.O_PLUS" -> Fail 
        """
        criminal = Criminal(name="VITOR", nickname="O destruidor de API",
                            description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

        assert criminal.name == "VITOR"
        assert criminal.nickname == "O destruidor de API"
        assert criminal.description == "Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front"
        assert criminal.gender == GENDER.UNDEFINED
        assert criminal.region == REGION.INDUSTRIAL_DISTRICT
        assert criminal.age == 21
        assert criminal.blood_type == BLOOD_TYPE.O_PLUS
        assert criminal.height == 1.90
        assert criminal.weight == 65.6

    def test_criminal_name_is_none(self):
        """The function that tests if the name is none, it fails if the name is passed none \n
            Example: name = None -> Fail 
            Example: name = "Brenas" -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name=None, nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_name_is_not_str(self):
        """The function that tests if the name is not a string, it fails if the name is passed as not a string \n
            Example: name = 14 -> Fail 
            Example: name = "Enricas" -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name=12, nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_name_is_shorter_than_min_length(self):
        """The function that tests if the name is shorter than min lenght, it fails if the name is passed shorter than min lenght \n
            Example: name = "A" -> Fail 
            Example: name = "Soller" -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="a", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_nickname_is_not_str(self):
        """The function that tests if the nickname is not a string, it fails if the nickname is passed as not a string \n
            Example: nickname = 14 -> Fail 
            Example: nickname = "Enricas" -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname=12,
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_nickname_is_shorter_than_min_length(self):
        """The function that tests if the nickname is shorter than min lenght, it fails if the nickname is passed shorter than min lenght \n
            Example: nickname = "A" -> Fail 
            Example: nickname = "Soller" -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="a",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_description_is_not_str(self):
        """The function that tests if the description is not a string, it fails if the description is passed as not a string \n
            Example: description = 14 -> Fail 
            Example: description = "Criminoso charmoso" -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description=12, gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_weight_is_none(self):
        """The function that tests if the weight is none, it fails if the weight is passed none \n
            Example: weight = None -> Fail 
            Example: weight = 72.4 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=None, height=1.90)

    def test_criminal_weight_is_not_float(self):
        """The function that tests if the weight is not a float, it fails if the weight is passed as not a float \n
            Example: weight = True -> Fail 
            Example: weight = 82.1 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight="65", height=1.90)

    def test_criminal_weight_is_negative(self):
        """The function that tests if the weight is negative, it fails if the weight is passed as negative \n
            Example: weight = -82.1 -> Fail 
            Example: weight = 82.1 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=-65.6, height=1.90)

    def test_criminal_height_is_none(self):
        """The function that tests if the height is none, it fails if the height is passed none \n
            Example: height = None -> Fail 
            Example: height = 1.82 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=None)

    def test_criminal_height_is_not_float(self):
        """The function that tests if the height is not a float, it fails if the height is passed as not a float \n
            Example: height = True -> Fail 
            Example: height = 1.30 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=190)

    def test_criminal_height_is_negative(self):
        """The function that tests if the height is negative, it fails if the height is passed as negative \n
            Example: height = -1.90 -> Fail 
            Example: height = 1.90 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=-10.1)

    def test_criminal_region_is_none(self):
        """The function that tests if the region is none, it fails if the region is passed none \n
            Example: region = None -> Fail 
            Example: region = REGION.INDUSTRIAL_DISTRICT -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=None, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_region_is_not_region(self):
        """The function that tests if the region is not region, it fails if the region is passed as not region \n
            Example: region = 30 -> Fail 
            Example: region = REGION.INDUSTRIAL_DISTRICT -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=True, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_gender_is_none(self):
        """The function that tests if the gender is none, it fails if the gender is passed none \n
            Example: gender = None -> Fail 
            Example: gender = GENDER.UNDEFINED -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=None, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_gender_is_not_gender(self):
        """The function that tests if the gender is not gender, it fails if the gender is passed as not gender \n
            Example: gender = 30 -> Fail 
            Example: gender = GENDER.UNDEFINED  -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender='não é gender', region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_blood_type_is_none(self):
        """The function that tests if the blood type is none, it fails if the blood type is passed none \n
            Example: blood_type = None -> Fail 
            Example: blood_type = BLOOD_TYPE.A_PLUS -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=None, age=21, weight=65, height=1.90)

    def test_criminal_blood_type_is_not_blood_type(self):
        """The function that tests if the blood type is not blood type, it fails if the blood type is passed as not blood type \n
            Example: blood_type = 30 -> Fail 
            Example: blood_type = BLOOD_TYPE.A_PLUS -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=10, age=21, weight=65, height=1.90)

    def test_criminal_age_is_not_int(self):
        """The function that tests if the age type is not int, it fails if the age type is passed as not int \n
            Example: age = "30" -> Fail 
            Example: age = 30 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=10, age="21", weight=65, height=1.90)

    def test_criminal_age_is_none(self):
        """The function that tests if the age type is not int, it fails if the age type is passed as not int \n
            Example: age = None -> Fail 
            Example: age = 30 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=10, age=None, weight=65, height=1.90)

    def test_criminal_age_is_negative(self):
        """The function that tests if the age is negative, it fails if the age type is passed as negative \n
            Example: age = -30 -> Fail 
            Example: age = 30 -> Pass 
        """
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=10, age=-30, weight=65, height=1.90)
