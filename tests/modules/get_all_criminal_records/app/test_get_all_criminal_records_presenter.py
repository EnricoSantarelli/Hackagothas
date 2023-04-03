import json
from src.modules.get_all_criminal_records.app.get_all_criminal_records_presenter import get_all_criminal_records_presenter


class Test_GetAllCriminalRecordsPresenter:

    def test_get_all_criminal_records_presenter(self):
        """
            The function that tests if the get all criminal records presenter response is the expected
        """

        event = {}

        response = get_all_criminal_records_presenter(event, None)

        assert json.loads(response["body"])[
            'message'] == "all criminal records were found"
