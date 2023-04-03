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
        assert response.body['message'] == "the criminal record was updated"
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

    def test_update_criminal_record_controller_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the criminal record id is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
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
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is missing"

    def test_update_criminal_record_controller_no_items_found(self):
        """
            The function that tests if the criminal record controller request is raising an no items found when there isn't any criminal record with the criminal record id passed
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3e55",
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
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "No items found for criminal_record_id"

    def test_update_criminal_record_controller_wrong_criminal_record_id_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the criminal record id is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": 42112512512521,
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
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is not valid"

    def test_update_criminal_record_controller_missing_new_danger_score(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_danger_score is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
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
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_danger_score is missing"

    def test_update_criminal_record_controller_missing_new_is_arrested(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_is_arrested is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
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
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_is_arrested is missing"

    def test_update_criminal_record_controller_missing_new_prison(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_prison is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_prison is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_owner is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_criminal_owner is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_name(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_owner_name is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_nickname(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_owner_nickname is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field nickname is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_age(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_owner_age is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field age is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_blood_type(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_owner_blood_type is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field blood_type is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_gender(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_owner_gender is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field gender is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_criminal_description(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_description is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": 30,
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "height": 1.82,
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_description is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_height(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_height is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
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
                    "weight": 80.3,
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field height is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_weight(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_weight is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
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
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field weight is missing"

    def test_update_criminal_record_controller_missing_new_criminal_owner_criminal_region(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the new_criminal_criminal_region is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
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
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_region is missing"

    def test_update_criminal_record_controller_wrong_new_prison_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the new_prison is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": "2",
                "new_is_arrested": "True",
                "new_prison": "15",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": "30",
                    "blood_type": "AB_PLUS",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": "1.82",
                    "weight": "80.3",
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_prison is not valid"

    def test_update_criminal_record_controller_wrong_new_criminal_owner_blood_type_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the blood_type is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": "2",
                "new_is_arrested": "True",
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": "30",
                    "blood_type": "True",
                    "gender": "MALE",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": "1.82",
                    "weight": "80.3",
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field blood_type is not valid"

    def test_update_criminal_record_controller_wrong_new_criminal_owner_gender_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the gender is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": "2",
                "new_is_arrested": "True",
                "new_prison": "BLACKGATE",
                "new_criminal_owner": {
                    "name": "Edward Nigma",
                    "nickname": "Riddler",
                    "age": "30",
                    "blood_type": "AB_PLUS",
                    "gender": "masculino",
                    "criminal_description": "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    "height": "1.82",
                    "weight": "80.3",
                    "criminal_region": "NEW_GOTHAM"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field gender is not valid"

    def test_update_criminal_record_controller_wrong_new_criminal_owner_criminal_region_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the criminal_region is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
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
                    "criminal_region": "abc paulista"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_region is not valid"

    def test_update_criminal_record_controller_wrong_new_criminal_owner_criminal_region_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the criminal_region is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
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
                    "criminal_region": "abc paulista"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_region is not valid"

    def test_update_criminal_record_controller_wrong_new_criminal_owner_entity(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the entity of the new_criminal_owner is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
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
                    "criminal_region": "NEW_GOTHAM",
                    "invalid": "invalid"
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_criminal_owner is not valid"

    def test_update_criminal_record_controller_wrong_new_criminal_owner_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the new_criminal_owner is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)
        controller = UpdateCriminalRecordController(usecase)

        request = HttpRequest(
            body={
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "new_danger_score": 2,
                "new_is_arrested": True,
                "new_prison": "BLACKGATE",
                "new_criminal_owner": 1
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_criminal_owner is not valid"
