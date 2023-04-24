from src.modules.get_crimes_by_criminal_record_id.app.get_crimes_by_criminal_record_id_viewmodel import GetCrimesByCriminalRecordIdViewmodel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCrimesByCriminalRecordIdViewmodel:

    def test_get_crimes_by_criminal_record_id(self):
        """
            The function that tests if the criminal record view model translation is the same as the expected 
        """

        repo = CriminalRecordRepositoryMock()
        crime_list_viewmodel = GetCrimesByCriminalRecordIdViewmodel(
            crime_list=repo.criminal_record_list[0].crime_list).to_dict()

        expected_crime_list_json = {
            'crimes': [
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
            'message': 'all crimes were found'
        }

        assert crime_list_viewmodel == expected_crime_list_json
