import json
from src.modules.create_criminal_record.create_criminal_record_presenter import create_criminal_record_presenter
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordPresenter:

    def test_delete_criminal_record_presenter(self):
        """
            The function that tests if the criminal record presenter response is the expected
        """
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.criminal_record_list[0]

        event = {
            "body": {
                "criminal_record_id": criminal_record.criminal_record_id}
        }

        response = create_criminal_record_presenter(event, None)

        expected = {
            "criminal_record": {
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "crime_list": [
                    {
                        "crime_id": "d9af6081-74f9-478d-9599-d2b21a06b386",
                        "crime_type": "Arson",
                        "responsible_criminal": {
                            "name": "Lonnie Machin",
                            "nickname": "Anarky",
                            "age": 16,
                            "blood_type": "Undefined",
                            "criminal_description": "New Gotham",
                            "gender": "Male",
                            "height": 1.7,
                            "weight": 75.2
                        },
                        "date": 1648755588000,
                        "crime_description": "Crime committed violently against innocent people",
                        "crime_region": "Amusement Mile",
                        "seriousness": "High"
                    },
                    {
                        "crime_id": "9130a793-ad89-4171-adf2-c33575a4c066",
                        "crime_type": "Theft",
                        "responsible_criminal": {
                            "name": "Lonnie Machin",
                            "nickname": "Anarky",
                            "age": 16,
                            "blood_type": "Undefined",
                            "criminal_description": "New Gotham",
                            "gender": "Male",
                            "height": 1.7,
                            "weight": 75.2
                        },
                        "date": 1648755588000,
                        "crime_description": "Armed robbery against the elderly",
                        "crime_region": "New Gotham",
                        "seriousness": "Medium"
                    }
                ],
                "criminal_owner": {
                    "name": "Lonnie Machin",
                    "nickname": "Anarky",
                    "age": 16,
                    "blood_type": "Undefined",
                    "criminal_description": "New Gotham",
                    "gender": "Male",
                    "height": 1.7,
                    "weight": 75.2
                },
                "danger_score": 3,
                "is_arrested": False,
                "prison": None
            },
            "message": "the criminal record was created"
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected

    def test_create_criminal_record_presenter_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record presenter response is raising an missing parameters when the criminal record id is missing
        """
        event = {
            "body": {}
        }

        response = create_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is missing"

    def test_create_criminal_record_presenter_no_items_found(self):
        """
            The function that tests if the criminal record presenter response is raising an entity error if the type of the criminal record id is wrong
        """
        event = {
            "body": {'criminal_record_id': 43214242432412321312321}
        }

        response = create_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is not valid"
