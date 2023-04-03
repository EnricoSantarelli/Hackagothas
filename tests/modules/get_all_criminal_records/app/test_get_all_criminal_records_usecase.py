from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetAllCriminalRecordsUsecase:

    def test_get_all_criminal_records(self):
        """
            The function that tests if all criminal records is being getted by the repository when calling the usecase GetAllCriminalRecordsUsecase
        """

        repo = CriminalRecordRepositoryMock()
        usecase = GetAllCriminalRecordsUsecase(repo=repo)

        criminal_records_list = usecase()

        assert criminal_records_list == repo.criminal_record_list
