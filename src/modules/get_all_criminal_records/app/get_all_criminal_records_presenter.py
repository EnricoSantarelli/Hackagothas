from .get_all_criminal_records_controller import GetAllCriminalRecordsController
from .get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


def get_all_criminal_records_presenter(event, context):
    """Function Presenter of the route Update Criminal Record"""

    repo = CriminalRecordRepositoryMock()
    usecase = GetAllCriminalRecordsUsecase(repo)
    controller = GetAllCriminalRecordsController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
