import json
from src.modules.create_criminal_record.app.create_criminal_record_presenter import create_criminal_record_presenter
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordPresenter:

    def test_delete_criminal_record_presenter(self):
        """
            The function that tests if the criminal record presenter response is the expected
        """
        repo = CriminalRecordRepositoryMock()

        event = {
            'body': {
                "new_criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": "2",
                "new_is_arrested": "True",
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": "30",
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": "1.82",
                    "weight": "80.3",
                    "criminal_region": "AMUSEMENT_MILE"
                }
            }
        }

        response = create_criminal_record_presenter(event, None)

        expected = {
            "criminal_record": {
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "gender": "MALE",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "AMUSEMENT_MILE"
                },
                "danger_score": 2,
                "is_arrested": True,
                "prison": "BLACKGATE"
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
            'body': {
                "new_danger_score": "2",
                "new_is_arrested": "True",
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": "30",
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": "1.82",
                    "weight": "80.3",
                    "criminal_region": "AMUSEMENT_MILE"
                }
            }
        }
        response = create_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is missing"
