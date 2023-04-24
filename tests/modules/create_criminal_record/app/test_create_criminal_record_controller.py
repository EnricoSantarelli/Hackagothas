from src.modules.create_criminal_record.app.create_criminal_record_controller import CreateCriminalRecordController
from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordController:

    def test_create_criminal_record_controller(self):
        """
            The function that tests if the criminal record controller request is the expected
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
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
            })

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the criminal record was created"
        assert response.body['criminal_record']['criminal_record_id'] == "4d108071-6d0f-48cb-8675-5d38049c3ecc"
        assert response.body['criminal_record']['danger_score'] == 2
        assert response.body['criminal_record']['is_arrested'] == True
        assert response.body['criminal_record']['prison'] == "BLACKGATE"
        assert response.body['criminal_record']['criminal_owner']['name'] == "Edward Nigma"
        assert response.body['criminal_record']['criminal_owner']['nickname'] == "Riddler"
        assert response.body['criminal_record']['criminal_owner']['age'] == 30
        assert response.body['criminal_record']['criminal_owner']['blood_type'] == "AB_PLUS"
        assert response.body['criminal_record']['criminal_owner']['gender'] == "MALE"
        assert response.body['criminal_record']['criminal_owner']['criminal_description'] == "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence."
        assert response.body['criminal_record']['criminal_owner']['height'] == 1.82
        assert response.body['criminal_record']['criminal_owner']['weight'] == 80.3
        assert response.body['criminal_record']['criminal_owner']['criminal_region'] == "AMUSEMENT_MILE"

    def test_create_criminal_record_controller_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the criminal record id is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
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
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is missing"

    def test_create_criminal_record_controller_wrong_criminal_record_id_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the criminal record id is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "new_criminal_record_id": 412421412421421,
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
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is not valid"
