from src.shared.domain.entities.criminal import Criminal
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION


class Test_Criminal:
    def test_criminal(self):
        Criminal(name="VITOR", nickname="O destruidor de API",
                 description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_name_is_none(self):
        with pytest.raises(EntityError):
            Criminal(name=None, nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_name_is_not_str(self):
        with pytest.raises(EntityError):
            Criminal(name=12, nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_name_is_shorter_than_min_length(self):
        with pytest.raises(EntityError):
            Criminal(name="a", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_nickname_is_not_str(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname=12,
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_nickname_is_shorter_than_min_length(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="a",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_description_is_not_str(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description=12, gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_weight_is_none(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=None, height=1.90)

    def test_criminal_weight_is_not_float(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight="65", height=1.90)

    def test_criminal_weight_is_negative(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=-65.6, height=1.90)

    def test_criminal_height_is_none(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=None)

    def test_criminal_height_is_not_float(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=190)

    def test_criminal_height_is_negative(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=-10.1)

    def test_criminal_region_is_none(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=None, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_region_is_not_region(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=True, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_gender_is_none(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=None, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_gender_is_not_gender(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender='não é gender', region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65, height=1.90)

    def test_criminal_blood_type_is_none(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=None, age=21, weight=65, height=1.90)

    def test_criminal_blood_type_is_not_blood_type(self):
        with pytest.raises(EntityError):
            Criminal(name="VITOR", nickname="O destruidor de API",
                     description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=10, age=21, weight=65, height=1.90)
