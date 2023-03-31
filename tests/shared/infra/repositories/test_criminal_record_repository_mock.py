from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal import Criminal
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.blood_type_enum import BLOOD_TYPE
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.prison_enum import PRISON
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CriminalRecordRepositoryMock:

    # list variable of a crime_list to be used in the tests
    crime_list = [Crime(crime_id="cdccceb6-5acc-493e-8958-9907e096fa80",
                        crime_type=CRIME_TYPE.MURDER,
                        responsible_criminal=Criminal(name="Harleen Quinzel",
                                                      nickname="Harley Quinn",
                                                      criminal_description="In time, Harley came to realize the Joker was holding her back and she struck out on her own. She became an entrepreneur and a member of several slightly less-than-reputable super teams (including the Suicide Squad), Gotham City’s all-girl gang the Gotham City Sirens, and a traveling sideshow. Along the way Harley has become one of the most popular super-villains in the DC Universe, thanks in part to her versatility, charisma and cheery-but-deranged outlook on life.",
                                                      gender=GENDER.FEMALE,
                                                      criminal_region=REGION.NEW_GOTHAM,
                                                      blood_type=BLOOD_TYPE.AB_MINUS,
                                                      age=26,
                                                      weight=50.30,
                                                      height=1.60),
                        date=1648755588000,
                        crime_description="Crime committed violently against innocent people",
                        crime_region=REGION.AMUSEMENT_MILE,
                        seriousness=SERIOUSNESS.MEDIUM),
                  Crime(crime_id="c94efd7c-aede-4a1f-81ee-7ec045afbf2a",
                        crime_type=CRIME_TYPE.THEFT,
                        responsible_criminal=Criminal(name="Harleen Quinzel",
                                                      nickname="Harley Quinn",
                                                      criminal_description="In time, Harley came to realize the Joker was holding her back and she struck out on her own. She became an entrepreneur and a member of several slightly less-than-reputable super teams (including the Suicide Squad), Gotham City’s all-girl gang the Gotham City Sirens, and a traveling sideshow. Along the way Harley has become one of the most popular super-villains in the DC Universe, thanks in part to her versatility, charisma and cheery-but-deranged outlook on life.",
                                                      gender=GENDER.FEMALE,
                                                      criminal_region=REGION.NEW_GOTHAM,
                                                      blood_type=BLOOD_TYPE.AB_MINUS,
                                                      age=26,
                                                      weight=50.30,
                                                      height=1.60),
                        date=1648755588000,
                        crime_description="Armed robbery against her doctor",
                        crime_region=REGION.MIAGANI_ISLAND,
                        seriousness=SERIOUSNESS.LOW)]
    # variable of a criminal to be used in the tests
    criminal = Criminal(name="Harleen Quinzel",
                        nickname="Harley Quinn",
                        criminal_description="In time, Harley came to realize the Joker was holding her back and she struck out on her own. She became an entrepreneur and a member of several slightly less-than-reputable super teams (including the Suicide Squad), Gotham City’s all-girl gang the Gotham City Sirens, and a traveling sideshow. Along the way Harley has become one of the most popular super-villains in the DC Universe, thanks in part to her versatility, charisma and cheery-but-deranged outlook on life.",
                        gender=GENDER.FEMALE,
                        criminal_region=REGION.NEW_GOTHAM,
                        blood_type=BLOOD_TYPE.AB_MINUS,
                        age=26,
                        weight=50.30,
                        height=1.60)

    def test_get_criminal_record(self):
        """
            The function that tests if the criminal record is being getted by the repository when calling the function get_criminal_record
        """
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.get_criminal_record(
            criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc")
        criminal_list = repo.criminal_list
        crime_list = repo.crime_list

        assert criminal_record.criminal_owner == criminal_list[0]
        assert criminal_record.crime_list == [crime_list[0], crime_list[1]]
        assert criminal_record.criminal_record_id == "4d108071-6d0f-48cb-8675-5d38049c3ecc"
        assert criminal_record.danger_score == 3
        assert criminal_record.is_arrested == False

    def test_create_criminal_record(self):
        """
            The function that tests if the criminal record is being created by the repository when calling the function create_criminal_record
        """
        repo = CriminalRecordRepositoryMock()
        new_criminal_record = CriminalRecord(
            criminal_owner=self.criminal,
            crime_list=self.crime_list,
            criminal_record_id="cd689029-4a77-484e-9d78-c9ae19329178",
            danger_score=5,
            is_arrested=True,
            prison=PRISON.BLACKGATE)

        criminal_record_created = repo.create_criminal_record(
            new_criminal_record=new_criminal_record)

        assert criminal_record_created == new_criminal_record

    def test_delete_criminal_record(self):
        """
            The function that tests if the criminal record is being deleted by the repository when calling the function delete_criminal_record
        """
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.criminal_record_list[0]

        deleted_criminal_record = repo.delete_criminal_record(
            criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc")

        assert criminal_record == deleted_criminal_record

    def test_update_criminal_record(self):
        """
            The function that tests if the criminal record is being updated by the repository when calling the function update_criminal_record
        """
        repo = CriminalRecordRepositoryMock()

        new_criminal_record = repo.update_criminal_record(criminal_record_id="4d108071-6d0f-48cb-8675-5d38049c3ecc",
                                                          new_criminal_owner=self.criminal, new_is_arrested=True, new_prison=PRISON.ARKHAMASILUM, new_danger_score=2)

        assert new_criminal_record.criminal_owner == self.criminal
        assert new_criminal_record.is_arrested == True
        assert new_criminal_record.prison == PRISON.ARKHAMASILUM
        assert new_criminal_record.danger_score == 2
