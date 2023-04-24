import pytest
from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordUsecase:
    def test_create_criminal_record_usecase(self):
        """
            The function that tests if the criminal record is being created by the repository when calling the usecase CreateCriminalRecordusecase
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo_criminal_record=repo)
        criminal_record_len_before_create = len(repo.criminal_record_list)
        criminal_record = usecase(new_criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc",
                                         new_criminal_owner=Criminal(name= "Edward Nigma",
                    nickname= "Riddler",
                    age= 30,
                    blood_type= BLOOD_TYPE.AB_PLUS,
                    gender= GENDER.MALE,
                    criminal_description= "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    height=1.82,
                    weight=80.3,
                    criminal_region= REGION.AMUSEMENT_MILE), new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)

        assert type(criminal_record) == CriminalRecord
        assert len(
            repo.criminal_record_list) == criminal_record_len_before_create + 1

    def test_create_criminal_record_usecase_wrong_criminal_record_id(self):
        """
            The function that tests if is rasing an entity error when calling the usecase CreateCriminalRecordUsecase with a wrong criminal_record_id
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCriminalRecordUsecase(repo_criminal_record=repo)
        with pytest.raises(EntityError):
            criminal_record = usecase(new_criminal_record_id=None,
                                         new_criminal_owner=Criminal(name= "Edward Nigma",
                    nickname= "Riddler",
                    age= 30,
                    blood_type= BLOOD_TYPE.AB_PLUS,
                    gender= GENDER.MALE,
                    criminal_description= "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    height=1.82,
                    weight=80.3,
                    criminal_region= REGION.AMUSEMENT_MILE), new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)
        with pytest.raises(EntityError):
            criminal_record = usecase(new_criminal_record_id=412421125215,
                                         new_criminal_owner=Criminal(name= "Edward Nigma",
                    nickname= "Riddler",
                    age= 30,
                    blood_type= BLOOD_TYPE.AB_PLUS,
                    gender= GENDER.MALE,
                    criminal_description= "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    height=1.82,
                    weight=80.3,
                    criminal_region= REGION.AMUSEMENT_MILE), new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)
        with pytest.raises(EntityError):
            criminal_record = usecase(new_criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecccccccccc",
                                         new_criminal_owner=Criminal(name= "Edward Nigma",
                    nickname= "Riddler",
                    age= 30,
                    blood_type= BLOOD_TYPE.AB_PLUS,
                    gender= GENDER.MALE,
                    criminal_description= "A complete psychopath with no moral compass whatsoever, Riddler, is characterized by his charades and riddles, which he uses to taunt his enemies and to show off his intelligence.",
                    height=1.82,
                    weight=80.3,
                    criminal_region= REGION.AMUSEMENT_MILE), new_is_arrested=True, new_prison=PRISON.STATEPRISON, new_danger_score=2)