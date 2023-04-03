import json
from src.modules.update_criminal_record.app.update_criminal_record_presenter import update_criminal_record_presenter
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordPresenter:

    def test_update_criminal_record_presenter(self):
        """
            The function that tests if the criminal record presenter response is the expected
        """

        event = {
            'body': {
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
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

        response = update_criminal_record_presenter(event, None)

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
            "message": "the criminal record was updated"
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expected

    def test_update_criminal_record_presenter_no_items_found(self):
        """
            The function that tests if the criminal record presenter response is raising an no items found when there isn't any criminal record with the criminal record id passed
        """
        event = {
            'body': {
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3e66",
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

        response = update_criminal_record_presenter(event, None)

        assert response["status_code"] == 404
        assert json.loads(
            response["body"]) == "No items found for criminal_record_id"

    def test_update_criminal_record_presenter_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record presenter response is raising an missing parameters when the criminal record id is missing
        """
        event = {
            'body': {
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "AMUSEMENT_MILE"
                }
            }
        }

        response = update_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is missing"

    def test_update_criminal_record_presenter_wrong_criminal_record_id_type(self):
        """
            The function that tests if the criminal record presenter response is raising an entity error if the type of the criminal record id is wrong
        """
        event = {
            'body': {
                "criminal_record_id": 241125215124214,
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

        response = update_criminal_record_presenter(event, None)

        assert response["status_code"] == 400
        assert json.loads(
            response["body"]) == "Field criminal_record_id is not valid"
