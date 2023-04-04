from src.shared.helpers.external_interfaces.http_codes import OK
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, NotFound
from .get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from .get_all_criminal_records_viewmodel import GetAllCriminalRecordsViewmodel
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class GetAllCriminalRecordsController:
    """Controller of the route Get All Criminal Records"""

    def __init__(self, usecase: GetAllCriminalRecordsUsecase):
        """CriminalRecordController contructor instantiating the usecase"""
        self.getAllCriminalRecordsUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            criminal_records_response = self.getAllCriminalRecordsUsecase()
            viewmodel = GetAllCriminalRecordsViewmodel(
                criminal_records_list=criminal_records_response)

            return OK(body=viewmodel.to_dict())

        except Exception as err:
            return InternalServerError(body=err.args[0])
