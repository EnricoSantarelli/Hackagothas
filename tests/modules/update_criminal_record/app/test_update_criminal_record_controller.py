from src.modules.update_criminal_record.app.update_criminal_record_controller import UpdateCriminalRecordController
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordController:

    def test_update_criminal_record_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "Penitenciária Blackgate",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB+",
                    "gender": "Male",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "New Gotham"
                }
            })

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the criminal record was updated"
        assert response.body['criminal_record']['criminal_record_id'] == "4d108071-6d0f-48cb-8675-5d38049c3ecc"
        assert response.body['criminal_record']['danger_score'] == 2
        assert response.body['criminal_record']['is_arrested'] == True
        assert response.body['criminal_record']['prison'] == "Penitenciária Blackgate"
        assert response.body['criminal_record']['criminal_owner']['name'] == "Edward Nigma"
        assert response.body['criminal_record']['criminal_owner']['nickname'] == "Riddler"
        assert response.body['criminal_record']['criminal_owner']['age'] == 30
        assert response.body['criminal_record']['criminal_owner']['blood_type'] == "AB+"
        assert response.body['criminal_record']['criminal_owner']['gender'] == "Male"
        assert response.body['criminal_record']['criminal_owner']['criminal_description'] == "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence."
        assert response.body['criminal_record']['criminal_owner']['height'] == 1.82
        assert response.body['criminal_record']['criminal_owner']['weight'] == 80.3
        assert response.body['criminal_record']['criminal_owner']['criminal_region'] == "New Gotham"
