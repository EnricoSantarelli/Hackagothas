from src.modules.get_all_criminal_records.app.get_all_criminal_records_viewmodel import GetAllCriminalRecordsViewmodel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetAllCriminalRecordsViewmodel:

    def test_get_all_criminal_records_viewmodel(self):
        """
            The function that tests if the criminal record view model translation is the same as the expected 
        """
        repo = CriminalRecordRepositoryMock()
        criminal_records_list = repo.criminal_record_list
        criminal_record_viewmodel = GetAllCriminalRecordsViewmodel(
            criminal_records_list=criminal_records_list).to_dict()

        expected_criminal_record_json = {
            'criminal_records': [
                {
                    'criminal_record_id': '4d108071-6d0f-48cb-8675-5d38049c3ecc',
                    'crime_list': [
                        {
                            'crime_id': 'd9af6081-74f9-478d-9599-d2b21a06b386',
                            'crime_type': 'ARSON',
                            'responsible_criminal': {
                                'name': 'Lonnie Machin',
                                'nickname': 'Anarky',
                                'age': 16,
                                'blood_type': 'UNDEFINED',
                                'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                                'gender': 'MALE',
                                'height': 1.7,
                                'weight': 75.2,
                                'criminal_region': 'NEW_GOTHAM'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Crime committed violently against innocent people',
                            'crime_region': 'AMUSEMENT_MILE',
                            'seriousness': 'HIGH'
                        },
                        {
                            'crime_id': '9130a793-ad89-4171-adf2-c33575a4c066',
                            'crime_type': 'THEFT',
                            'responsible_criminal': {
                                'name': 'Lonnie Machin',
                                'nickname': 'Anarky',
                                'age': 16,
                                'blood_type': 'UNDEFINED',
                                'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                                'gender': 'MALE',
                                'height': 1.7,
                                'weight': 75.2,
                                'criminal_region': 'NEW_GOTHAM'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Armed robbery against the elderly',
                            'crime_region': 'NEW_GOTHAM',
                            'seriousness': 'MEDIUM'
                        }
                    ],
                    'criminal_owner': {
                        'name': 'Lonnie Machin',
                        'nickname': 'Anarky',
                        'age': 16,
                        'blood_type': 'UNDEFINED',
                        'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                        'gender': 'MALE',
                        'height': 1.7,
                        'weight': 75.2,
                        'criminal_region': 'NEW_GOTHAM'
                    },
                    'danger_score': 3,
                    'is_arrested': False,
                    'prison': None
                },
                {
                    'criminal_record_id': '7f2365f2-193c-41a8-a336-52b18069bf47',
                    'crime_list': [
                        {
                            'crime_id': 'd7bf024d-bd24-4fd4-be7e-f6ea1107d8c4',
                            'crime_type': 'KIDNAPPING',
                            'responsible_criminal': {
                                'name': 'Antônio Diego',
                                'nickname': 'Bane',
                                'age': 50,
                                'blood_type': 'B_MINUS',
                                'criminal_description': 'Bane nasceu em 15 de Setembro de 1977, na prisão de Pietra Dura, localizada na ilha de Santa Prisca, no Caribe. Teve de cumprir a prisão perpétua, condenado pelos crimes cometidos por seu pai, o Rei Cobra. Na infância, passou a ser cuidado por um padre jesuíta, que viria a ser assassinado pelo próprio Bane, anos mais tarde. Aos oito anos de idade, cometeu seu primeiro assassinato, matando um criminoso que queria usá-lo como moeda de troca de informações na prisão. Sua única companhia era seu ursinho de pelúcia chamado Osito.',
                                'gender': 'MALE',
                                'height': 1.7,
                                'weight': 75.0,
                                'criminal_region': 'NEW_GOTHAM'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Sold marijuana and methamphetamine',
                            'crime_region': 'FOUNDER_ISLAND',
                            'seriousness': 'HIGH'
                        },
                        {
                            'crime_id': '01302785-e445-48ab-8eaf-ed95d4d0f0ed',
                            'crime_type': 'DRUG_DEALING',
                            'responsible_criminal': {
                                'name': 'Antônio Diego',
                                'nickname': 'Bane',
                                'age': 50,
                                'blood_type': 'B_MINUS',
                                'criminal_description': 'Bane nasceu em 15 de Setembro de 1977, na prisão de Pietra Dura, localizada na ilha de Santa Prisca, no Caribe. Teve de cumprir a prisão perpétua, condenado pelos crimes cometidos por seu pai, o Rei Cobra. Na infância, passou a ser cuidado por um padre jesuíta, que viria a ser assassinado pelo próprio Bane, anos mais tarde. Aos oito anos de idade, cometeu seu primeiro assassinato, matando um criminoso que queria usá-lo como moeda de troca de informações na prisão. Sua única companhia era seu ursinho de pelúcia chamado Osito.',
                                'gender': 'MALE',
                                'height': 1.7,
                                'weight': 75.0,
                                'criminal_region': 'NEW_GOTHAM'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Kidnapping of an orphaned child',
                            'crime_region': 'FOUNDER_ISLAND',
                            'seriousness': 'LOW'
                        }
                    ],
                    'criminal_owner': {
                        'name': 'Antônio Diego',
                        'nickname': 'Bane',
                        'age': 50,
                        'blood_type': 'B_MINUS',
                        'criminal_description': 'Bane nasceu em 15 de Setembro de 1977, na prisão de Pietra Dura, localizada na ilha de Santa Prisca, no Caribe. Teve de cumprir a prisão perpétua, condenado pelos crimes cometidos por seu pai, o Rei Cobra. Na infância, passou a ser cuidado por um padre jesuíta, que viria a ser assassinado pelo próprio Bane, anos mais tarde. Aos oito anos de idade, cometeu seu primeiro assassinato, matando um criminoso que queria usá-lo como moeda de troca de informações na prisão. Sua única companhia era seu ursinho de pelúcia chamado Osito.',
                        'gender': 'MALE',
                        'height': 1.7,
                        'weight': 75.0,
                        'criminal_region': 'NEW_GOTHAM'
                    },
                    'danger_score': 2,
                    'is_arrested': True,
                    'prison': 'STATEPRISON'
                },
                {
                    'criminal_record_id': 'c5fe225f-3437-4906-b0ed-e58d69cb9737',
                    'crime_list': [
                        {
                            'crime_id': '5e4667f7-b0bc-4e0a-b8b7-1386f2b4608d',
                            'crime_type': 'MURDER',
                            'responsible_criminal': {
                                'name': 'Leonard Snart',
                                'nickname': 'Captain Cold',
                                'age': 47,
                                'blood_type': 'UNDEFINED',
                                'criminal_description': "Leonard Snart was raised by an abusive father and took refuge with his grandfather, who worked in an ice truck. When his grandfather died, Snart grew tired of his father's abuse and set out to start a criminal career. Snart joined up with a group of small-time thieves and in planning out a robbery, each was issued a gun and a visor to protect their eyes against the flashes of gunfire. This visor design would later be adapted by Snart into his trademark costume. In recent years he has added a radio receiver to them which picks up the police band to monitor local law enforcement. Snart and the other thugs were captured by the Flash and imprisoned.",
                                'gender': 'MALE',
                                'height': 1.89,
                                'weight': 85.6,
                                'criminal_region': 'BLEAK_ISLAND'
                            },
                            'date': 1648755588000,
                            'crime_description': "Assassination of the president's family",
                            'crime_region': 'NEW_GOTHAM',
                            'seriousness': 'HIGH'
                        },
                        {
                            'crime_id': 'ab8cb62e-aca9-4f79-ad82-b77180e53498',
                            'crime_type': 'ARSON',
                            'responsible_criminal': {
                                'name': 'Leonard Snart',
                                'nickname': 'Captain Cold',
                                'age': 47,
                                'blood_type': 'UNDEFINED',
                                'criminal_description': "Leonard Snart was raised by an abusive father and took refuge with his grandfather, who worked in an ice truck. When his grandfather died, Snart grew tired of his father's abuse and set out to start a criminal career. Snart joined up with a group of small-time thieves and in planning out a robbery, each was issued a gun and a visor to protect their eyes against the flashes of gunfire. This visor design would later be adapted by Snart into his trademark costume. In recent years he has added a radio receiver to them which picks up the police band to monitor local law enforcement. Snart and the other thugs were captured by the Flash and imprisoned.",
                                'gender': 'MALE',
                                'height': 1.89,
                                'weight': 85.6,
                                'criminal_region': 'BLEAK_ISLAND'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Setting fire in 10 houses in one night, all the victims where from a organization',
                            'crime_region': 'OLD_GOTHAM',
                            'seriousness': 'HIGH'
                        }
                    ],
                    'criminal_owner': {
                        'name': 'Leonard Snart',
                        'nickname': 'Captain Cold',
                        'age': 47,
                        'blood_type': 'UNDEFINED',
                        'criminal_description': "Leonard Snart was raised by an abusive father and took refuge with his grandfather, who worked in an ice truck. When his grandfather died, Snart grew tired of his father's abuse and set out to start a criminal career. Snart joined up with a group of small-time thieves and in planning out a robbery, each was issued a gun and a visor to protect their eyes against the flashes of gunfire. This visor design would later be adapted by Snart into his trademark costume. In recent years he has added a radio receiver to them which picks up the police band to monitor local law enforcement. Snart and the other thugs were captured by the Flash and imprisoned.",
                        'gender': 'MALE',
                        'height': 1.89,
                        'weight': 85.6,
                        'criminal_region': 'BLEAK_ISLAND'
                    },
                    'danger_score': 4,
                    'is_arrested': False,
                    'prison': None
                },
                {
                    'criminal_record_id': 'eb24786c-72fe-49d4-9d51-83d985c5c68a',
                    'crime_list': [
                        {
                            'crime_id': '79fc6ada-a004-449f-b745-d015caeac6ca',
                            'crime_type': 'DRUG_DEALING',
                            'responsible_criminal': {
                                'name': "Jade Nguyen's",
                                'nickname': 'Cheshire',
                                'age': 36,
                                'blood_type': 'UNDEFINED',
                                'criminal_description': 'Cheshire is a skilled hand-to-hand combatant, and is one of the premiere martial artists and hand-to-hand combatants in the DC Universe. She is trained in several martial arts thought forever lost. In addition, Cheshire is also an expert triple-jointed acrobat, and uses this skill to move quickly and unexpectedly, and to also augment her fighting abilities. Of bigger concern are her artificial fingernails, which she dips in several varieties of poisons. She gives her weapons and other accessories a similar treatment.',
                                'gender': 'FEMALE',
                                'height': 1.75,
                                'weight': 70.7,
                                'criminal_region': 'AMUSEMENT_MILE'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Seeling drugs to 16 years old in alleys close to schools, resident areas and hospitals',
                            'crime_region': 'NEW_GOTHAM',
                            'seriousness': 'MEDIUM'
                        },
                        {
                            'crime_id': 'e871717e-b9cf-4f2b-8be0-9e6221cc59dc',
                            'crime_type': 'MURDER',
                            'responsible_criminal': {
                                'name': "Jade Nguyen's",
                                'nickname': 'Cheshire',
                                'age': 36,
                                'blood_type': 'UNDEFINED',
                                'criminal_description': 'Cheshire is a skilled hand-to-hand combatant, and is one of the premiere martial artists and hand-to-hand combatants in the DC Universe. She is trained in several martial arts thought forever lost. In addition, Cheshire is also an expert triple-jointed acrobat, and uses this skill to move quickly and unexpectedly, and to also augment her fighting abilities. Of bigger concern are her artificial fingernails, which she dips in several varieties of poisons. She gives her weapons and other accessories a similar treatment.',
                                'gender': 'FEMALE',
                                'height': 1.75,
                                'weight': 70.7,
                                'criminal_region': 'AMUSEMENT_MILE'
                            },
                            'date': 1648755588000,
                            'crime_description': 'Assanation of many doctors',
                            'crime_region': 'INDUSTRIAL_DISTRICT',
                            'seriousness': 'MEDIUM'
                        }
                    ],
                    'criminal_owner': {
                        'name': "Jade Nguyen's",
                        'nickname': 'Cheshire',
                        'age': 36,
                        'blood_type': 'UNDEFINED',
                        'criminal_description': 'Cheshire is a skilled hand-to-hand combatant, and is one of the premiere martial artists and hand-to-hand combatants in the DC Universe. She is trained in several martial arts thought forever lost. In addition, Cheshire is also an expert triple-jointed acrobat, and uses this skill to move quickly and unexpectedly, and to also augment her fighting abilities. Of bigger concern are her artificial fingernails, which she dips in several varieties of poisons. She gives her weapons and other accessories a similar treatment.',
                        'gender': 'FEMALE',
                        'height': 1.75,
                        'weight': 70.7,
                        'criminal_region': 'AMUSEMENT_MILE'
                    },
                    'danger_score': 3,
                    'is_arrested': False,
                    'prison': None
                }
            ],
            'message': 'all criminal records were found'
        }

        assert criminal_record_viewmodel == expected_criminal_record_json
