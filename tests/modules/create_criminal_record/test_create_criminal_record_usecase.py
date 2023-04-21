import pytest
from src.modules.create_criminal_record.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordUsecase:
    def test_create_criminal_record_usecase(self):
        """
            The function that tests if the criminal record is being created by the repository when calling the usecase CreateCriminalRecordusecase
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo=repo)
        criminal_record_len_before_create = len(repo.criminal_record_list)
        criminal_record = usecase(
            criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc")

        assert type(criminal_record) == CriminalRecord
        assert len(
            repo.criminal_record_list) == criminal_record_len_before_create + 1

    def test_create_criminal_record_usecase_wrong_criminal_record_id(self):
        """
            The function that tests if is rasing an entity error when calling the usecase CreateCriminalRecordUsecase with a wrong criminal_record_id
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo=repo)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id=None)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id=421321321321312)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3eccccccccc")

    def test_create_criminal_record_usecase_not_exists(self):
        """
            The function that tests if is rasing an no items found when calling the usecase CreateCriminalRecordusecase with a criminal_record_id that doesn't exists
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            criminal_record = usecase(
                criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3egg")
