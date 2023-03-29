from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord

from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository

from src.shared.helpers.errors.usecase_errors import NoItemsFound


class CriminalRecordRepositoryMock(ICriminalRecordRepository):
    """Repository responsible for request the CRUD"""

    criminal_list: list[Criminal]
    """
      List of criminals
    """

    crime_list: list[Crime]
    """
      List of crimes
    """

    criminal_record_list: list[CriminalRecord]
    """
      List of criminal records
    """

    criminal_records_counter: int
    """
      Number of criminals in the list criminals
    """

    def __init__(self):
        """
            Criminal Record Repository Mock constructor
        """
        self.criminal_list = [
            Criminal(name="Lonnie Machin",
                     nickname="Anarky",
                     criminal_description="Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                     gender=GENDER.MALE,
                     criminal_region=REGION.NEW_GOTHAM,
                     blood_type=BLOOD_TYPE.UNDEFINED,
                     age=16,
                     weight=75.2,
                     height=1.70),
            Criminal(name="Antônio Diego",
                     nickname="Bane",
                     criminal_description="Bane nasceu em 15 de Setembro de 1977, na prisão de Pietra Dura, localizada na ilha de Santa Prisca, no Caribe. Teve de cumprir a prisão perpétua, condenado pelos crimes cometidos por seu pai, o Rei Cobra. Na infância, passou a ser cuidado por um padre jesuíta, que viria a ser assassinado pelo próprio Bane, anos mais tarde. Aos oito anos de idade, cometeu seu primeiro assassinato, matando um criminoso que queria usá-lo como moeda de troca de informações na prisão. Sua única companhia era seu ursinho de pelúcia chamado Osito.",
                     gender=GENDER.MALE,
                     criminal_region=REGION.NEW_GOTHAM,
                     blood_type=BLOOD_TYPE.B_MINUS,
                     age=50,
                     weight=75.0,
                     height=1.70),
            Criminal(name="Leonard Snart",
                     nickname="Captain Cold",
                     criminal_description="Leonard Snart was raised by an abusive father and took refuge with his grandfather, who worked in an ice truck. When his grandfather died, Snart grew tired of his father's abuse and set out to start a criminal career. Snart joined up with a group of small-time thieves and in planning out a robbery, each was issued a gun and a visor to protect their eyes against the flashes of gunfire. This visor design would later be adapted by Snart into his trademark costume. In recent years he has added a radio receiver to them which picks up the police band to monitor local law enforcement. Snart and the other thugs were captured by the Flash and imprisoned.",
                     gender=GENDER.MALE,
                     criminal_region=REGION.BLEAK_ISLAND,
                     blood_type=BLOOD_TYPE.UNDEFINED,
                     age=47,
                     weight=85.6,
                     height=1.89),
            Criminal(name="Jade Nguyen's",
                     nickname="Cheshire",
                     criminal_description="Cheshire is a skilled hand-to-hand combatant, and is one of the premiere martial artists and hand-to-hand combatants in the DC Universe. She is trained in several martial arts thought forever lost. In addition, Cheshire is also an expert triple-jointed acrobat, and uses this skill to move quickly and unexpectedly, and to also augment her fighting abilities. Of bigger concern are her artificial fingernails, which she dips in several varieties of poisons. She gives her weapons and other accessories a similar treatment.",
                     gender=GENDER.FEMALE,
                     criminal_region=REGION.AMUSEMENT_MILE,
                     blood_type=BLOOD_TYPE.UNDEFINED,
                     age=36,
                     weight=70.7,
                     height=1.75),
        ]

        self.crime_list = [
            Crime(crime_id="d9af6081-74f9-478d-9599-d2b21a06b386",
                  crime_type=CRIME_TYPE.ARSON,
                  responsible_criminal=self.criminal_list[0],
                  date=1648755588000,
                  crime_description="Crime committed violently against innocent people",
                  crime_region=REGION.AMUSEMENT_MILE,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id="9130a793-ad89-4171-adf2-c33575a4c066",
                  crime_type=CRIME_TYPE.THEFT,
                  responsible_criminal=self.criminal_list[0],
                  date=1648755588000,
                  crime_description="Armed robbery against the elderly",
                  crime_region=REGION.NEW_GOTHAM,
                  seriousness=SERIOUSNESS.MEDIUM),
            Crime(crime_id="d7bf024d-bd24-4fd4-be7e-f6ea1107d8c4",
                  crime_type=CRIME_TYPE.KIDNAPPING,
                  responsible_criminal=self.criminal_list[1],
                  date=1648755588000,
                  crime_description="Sold marijuana and methamphetamine",
                  crime_region=REGION.FOUNDER_ISLAND,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id="01302785-e445-48ab-8eaf-ed95d4d0f0ed",
                  crime_type=CRIME_TYPE.DRUG_DEALING,
                  responsible_criminal=self.criminal_list[1],
                  date=1648755588000,
                  crime_description="Kidnapping of an orphaned child",
                  crime_region=REGION.FOUNDER_ISLAND,
                  seriousness=SERIOUSNESS.LOW),
            Crime(crime_id="5e4667f7-b0bc-4e0a-b8b7-1386f2b4608d",
                  crime_type=CRIME_TYPE.MURDER,
                  responsible_criminal=self.criminal_list[2],
                  date=1648755588000,
                  crime_description="Assassination of the president's family",
                  crime_region=REGION.NEW_GOTHAM,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id="ab8cb62e-aca9-4f79-ad82-b77180e53498",
                  crime_type=CRIME_TYPE.ARSON,
                  responsible_criminal=self.criminal_list[2],
                  date=1648755588000,
                  crime_description="Setting fire in 10 houses in one night, all the victims where from a organization",
                  crime_region=REGION.OLD_GOTHAM,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id="79fc6ada-a004-449f-b745-d015caeac6ca",
                  crime_type=CRIME_TYPE.DRUG_DEALING,
                  responsible_criminal=self.criminal_list[3],
                  date=1648755588000,
                  crime_description="Seeling drugs to 16 years old in alleys close to schools, resident areas and hospitals",
                  crime_region=REGION.NEW_GOTHAM,
                  seriousness=SERIOUSNESS.MEDIUM),
            Crime(crime_id="e871717e-b9cf-4f2b-8be0-9e6221cc59dc",
                  crime_type=CRIME_TYPE.MURDER,
                  responsible_criminal=self.criminal_list[3],
                  date=1648755588000,
                  crime_description="Assanation of many doctors",
                  crime_region=REGION.INDUSTRIAL_DISTRICT,
                  seriousness=SERIOUSNESS.MEDIUM),

        ]
        self.criminal_record_list = [
            CriminalRecord(criminal_owner=self.criminal_list[0],
                           crime_list=[self.crime_list[0],
                                       self.crime_list[1]],
                           criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc",
                           danger_score=3,
                           is_arrested=False),
            CriminalRecord(criminal_owner=self.criminal_list[1],
                           crime_list=[self.crime_list[2],
                                       self.crime_list[3]],
                           criminal_record_id="7f2365f2-193c-41a8-a336-52b18069bf47",
                           danger_score=2,
                           is_arrested=True,
                           prison=PRISON.STATEPRISON),
            CriminalRecord(criminal_record_id="c5fe225f-3437-4906-b0ed-e58d69cb9737",
                           criminal_owner=self.criminal_list[2],
                           danger_score=4,
                           is_arrested=False,
                           crime_list=[self.crime_list[4], self.crime_list[5]]),
            CriminalRecord(criminal_owner=self.criminal_list[3],
                           crime_list=[self.crime_list[6],
                                       self.crime_list[7]],
                           criminal_record_id="eb24786c-72fe-49d4-9d51-83d985c5c68a",
                           danger_score=3,
                           is_arrested=False),
        ]

    def get_criminal_record(self, criminal_record_id: int) -> CriminalRecord:
        """
            Function that returns the criminal record of the passed criminal record id
        """
        for criminal_record in self.criminal_record_list:
            if criminal_record.criminal_record_id == criminal_record_id:
                return criminal_record
        raise NoItemsFound("criminal_record_id")

    def create_criminal_record(self, new_criminal_record: CriminalRecord) -> CriminalRecord:
        """
            Function that creates and return a new criminal record
        """
        self.criminal_record_list.append(new_criminal_record)
        return new_criminal_record

    def delete_criminal_record(self, criminal_record_id: str) -> CriminalRecord:
        """
            Function that delete a criminal record of the list criminal_records
        """
        for index, record in enumerate(self.criminal_record_list):
            if record.criminal_record_id == criminal_record_id:
                return self.criminal_record_list.pop(index)

        raise NoItemsFound("criminal_record_id")

    def update_criminal_record(self, criminal_record_id: str, new_danger_score: int = None, new_criminal_owner: Criminal = None, new_is_arrested: bool = None, new_prison: PRISON = None, new_crime_list: List[Crime] = None) -> CriminalRecord:
        """
            Function that updates and return a new criminal record of the passed criminal record id
        """
        for criminal_record in self.criminal_record_list:
            if criminal_record.criminal_record_id == criminal_record_id:
                if new_danger_score is not None:
                    criminal_record.danger_score = new_danger_score
                if new_criminal_owner is not None:
                    criminal_record.criminal_owner = new_criminal_owner
                if new_is_arrested is not None:
                    criminal_record.is_arrested = new_is_arrested
                if new_prison is not None:
                    criminal_record.prison = new_prison
                if new_crime_list is not None:
                    criminal_record.crime_list = new_crime_list

                return criminal_record

            return None
