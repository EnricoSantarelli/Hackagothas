import json
from src.modules.create_crime.app.create_crime_presenter import create_crime_presenter


class Test_CreateCrimePresenter:

    def test_create_crime_presenter(self):
        """
            The function that tests if the crime presenter response is the expected
        """

        event = {
            'body': {
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            }
        }

        response = create_crime_presenter(event, None)

        expected = {
            "crime": {
                "crime_description": "Murder of other vilains",
                "crime_type": "MURDER",
                "date": 1648755588000,
                "seriousness": "LOW",
                "crime_region": "AMUSEMENT_MILE",
                "responsible_criminal": {
                    "name": "Lonnie Machin",
                    "nickname": "Anarky",
                    "age": 16,
                    "blood_type": "UNDEFINED",
                    "criminal_description": "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself\u2014surprise.",
                    "gender": "MALE",
                    "height": 1.7,
                    "weight": 75.2,
                    "criminal_region": "NEW_GOTHAM"
                }
            },
            "message": "the crime was created"
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected
