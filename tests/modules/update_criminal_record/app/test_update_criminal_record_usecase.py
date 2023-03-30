import pytest
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUsecase
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ExcededParameters, NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordUsecase:

    def test_update_criminal_record_usecase(self):
        """
            The function that tests if the criminal record is being updated by the repository when calling the usecase UpdateCriminalRecordUsecase
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo=repo)

        update_criminal_record = usecase(criminal_record_id=repo.criminal_record_list[0].criminal_record_id,
                                         new_criminal_owner=repo.criminal_list[1], new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)

        assert type(update_criminal_record) == CriminalRecord

        assert repo.criminal_record_list[0].criminal_owner == update_criminal_record.criminal_owner
        assert repo.criminal_record_list[0].danger_score == update_criminal_record.danger_score
        assert repo.criminal_record_list[0].is_arrested == update_criminal_record.is_arrested
        assert repo.criminal_record_list[0].prison == update_criminal_record.prison

    def test_update_criminal_record_usecase_not_exists(self):
        """
            The function that tests if is rasing an no items found when calling the usecase UpdateCriminalRecordusecase with a criminal_record_id that doesn't exists
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            criminal_record = usecase(criminal_record_id="eb24786c-72fe-49d4-9d51-83d985c5caaa",
                                      new_criminal_owner=repo.criminal_list[1], new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)

    def test_update_criminal_record_usecase_wrong_criminal_record_id(self):
        """
            The function that tests if is rasing an entity error when calling the usecase UpdateCriminalRecordusecase with a wrong criminal_record_id
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo=repo)
        with pytest.raises(EntityError):
            criminal_record = usecase(
                criminal_record_id=None,  new_criminal_owner=repo.criminal_list[1], new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)
        with pytest.raises(EntityError):
            criminal_record = usecase(criminal_record_id=2414221412451241,
                                      new_criminal_owner=repo.criminal_list[1], new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)
        with pytest.raises(EntityError):
            criminal_record = usecase(criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3eccccccccc",
                                      new_criminal_owner=repo.criminal_list[1], new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)

    def test_update_criminal_record_usecase_new_is_arrested(self):
        """
            The function that tests if is rasing an entity error when passing a prison when the is_arrested is false, or passing is_arrested true when prison is false
        """
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo=repo)
        with pytest.raises(ExcededParameters):
            criminal_record = usecase(criminal_record_id=repo.criminal_record_list[0].criminal_record_id,
                                      new_criminal_owner=repo.criminal_list[1], new_is_arrested=False, new_prison=PRISON.STATEPRISON, new_danger_score=2)
        with pytest.raises(MissingParameters):
            criminal_record = usecase(criminal_record_id=repo.criminal_record_list[0].criminal_record_id,
                                      new_criminal_owner=repo.criminal_list[1], new_is_arrested=True, new_prison=None, new_danger_score=2)
