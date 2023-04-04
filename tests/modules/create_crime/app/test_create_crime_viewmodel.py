from src.modules.create_crime.app.create_crime_viewmodel import CreateCrimeViewmodel
from src.shared.domain.entities.crime import Crime
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.region_enum import REGION
from src.shared.domain.enums.seriousness_enum import SERIOUSNESS
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCrimeViewmodel:

    def test_create_crime_viewmodel(self):
        """
            The function that tests if the crime view model translation is the same as the expected
        """

        repo = CriminalRecordRepositoryMock()
        crime_viewmodel = CreateCrimeViewmodel(
            crime_description="Murder of other vilains",
            crime_type=CRIME_TYPE.MURDER, date=1648755588000, seriousness=SERIOUSNESS.LOW, crime_region=REGION.AMUSEMENT_MILE,
            responsible_criminal=repo.criminal_list[0]
        ).to_dict()

        expected_crime_json = {
            'crime': {
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': 1648755588000,
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': 16,
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': 1.7,
                    'weight': 75.2,
                    'criminal_region': 'NEW_GOTHAM'
                }
            },
            'message': 'the crime was created'
        }

        assert crime_viewmodel == expected_crime_json
