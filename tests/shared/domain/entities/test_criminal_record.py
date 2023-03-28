from typing import List
import pytest
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Criminal_Record:

    crime_list = [Crime(crime_id="c303282d-f2e6-46ca-a04a-35d3d873712d", crime_description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.", date=1585312648914, responsible_criminal=Criminal(name="VITOR", nickname="O destruidor de API", criminal_description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, criminal_region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90), crime_type=CRIME_TYPE.ARSON, crime_region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH),
                  Crime(crime_id="c303282d-f2e6-46ca-a04a-35d3d873712d", crime_description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.", date=1585312648914, responsible_criminal=Criminal(name="VITOR", nickname="O destruidor de API", criminal_description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, criminal_region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90), crime_type=CRIME_TYPE.ARSON, crime_region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH)]

    criminal = Criminal(name="VITOR", nickname="O destruidor de API", criminal_description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front",
                        gender=GENDER.UNDEFINED, criminal_region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90)

    def test_criminal_record(self):
        """The function that tests the constructor of the class Criminal Record, it fails if any attribute is passed wrong \n
           Example: id = 30 -> Fail
           Example: danger_score = "Perigoso demais" -> Fail
           Example: prison =  "BLOOD_TYPE.O_PLUS" -> Fail
       """
        criminal_record = CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d873712d", crime_list=Test_Criminal_Record.crime_list, criminal_owner=Test_Criminal_Record.criminal,
                                         danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

        assert criminal_record.criminal_owner == Test_Criminal_Record.criminal
        assert criminal_record.crime_list == Test_Criminal_Record.crime_list
        assert criminal_record.danger_score == 3
        assert criminal_record.is_arrested == True
        assert criminal_record.prison == PRISON.ARKHAMASILUM
        assert criminal_record.criminal_record_id == "c303282d-f2e6-46ca-a04a-35d3d873712d"

    def test_criminal_record_id_is_none(self):
        """The function that tests if the id is none, it fails if the id is passed none \n
            Example: id = None -> Fail
            Example: id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> Pass
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=None, crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_id_is_not_str(self):
        """The function that tests if the id is not a string, it fails if the id is passed as not a string \n
            Example: id = 14 -> Fail
            Example: id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> Pass
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=16, crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_id_size_is_different_than_the_required(self):
        """The function that tests if the id size is diferrent than the required, it fails if the id is passed shorter or longer than required lenght \n
            Example: id = "c303282d-f2e6-46ca-a04a-35d" -> Fail 
            Example: id = "c303282d-f2e6-46ca-a04a-35d532532523523512" -> Fail 
            Example: id = "c303282d-f2e6-46ca-a04a-35d3d873712d" -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d873712d432432143124124", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_criminal_is_none(self):
        """The function that tests if the criminal is none, it fails if the criminal is passed none \n
            Example: criminal = None -> Fail 
            Example: criminal = Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90) -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=None, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_criminal_is_not_criminal(self):
        """The function that tests if the criminal is not criminal, it fails if the criminal is passed as not as criminal \n
            Example: criminal = "criminoso" -> Fail 
            Example: criminal = Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90) -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner="é o criminals", danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_danger_score_is_none(self):
        """The function that tests if the danger score is none, it fails if the danger score is passed none \n
            Example: danger_score = None -> Fail
            Example: danger_score = 3 -> Pass
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=None, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_danger_score_is_not_int(self):
        """The function that tests if the danger score is not a int, it fails if the danger score is passed as not a int \n
            Example: danger_score = "2" -> Fail 
            Example: danger_score = 2 -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score="perigoso", is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_danger_score_is_out_of_range(self):
        """The function that tests if the danger score is out of range, it fails if the danger score is passed out of range \n
            Example: danger_score = -2 -> Fail 
            Example: danger_score = 10 -> Fail 
            Example: danger_score = 1 -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=-2, is_arrested=True, prison=PRISON.ARKHAMASILUM)

        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=10, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_is_arrested_not_bool(self):
        """The function that tests if the is_arrested is not a bool, it fails if the is_arrested is passed as not a bool \n
            Example: is_arrested = "true" -> Fail 
            Example: is_arrested = True -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=5, is_arrested="sim", prison=PRISON.ARKHAMASILUM)

    def test_is_arrested_is_none(self):
        """The function that tests if the is_arrested is not a bool, it fails if the is_arrested is passed as not a bool \n
            Example: is_arrested = "true" -> Fail 
            Example: is_arrested = True -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id="c303282d-f2e6-46ca-a04a-35d3d8", crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=None, is_arrested="sim", prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_prison_is_not_prison(self):
        """The function that tests if the prison is other type, it fails if the prison is passed as anything but prison enum \n
            Example: prison = "Prisão" -> Fail 
            Example: prison = PRISON.STATEPRISON -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=16, crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison="Cadeia")

    def test_criminal_record_is_not_criminal_record(self):
        """The function that tests if the prison not prison, it fails if the prison is passed as not prison \n
            Example: seriousness = "Muito sério" -> Fail 
            Example: seriousness = PRISON.STATEPRISON -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=16, crime_list=Test_Criminal_Record.crime_list,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_crime_list_is_not_crime(self):
        """The function that tests if the elements of the crime list is not crime, it fails if any element of the crime list is passed as not crime \n
            Example: crime_list = [Crime(id="c303282d-f2e6-46ca-a04a-35d3d873712d", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
              date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
              crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH, 2] -> Fail 
            Example: crime_list = [Crime(id="c303282d-f2e6-46ca-a04a-35d3d873712d", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
              date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
              crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH, Crime(id="c303282d-f2e6-46ca-a04a-35d3d873712d", description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
              date=1585312648914, criminal=Criminal(name="VITOR", nickname="O destruidor de API", description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
              crime_type=CRIME_TYPE.ARSON, region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH))] -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=16, crime_list=[Crime(crime_id="c303282d-f2e6-46ca-a04a-35d3d873712d", crime_description="The crime was extremely violent, leaving 6 citizens injured and 2 dead. The author left few clues behind.",
                                                                    date=1585312648914, responsible_criminal=Criminal(name="VITOR", nickname="O destruidor de API", criminal_description="Esse criminoso terroriza os desenvolvedores front-end derrubando a API minutos antes da entrega. Não se sabe quantas vitimas morreram do coração achando que o erro era do front", gender=GENDER.UNDEFINED, criminal_region=REGION.INDUSTRIAL_DISTRICT, blood_type=BLOOD_TYPE.O_PLUS, age=21, weight=65.6, height=1.90),
                                                                    crime_type=CRIME_TYPE.ARSON, crime_region=REGION.AMUSEMENT_MILE, seriousness=SERIOUSNESS.HIGH), 2],
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_crime_list_is_none(self):
        """The function that tests if the crime_list is none, it fails if the crime_list is passed none \n
            Example: crime_list = None -> Fail 
            Example: crime_list = List[Crime] -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=16, crime_list=None,
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)

    def test_criminal_record_crime_list_is_empty(self):
        """The function that tests if the crime_list is empty, it fails if the crime_list is passed empty \n
            Example: crime_list = List[] -> Fail 
            Example: crime_list = List[Crime] -> Pass 
        """
        with pytest.raises(EntityError):
            CriminalRecord(criminal_record_id=16, crime_list=[],
                           criminal_owner=Test_Criminal_Record.criminal, danger_score=3, is_arrested=True, prison=PRISON.ARKHAMASILUM)
