import pytest
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Crime:
    criminal = Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front",
                        gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_crime(self):
        """The function that tests the constructor of the class Crime, it fails if any attribute is passed wrong \n
            Example: id = 30 -> Fail
            Example: crime_type = "Assalto" -> Fail
            Example: region =  "BLOOD_TYPE.O_PLUS" -> Fail
        """
        crime = Crime(id="c303282d-f2e6-46ca-a04a-35d3d873712d", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                      date=1585312648914, criminal=Test_Crime.criminal, crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

        assert crime.crime_id == "c303282d-f2e6-46ca-a04a-35d3d873712d"
        assert crime.description == "The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind."
        assert crime.date == 1585312648914
        assert crime.criminal == Test_Crime.criminal
        assert crime.crime_type == CRIME_TYPE.ARSON
        assert crime.region == REGION.AMUSEMENT_MILE
        assert crime.seriousness == SERIOUSNESS.HIGH

    def test_crime_id_is_none(self):
        """The function that tests if the id is none, it fails if the id is passed none \n
            Example: id = None -> Fail
            Example: id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> Pass
        """
        with pytest.raises(EntityError):
            Crime(id=None, description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_id_is_not_str(self):
        """The function that tests if the id is not a string, it fails if the id is passed as not a string \n
            Example: id = 14 -> Fail
            Example: id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> Pass
        """
        with pytest.raises(EntityError):
            Crime(id=15, description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_id_size_is_different_than_the_required(self):
        """The function that tests if the id size is diferrent than the required, it fails if the id is passed shorter or longer than required lenght \n
            Example: id = "c303282d-f2e6-46ca-a04a-35d" -> Fail 
            Example: id = "c303282d-f2e6-46ca-a04a-35d532532523523512" -> Fail 
            Example: id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_description_is_not_str(self):
        """The function that tests if the description is not a string, it fails if the description is passed as not a string \n
            Example: description = 14 -> Fail 
            Example: description = "The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind." -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_date_is_none(self):
        """The function that tests if the date is none, it fails if the date is passed none \n
            Example: date = None -> Fail
            Example: date = 1585312648914 -> Pass
        """
        with pytest.raises(EntityError):
            Crime(id=None, description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=None, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_date_is_not_int(self):
        """The function that tests if the date is not a int, it fails if the date is passed as not a int \n
            Example: date = "15214124214" -> Fail 
            Example: date = 1585312648914 -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date="1585312648914", criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_date_is_out_of_range(self):
        """The function that tests if the date is out of range, it fails if the date is passed out of range \n
            Example: date = 41242145153253252353253221321 -> Fail 
            Example: date = 1232131 -> Fail 
            Example: date = 1585312648914 -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date=41242145153253252353253221321, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date=1232131, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_criminal_is_none(self):
        """The function that tests if the criminal is none, it fails if the criminal is passed none \n
            Example: criminal = None -> Fail 
            Example: criminal = Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90) -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15, date=41242145153253252353253221321,
                  criminal=None, crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_criminal_is_not_criminal(self):
        """The function that tests if the criminal is not criminal, it fails if the criminal is passed as not as criminal \n
            Example: criminal = "criminoso" -> Fail 
            Example: criminal = Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90) -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15, date=41242145153253252353253221321,
                  criminal=145, crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_crime_type_is_none(self):
        """The function that tests if the crime type is none, it fails if the crime type is passed none \n
            Example: crime_type = None -> Fail 
            Example: crime_type = CRIME_TYPE.ARSON -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id=None, description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=None, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_crime_type_is_not_crime_type(self):
        """The function that tests if the crime type is not crime type, it fails if the crime type is passed as not crime type \n
            Example: crime_type = 30 -> Fail 
            Example: crime_type = CRIME_TYPE.ARSON -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date=1232131, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=30, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)

    def test_crime_region_is_none(self):
        """The function that tests if the region is none, it fails if the region is passed none \n
            Example: region = None -> Fail 
            Example: region = REGION.INDUSTRIAL_DISTRICT -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id=None, description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=None, region=None, seriousness=SERIOUSNESS.HIGH)

    def test_crime_region_is_not_region(self):
        """The function that tests if the region not region, it fails if the region is passed as not region \n
            Example: region = "Lagoa" -> Fail 
            Example: region = REGION.INDUSTRIAL_DISTRICT -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date=1232131, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=30, region="São Caetano do Sul", seriousness=SERIOUSNESS.HIGH)

    def test_crime_seriousness_is_none(self):
        """The function that tests if the seriousness is none, it fails if the seriousness is passed none \n
            Example: seriousness = None -> Fail 
            Example: seriousness = SERIOUSNESS.HIGH -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id=None, description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                  date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=None, region=None, seriousness=None)

    def test_crime_seriousness_is_not_seriousness(self):
        """The function that tests if the seriousness not seriousness, it fails if the seriousness is passed as not seriousness \n
            Example: seriousness = "Muito sério" -> Fail 
            Example: seriousness = SERIOUSNESS.HIGH -> Pass 
        """
        with pytest.raises(EntityError):
            Crime(id="c303282d-f2e6-46ca-a04a-35d532532523523512", description=15,
                  date=1232131, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                  crime_type=30, region="São Caetano do Sul", seriousness=50)
