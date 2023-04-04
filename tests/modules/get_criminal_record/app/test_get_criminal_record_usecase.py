import pytest
from src.modules.get_criminal_record.app.get_criminal_record_usecase import GetCriminalRecordUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordUsecase:

    def test_get_criminal_record_by_criminal_record_id(self):
        """
            The function that tests if the criminal record of a criminal record id is being returned by the usecase
        """

        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo=repo)

        criminal_record = usecase(
            criminal_record_id=repo.criminal_record_list[0].criminal_record_id)

        assert criminal_record == repo.criminal_record_list[0]

    def test_get_criminal_record_by_wrong_criminal_record_id(self):
        """
            The function that tests if the usecase is raising entity error when a wrong criminal record id is passed
        """

        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo=repo)

        with pytest.raises(EntityError):
            criminal_record = usecase(criminal_record_id=None)
        with pytest.raises(EntityError):
            criminal_record = usecase(criminal_record_id=123414214214)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id="d9af6081-74f9-478d-9599-d2b21a0")
