from .create_crime_controller import CreateCrimeController
from .create_crime_usecase import CreateCrimeUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


def create_crime_presenter(event, context):
    """Function Presenter of the route Create Crime"""

    repo = CriminalRecordRepositoryMock()
    usecase = CreateCrimeUsecase(repo)
    controller = CreateCrimeController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
