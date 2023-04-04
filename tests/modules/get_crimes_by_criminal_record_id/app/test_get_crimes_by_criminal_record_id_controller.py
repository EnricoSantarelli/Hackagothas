from src.modules.get_crimes_by_criminal_record_id.app.get_crimes_by_criminal_record_id_controller import GetCrimesByCriminalRecordIdController
from src.modules.get_crimes_by_criminal_record_id.app.get_crimes_by_criminal_record_id_usecase import GetCrimesByCriminalRecordIdUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCrimesByCriminalRecordIdController:

    def test_get_crimes_by_criminal_record_id_controller(self):
        """
            The function that tests if the criminal record controller request is the expected
        """
        repo = CriminalRecordRepositoryMock()
        usecase = GetCrimesByCriminalRecordIdUsecase(repo)
        controller = GetCrimesByCriminalRecordIdController(usecase)
        criminal_record = repo.criminal_record_list[0]

        request = HttpRequest(
            body={'criminal_record_id': criminal_record.criminal_record_id})

        response = controller(request)

        assert response.status_code == 200
        assert len(response.body['crimes']) == len(
            criminal_record.crime_list)
        assert response.body['message'] == "all crimes were found"

    def test_get_crimes_by_criminal_record_id_controller_controller_missing_criminal_record_id(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the criminal record id is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = GetCrimesByCriminalRecordIdUsecase(repo)
        controller = GetCrimesByCriminalRecordIdController(usecase)

        request = HttpRequest(
            body={})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is missing"

    def test_get_crimes_by_criminal_record_id_controller_no_items_found(self):
        """
            The function that tests if the criminal record controller request is raising an no items found when there isn't any criminal record with the criminal record id passed
        """
        repo = CriminalRecordRepositoryMock()
        usecase = GetCrimesByCriminalRecordIdUsecase(repo)
        controller = GetCrimesByCriminalRecordIdController(usecase)

        request = HttpRequest(
            body={'criminal_record_id': "cf54ac31-64ed-425f-b8b2-b38b1e59bf2f"})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "No items found for criminal_record_id"

    def test_get_crimes_by_criminal_record_id_controller_wrong_criminal_record_id_type(self):
        """
            The function that tests if the criminal record controller request is raising an wrong type when the criminal record id is not a uuid
        """
        repo = CriminalRecordRepositoryMock()
        usecase = GetCrimesByCriminalRecordIdUsecase(repo)
        controller = GetCrimesByCriminalRecordIdController(usecase)

        request = HttpRequest(
            body={'criminal_record_id': 21321412421})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id is not valid"
