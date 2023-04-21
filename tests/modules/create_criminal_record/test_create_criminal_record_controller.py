from src.modules.create_criminal_record.create_criminal_record_controller import CreateCriminalRecordController
from src.modules.create_criminal_record.create_criminal_record_usecase import CreateCriminalRecordUsecase
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
        criminal_record = repo.criminal_record_list[0]

        request = HttpRequest(
            body={'criminal_record_id': criminal_record.criminal_record_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the criminal record was deleted"
        assert response.body['criminal_record']['criminal_record_id'] == criminal_record.criminal_record_id

    def test_create_criminal_record_controller_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the criminal record id is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo)
        controller = CreateCriminalRecordController(usecase)

        request = HttpRequest(
            body={})

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
            body={'criminal_record_id': 43214242432412321312321})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is not valid"
