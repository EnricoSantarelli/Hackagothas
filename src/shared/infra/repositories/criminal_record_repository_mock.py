from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord

from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.region_enum import REGION
import uuid
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository

from src.shared.helpers.errors.usecase_errors import NoItemsFound


class CriminalRecordRepositoryMock(ICriminalRecordRepository):
    """Repository responsible for request the CRUD"""

    criminals_list: List[Criminal]
    """
      List of criminals
    """

    crimes_list: List[Crime]
    """
      List of crimes
    """

    criminal_records: List[CriminalRecord]
    """
      List of criminal records
    """

    criminal_counter: int
    """
      Number of criminals in the list criminals
    """

    def __init__(self):
        """
            Criminal Record Repository Mock constructor
        """
        criminal_record_generated_id = uuid.uuid4()
        crime_generated_id = uuid.uuid4()
        self.criminals_list = [
            Criminal(name="Lonnie Machin",
                     nickname="Anarky",
                     description="Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                     gender=GENDER.MALE,
                     region=REGION.NEW_GOTHAM,
                     blood_type=BLOOD_TYPE.UNDEFINED,
                     age=16,
                     weight=75,
                     height=1.70),
            Criminal(name="Antônio Diego",
                     nickname="Bane",
                     description="Bane nasceu em 15 de Setembro de 1977, na prisão de Pietra Dura, localizada na ilha de Santa Prisca, no Caribe. Teve de cumprir a prisão perpétua, condenado pelos crimes cometidos por seu pai, o Rei Cobra. Na infância, passou a ser cuidado por um padre jesuíta, que viria a ser assassinado pelo próprio Bane, anos mais tarde. Aos oito anos de idade, cometeu seu primeiro assassinato, matando um criminoso que queria usá-lo como moeda de troca de informações na prisão. Sua única companhia era seu ursinho de pelúcia chamado Osito.",
                     gender=GENDER.MALE,
                     region=REGION.NEW_GOTHAM,
                     blood_type=BLOOD_TYPE.B_MINUS,
                     age=50,
                     weight=75.0,
                     height=1.70),
            Criminal(name="Leonard Snart",
                     nickname="Captain Cold",
                     description="Leonard Snart was raised by an abusive father and took refuge with his grandfather, who worked in an ice truck. When his grandfather died, Snart grew tired of his father's abuse and set out to start a criminal career. Snart joined up with a group of small-time thieves and in planning out a robbery, each was issued a gun and a visor to protect their eyes against the flashes of gunfire. This visor design would later be adapted by Snart into his trademark costume. In recent years he has added a radio receiver to them which picks up the police band to monitor local law enforcement. Snart and the other thugs were captured by the Flash and imprisoned.",
                     gender=GENDER.MALE,
                     region=REGION.BLEAK_ISLAND,
                     blood_type=BLOOD_TYPE.UNDEFINED,
                     age=47,
                     weight=85.6,
                     height=1.89),
            Criminal(name="Jade Nguyen's",
                     nickname="Cheshire",
                     description="Cheshire is a skilled hand-to-hand combatant, and is one of the premiere martial artists and hand-to-hand combatants in the DC Universe. She is trained in several martial arts thought forever lost. In addition, Cheshire is also an expert triple-jointed acrobat, and uses this skill to move quickly and unexpectedly, and to also augment her fighting abilities. Of bigger concern are her artificial fingernails, which she dips in several varieties of poisons. She gives her weapons and other accessories a similar treatment.",
                     gender=GENDER.FEMALE,
                     region=REGION.AMUSEMENT_MILE,
                     blood_type=BLOOD_TYPE.UNDEFINED,
                     age=36,
                     weight=70.7,
                     height=1.75),
        ]

        self.crimes_list = [
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.ARSON,
                  criminal=self.criminals_list[0],
                  date=1679951134400,
                  description="Crime committed violently against innocent people",
                  region=REGION.AMUSEMENT_MILE,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.THEFT,
                  criminal=self.criminals_list[0],
                  date=1679951629699,
                  description="Armed robbery against the elderly",
                  region=REGION.NEW_GOTHAM,
                  seriousness=SERIOUSNESS.MEDIUM),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.KIDNAPPING,
                  criminal=self.criminals_list[1],
                  date=1679951748647,
                  description="Sold marijuana and methamphetamine",
                  region=REGION.FOUNDER_ISLAND,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.DRUG_DEALING,
                  criminal=self.criminals_list[1],
                  date=1679951748647,
                  description="Kidnapping of an orphaned child",
                  region=REGION.FOUNDER_ISLAND,
                  seriousness=SERIOUSNESS.LOW),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.MURDER,
                  criminal=self.criminals_list[2],
                  date=1262304000000,
                  description="Assassination of the president's family",
                  region=REGION.NEW_GOTHAM,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.ARSON,
                  criminal=self.criminals_list[2],
                  date=946684800000,
                  description="Setting fire in 10 houses in one night, all the victims where from a organization",
                  region=REGION.OLD_GOTHAM,
                  seriousness=SERIOUSNESS.HIGH),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.DRUG_DEALING,
                  criminal=self.criminals_list[3],
                  date=1679951748647,
                  description="Seeling drugs to 16 years old in alleys close to schools, resident areas and hospitals",
                  region=REGION.NEW_GOTHAM,
                  seriousness=SERIOUSNESS.MEDIUM),
            Crime(crime_id=str(crime_generated_id),
                  crime_type=CRIME_TYPE.MURDER,
                  criminal=self.criminals_list[3],
                  date=946684800250,
                  description="Assanation of many doctors",
                  region=REGION.INDUSTRIAL_DISTRICT,
                  seriousness=SERIOUSNESS.MEDIUM),

        ]
        self.criminal_records = [
            CriminalRecord(criminal=self.criminals_list[0],
                           crime_list=[self.crimes_list[0],
                                       self.crimes_list[1]],
                           criminal_record_id=str(
                               criminal_record_generated_id),
                           danger_score=3,
                           is_arrested=False),
            CriminalRecord(criminal=self.criminals_list[1],
                           crime_list=[self.crimes_list[2],
                                       self.crimes_list[3]],
                           criminal_record_id=str(
                               criminal_record_generated_id),
                           danger_score=2,
                           is_arrested=True,
                           prison=PRISON.STATEPRISON),
            CriminalRecord(criminal_record_id=str(criminal_record_generated_id),
                           criminal=self.criminals_list[2],
                           danger_score=4,
                           is_arrested=False,
                           crime_list=[self.crimes_list[4], self.crimes_list[5]]),
            CriminalRecord(criminal=self.criminals_list[3],
                           crime_list=[self.crimes_list[6],
                                       self.crimes_list[7]],
                           criminal_record_id=str(
                               criminal_record_generated_id),
                           danger_score=3,
                           is_arrested=False),
        ]
        self.criminal_counter = 4

    def get_criminal_record(self, criminal_record_id: int) -> CriminalRecord:
        """
            Function that returns the criminal record of the passed criminal record id
        """
        for criminal_record in self.criminal_record:
            if criminal_record.criminal_record_id == criminal_record_id:
                return criminal_record
        raise NoItemsFound("user_id")

    def create_criminal_record(self, new_criminal_record: CriminalRecord) -> CriminalRecord:
        """
            Function that creates and return a new criminal record
        """
        self.criminal_records.append(new_criminal_record)
        self.criminal_records_counter += 1
        return new_criminal_record

    def delete_criminal_record(self, criminal_record_id: str) -> CriminalRecord:
        """
            Function that delete a criminal record of the list criminal_records
        """
        for idx, record in enumerate(self.criminal_records):
            if record.criminal_record_id == criminal_record_id:
                return self.criminal_records.pop(idx)

        raise NoItemsFound("user_id")

    def update_criminal_record(self, criminal_record_id: str, new_danger_score: int = None, new_criminal: Criminal = None, new_is_arrested: bool = None, new_prison: PRISON = None, new_crime_list: List[Crime] = None) -> CriminalRecord:
        """
            Function that updates and return a new criminal record of the passed criminal record id
        """      
        for criminal_record in self.criminal_records:
            if criminal_record.criminal_record_id == criminal_record_id:
                if new_danger_score is not None:
                    criminal_record.danger_score = new_danger_score
                if new_criminal is not None:
                    criminal_record.criminal_record_id = new_criminal
                if new_is_arrested is not None:
                    criminal_record.new_arrested = new_is_arrested
                if new_prison is not None:
                    criminal_record.prison = new_prison
                if new_crime_list is not None:
                    criminal_record.crime_list = new_crime_list

                return criminal_record

            return None
