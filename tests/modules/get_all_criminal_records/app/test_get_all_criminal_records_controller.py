from src.modules.get_all_criminal_records.app.get_all_criminal_records_controller import GetAllCriminalRecordsController
from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetAllCriminalRecordsController:

    def test_get_all_criminal_records_controller(self):
        """
            The function that tests if the controller GetAllCriminalRecordsController is returning the correct response
        """

        repo = CriminalRecordRepositoryMock()
        usecase = GetAllCriminalRecordsUsecase(repo)
        controller = GetAllCriminalRecordsController(usecase)

        response = controller(request={})

        assert response.status_code == 200
        assert response.body['message'] == 'all criminal records were found'
