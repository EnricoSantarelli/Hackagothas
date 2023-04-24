from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
from .update_criminal_record_usecase import UpdateCriminalRecordUsecase
from .update_criminal_record_controller import UpdateCriminalRecordController


def update_criminal_record_presenter(event, context):
    """Function Presenter of the route Update Criminal Record"""

    repo = CriminalRecordRepositoryMock()
    usecase = UpdateCriminalRecordUsecase(repo)
    controller = UpdateCriminalRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
