import json
from src.modules.get_crimes_by_criminal_record_id.app.get_crimes_by_criminal_record_id_presenter import get_crimes_by_criminal_record_id_presenter
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCrimesByCriminalRecordIdPresenter:

    def test_get_crimes_by_criminal_record_id_presenter(self):
        """
            The function that tests if the criminal record presenter response is the expected
        """
        repo = CriminalRecordRepositoryMock()
        criminal_record_id = repo.criminal_record_list[0].criminal_record_id

        event = {
            "body": {
                "criminal_record_id": criminal_record_id}
        }

        response = get_crimes_by_criminal_record_id_presenter(event, None)

        expected = {
            "crimes": [
                {
                    "crime_id": "d9af6081-74f9-478d-9599-d2b21a06b386",
                    "crime_type": "ARSON",
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
                    },
                    "date": 1648755588000,
                    "crime_description": "Crime committed violently against innocent people",
                    "crime_region": "AMUSEMENT_MILE",
                    "seriousness": "HIGH"
                },
                {
                    "crime_id": "9130a793-ad89-4171-adf2-c33575a4c066",
                    "crime_type": "THEFT",
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
                    },
                    "date": 1648755588000,
                    "crime_description": "Armed robbery against the elderly",
                    "crime_region": "NEW_GOTHAM",
                    "seriousness": "MEDIUM"
                }
            ],
            "message": "all crimes were found"
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected

    def test_get_crimes_by_criminal_record_id_presenter_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record presenter response is raising an missing parameters when the criminal record id is missing
        """
        event = {
            "body": {}
        }

        response = get_crimes_by_criminal_record_id_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is missing"

    def test_get_crimes_by_criminal_record_id_presenter_wrong_criminal_record_id_type(self):
        """
            The function that tests if the criminal record presenter response is raising an entity error if the type of the criminal record id is wrong
        """
        event = {
            "body": {'criminal_record_id': 43214242432412321312321}
        }

        response = get_crimes_by_criminal_record_id_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is not valid"

    def test_get_crimes_by_criminal_record_id_presenter_no_items_found(self):
        """
            The function that tests if the criminal record presenter response is raising an no items found when there isn't any crime list with the criminal record id passed
        """
        event = {
            "body": {'criminal_record_id': 'd9af6081-74f9-478d-9599-d2b21a06b386'}
        }

        response = get_crimes_by_criminal_record_id_presenter(event, None)

        assert response["status_code"] == 404
        assert json.loads(
            response["body"]) == "No items found for criminal_record_id"
