import pytest
from src.modules.get_crimes_by_criminal_record_id.app.get_crimes_by_criminal_record_id_usecase import GetCrimesByCriminalRecordIdUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCrimesByCriminalRecordIdUsecase:

    def test_get_crimes_by_criminal_record_id(self):
        """
            The function that tests if all crimes of a criminal record is being returned by the usecase
        """

        repo = CriminalRecordRepositoryMock()
        usecase = GetCrimesByCriminalRecordIdUsecase(repo=repo)

        crimes_list = usecase(
            criminal_record_id=repo.criminal_record_list[0].criminal_record_id)

        assert crimes_list == repo.criminal_record_list[0].crime_list

    def test_get_crimes_by_wrong_criminal_record_id(self):
        """
            The function that tests if the usecase is raising entity error when a wrong criminal record id is passed
        """

        repo = CriminalRecordRepositoryMock()
        usecase = GetCrimesByCriminalRecordIdUsecase(repo=repo)

        with pytest.raises(EntityError):
            crimes_list_1 = usecase(criminal_record_id=None)
        with pytest.raises(EntityError):
            crimes_list_2 = usecase(criminal_record_id=123414214214)
        with pytest.raises(EntityError):
            crimes_list_3 = usecase(
                criminal_record_id="d9af6081-74f9-478d-9599-d2b21a0")
