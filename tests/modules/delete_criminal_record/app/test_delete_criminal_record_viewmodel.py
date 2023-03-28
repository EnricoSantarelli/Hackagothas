from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_DeleteCriminalRecordViewmodel:

    def test_delete_criminal_record_viewmodel(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record_viewmodel = DeleteCriminalRecordViewmodel(
            repo.criminal_record_list[1])

        expected_criminal_record_json = {
            'criminal_record': {
                'criminal_record_id': '4d108071-6d0f-48cb-8675-5d38049c3ecc', 'crime_list': [
                    {'crime_id': 'd9af6081-74f9-478d-9599-d2b21a06b386', 'crime_type': 'Arson', 'criminal':
                     {'name': 'Lonnie Machin', 'nickname': 'Anarky', 'age': 16, 'blood_type': 'Undefined',
                         'description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.', 'gender': 'Male', 'height': 1.70, 'weight': 75.0, 'region': 'New Gotham'},
                     'date': 1648755588000, 'description': 'Crime committed violently against innocent people', 'region': 'Amusement Mile', 'seriousness': 'High'
                     },
                    {'crime_id': '9130a793-ad89-4171-adf2-c33575a4c066', 'crime_type': 'Theft', 'criminal':
                     {'name': 'Lonnie Machin', 'nickname': 'Anarky', 'age': 16, 'blood_type': 'Undefined',
                         'description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.', 'gender': 'Male', 'height': 1.70, 'weight': 75.0, 'region': 'New Gotham'},
                     'date': 1648755588000, 'description': 'Armed robbery against the elderly', 'region': 'New Gotham', 'seriousness': 'Medium'
                     },
                ],
                'criminal': {'name': 'Lonnie Machin', 'nickname': 'Anarky', 'age': 16, 'blood_type': 'Undefined', 'description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.', 'gender': 'Male', 'height': 1.70, 'weight': 75.0, 'region': 'New Gotham'},
                'danger_score': 3, 'is_arrested': 'False', 'prison': 'None'
            },
            'message': 'the criminal record was deleted'
        }

        assert criminal_record_viewmodel.to_dict() == expected_criminal_record_json
