from src.modules.create_crime.app.create_crime_controller import CreateCrimeController
from src.modules.create_crime.app.create_crime_usecase import CreateCrimeUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCrimeController:

    def test_create_crime_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            }
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the crime was created"

    def test_create_crime_controller_missing_crime_description(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the crime_description is missing
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field crime_description is missing"

    def test_create_crime_controller_missing_crime_type(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the crime_type is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field crime_type is missing"

    def test_create_crime_controller_missing_date(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the date is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field date is missing"

    def test_create_crime_controller_missing_seriousness(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the seriousness is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field seriousness is missing"

    def test_create_crime_controller_missing_crime_region(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the crime_region is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field crime_region is missing"

    def test_create_crime_controller_missing_responsible_criminal(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field responsible_criminal is missing"

    def test_create_crime_controller_missing_responsible_criminal_name(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_name is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_create_crime_controller_missing_responsible_criminal_nickname(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_nickname is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field nickname is missing"

    def test_create_crime_controller_missing_responsible_criminal_age(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_age is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field age is missing"

    def test_create_crime_controller_missing_responsible_criminal_blood_type(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_blood_type is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field blood_type is missing"

    def test_create_crime_controller_missing_responsible_criminal_criminal_description(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_criminal_description is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_description is missing"

    def test_create_crime_controller_missing_responsible_criminal_gender(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_gender is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field gender is missing"

    def test_create_crime_controller_missing_responsible_criminal_height(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_height is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field height is missing"

    def test_create_crime_controller_missing_responsible_criminal_weight(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_weight is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field weight is missing"

    def test_create_crime_controller_missing_responsible_criminal_criminal_region(self):
        """
            The function that tests if the criminal record controller request is raising an missing parameters when the responsible_criminal_criminal_region is missing
        """

        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_region is missing"

    def test_update_criminal_record_controller_wrong_crime_region_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the crime_region is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'rio de janeiro',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field crime_region is not valid"

    def test_update_criminal_record_controller_wrong_crime_crime_type_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the crime_type is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'assassinato',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field crime_type is not valid"

    def test_update_criminal_record_controller_wrong_crime_seriousness_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the seriousness is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 12,
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field seriousness is not valid"

    def test_update_criminal_record_controller_wrong_crime_responsible_criminal_blood_type_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the responsible_criminal_blood_type is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'não definido',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field blood_type is not valid"

    def test_update_criminal_record_controller_wrong_crime_responsible_criminal_gender_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the responsible_criminal_gender is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'não binário',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field gender is not valid"

    def test_update_criminal_record_controller_wrong_crime_responsible_criminal_criminal_region_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the responsible_criminal_criminal_region is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'região'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field criminal_region is not valid"

    def test_update_criminal_record_controller_wrong_responsible_criminal_entity(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the entity of the responsible_criminal is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': {
                    'name': 'Lonnie Machin',
                    'nickname': 'Anarky',
                    'age': "16",
                    'blood_type': 'UNDEFINED',
                    'criminal_description': 'Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.',
                    'gender': 'MALE',
                    'height': "1.7",
                    'weight': "75.2",
                    'criminal_region': 'NEW_GOTHAM',
                    'invalid': 'invalid'
                }
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field responsible_criminal is not valid"

    def test_update_criminal_record_controller_wrong_responsible_criminal_type(self):
        """
            The function that tests if the criminal record controller request is raising an entity error if the type of the responsible_criminal is wrong
        """
        repo = CriminalRecordRepositoryMock()
        usecase = CreateCrimeUsecase(repo)
        controller = CreateCrimeController(usecase)

        request = HttpRequest(
            body={
                'crime_description': 'Murder of other vilains',
                'crime_type': 'MURDER',
                'date': "1648755588000",
                'seriousness': 'LOW',
                'crime_region': 'AMUSEMENT_MILE',
                'responsible_criminal': 1
            })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field responsible_criminal is not valid"
