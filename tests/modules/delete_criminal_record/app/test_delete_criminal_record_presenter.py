import json
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_DeleteCriminalRecordPresenter:

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

        response = delete_criminal_record_presenter(event, None)

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
                            "criminal_description": "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                            "gender": "Male",
                            "height": 1.7,
                            "weight": 75.2,
                            "criminal_region": "New Gotham"
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
                            "criminal_description": "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                            "gender": "Male",
                            "height": 1.7,
                            "weight": 75.2,
                            "criminal_region": "New Gotham"
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
                    "criminal_description": "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                    "gender": "Male",
                    "height": 1.7,
                    "weight": 75.2,
                    "criminal_region": "New Gotham"
                },
                "danger_score": 3,
                "is_arrested": False,
                "prison": None
            },
            "message": "the criminal record was deleted"
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected

    def test_delete_criminal_record_presenter_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record presenter response is raising an missing parameters when the criminal record id is missing
        """
        event = {
            "body": {}
        }

        response = delete_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is missing"

    def test_delete_criminal_record_presenter_no_items_found(self):
        """
            The function that tests if the criminal record presenter response is raising an no items found when there isn't any criminal record with the criminal record id passed
        """
        event = {
            "body": {'criminal_record_id': "cf54ac31-64ed-425f-b8b2-b38b1e59bf2f"}
        }

        response = delete_criminal_record_presenter(event, None)

        assert response["status_code"] == 404
        assert json.loads(
            response["body"]) == "No items found for criminal_record_id"

    def test_delete_criminal_record_presenter_no_items_found(self):
        """
            The function that tests if the criminal record presenter response is raising an entity error if the type of the criminal record id is wrong
        """
        event = {
            "body": {'criminal_record_id': 43214242432412321312321}
        }

        response = delete_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is not valid"
