import pytest
from src.modules.create_crime.app.create_crime_usecase import CreateCrimeUsecase
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.helpers.errors.usecase_errors import ExcededParameters
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCrimeUsecase:

    def test_create_crime_usecase(self):
        """
            The function that tests if the crime is being by the repository when calling the usecase CreateCrimeUsecase
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo=repo)

        crime_list_len = len(repo.crime_list)
        crime_list_criminal_record_len = len(
            repo.criminal_record_list[0].crime_list)

        create_crime = usecase(crime_description="Murder of other vilains",
                               crime_type=CRIME_TYPE.MURDER, date=1648755588000, seriousness=SERIOUSNESS.LOW, crime_region=REGION.AMUSEMENT_MILE,
                               responsible_criminal=repo.criminal_list[0])

        assert len(repo.crime_list) == crime_list_len + 1
        assert len(
            repo.criminal_record_list[0].crime_list) == crime_list_criminal_record_len + 1
        assert repo.criminal_record_list[0].crime_list[2].crime_description == create_crime.crime_description
        assert repo.criminal_record_list[0].crime_list[2].crime_type == create_crime.crime_type
        assert repo.criminal_record_list[0].crime_list[2].date == create_crime.date
        assert repo.criminal_record_list[0].crime_list[2].seriousness == create_crime.seriousness
        assert repo.criminal_record_list[0].crime_list[2].crime_region == create_crime.crime_region
        assert repo.criminal_record_list[0].crime_list[2].responsible_criminal == create_crime.responsible_criminal

    def test_create_crime_usecase_with_inexistent_criminal(self):
        """
            The function that tests if the usecases is raising an entity error when passing a criminal that does not exist
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo=repo)

        with pytest.raises(ExcededParameters):
            create_crime = usecase(crime_description="Murder of other vilains",
                                   crime_type=CRIME_TYPE.MURDER, date=1648755588000, seriousness=SERIOUSNESS.LOW, crime_region=REGION.AMUSEMENT_MILE,
                                   responsible_criminal=Criminal(name="Coor Denas",
                                                                 nickname="Denas",
                                                                 criminal_description="Denas uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                                                                 gender=GENDER.MALE,
                                                                 criminal_region=REGION.NEW_GOTHAM,
                                                                 blood_type=BLOOD_TYPE.UNDEFINED,
                                                                 age=50,
                                                                 weight=150.10,
                                                                 height=3.70))
