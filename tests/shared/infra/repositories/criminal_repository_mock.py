from typing import List
from src.shared.domain.entities.criminal import Criminal

from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UserRepositoryMock():
    criminal: List[Criminal]
    criminal_counter: int

    def __init__(self):
        self.users = [
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
            Criminal(name = "Antônio Diego", nickname = "Bane", description = "Bane nasceu em 15 de Setembro de 1977, na prisão de Pietra Dura, localizada na ilha de Santa Prisca, no Caribe. Teve de cumprir a prisão perpétua, condenado pelos crimes cometidos por seu pai, o Rei Cobra. Na infância, passou a ser cuidado por um padre jesuíta, que viria a ser assassinado pelo próprio Bane, anos mais tarde. Aos oito anos de idade, cometeu seu primeiro assassinato, matando um criminoso que queria usá-lo como moeda de troca de informações na prisão. Sua única companhia era seu ursinho de pelúcia chamado Osito.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.B_MINUS, age= 50, weight= 75.0, height= 1.70),
            Criminal(name = "Leonard Snart", nickname = "Captain Cold", description = "Leonard Snart was raised by an abusive father and took refuge with his grandfather, who worked in an ice truck. When his grandfather died, Snart grew tired of his father's abuse and set out to start a criminal career. Snart joined up with a group of small-time thieves and in planning out a robbery, each was issued a gun and a visor to protect their eyes against the flashes of gunfire. This visor design would later be adapted by Snart into his trademark costume. In recent years he has added a radio receiver to them which picks up the police band to monitor local law enforcement. Snart and the other thugs were captured by the Flash and imprisoned.", gender = GENDER.MALE, region= REGION.BLEAK_ISLAND, blood_type= BLOOD_TYPE.UNDEFINED, age= 47, weight= 85.6, height= 1.89),
            Criminal(name = "Jade Nguyen's", nickname = "Cheshire", description = "Cheshire is a skilled hand-to-hand combatant, and is one of the premiere martial artists and hand-to-hand combatants in the DC Universe. She is trained in several martial arts thought forever lost. In addition, Cheshire is also an expert triple-jointed acrobat, and uses this skill to move quickly and unexpectedly, and to also augment her fighting abilities. Of bigger concern are her artificial fingernails, which she dips in several varieties of poisons. She gives her weapons and other accessories a similar treatment.", gender = GENDER.FEMALE, region= REGION.AMUSEMENT_MILE, blood_type= BLOOD_TYPE.UNDEFINED, age= 36, weight= 70.7, height= 1.75),
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
            Criminal(name = "Lonnie Machin", nickname = "Anarky", description = "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.", gender = GENDER.MALE, region= REGION.NEW_GOTHAM, blood_type= BLOOD_TYPE.UNDEFINED, age= 16, weight= 75, height= 1.70),
                    ]
        self.user_counter = 3

    # def get_user(self, user_id: int) -> User:
    #     for user in self.users:
    #         if user.user_id == user_id:
    #             return user
    #     raise NoItemsFound("user_id")

    # def get_all_user(self) -> List[User]:
    #     return self.users

    # def create_user(self, new_user: User) -> User:
    #     self.users.append(new_user)
    #     self.user_counter += 1
    #     return new_user

    # def delete_user(self, user_id: int) -> User:
    #     for idx, user in enumerate(self.users):
    #         if user.user_id == user_id:
    #             return self.users.pop(idx)

    #     raise NoItemsFound("user_id")

    # def update_user(self, user_id: int, new_name: str) -> User:
    #     for user in self.users:
    #         if user.user_id == user_id:
    #             user.name = new_name
    #             return user

    #     raise NoItemsFound("user_id")

    # def get_user_counter(self) -> int:
    #     return self.user_counter