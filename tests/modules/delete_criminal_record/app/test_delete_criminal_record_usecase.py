import pytest
from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_DeleteCriminalRecordUsecase:
    def test_delete_criminal_record_usecase(self):
        """
            The function that tests if the criminal record is being deleted by the repository when calling the usecase DeleteCriminalRecordusecase
        """
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo=repo)
        criminal_record_len_before_delete = len(repo.criminal_record_list)
        criminal_record = usecase(
            criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc")

        assert type(criminal_record) == CriminalRecord
        assert len(
            repo.criminal_record_list) == criminal_record_len_before_delete - 1

    def test_delete_criminal_record_usecase_wrong_criminal_record_id(self):
        """
            The function that tests if is rasing an entity error when calling the usecase DeleteCriminalRecordusecase with a wrong criminal_record_id
        """
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo=repo)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id=None)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id=421321321321312)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3eccccccccc")

    def test_delete_criminal_record_usecase_not_exists(self):
        """
            The function that tests if is rasing an no items found when calling the usecase DeleteCriminalRecordusecase with a criminal_record_id that doesn't exists
        """
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            criminal_record = usecase(
                criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3egg")
