import requests
from requests.auth import HTTPBasicAuth

class AtlassianRepository:

    def __init__(self, email: str):
        self.email = email

    def get_employee_atlassian_data(self) -> dict:
        url = "https://jaxel-inc.atlassian.net/rest/api/3/user/search"
        auth = HTTPBasicAuth("YOUR-LOGIN", "YOUR-TOKEN")

        headers = {
            "Accept": "application/json"
        }

        query = {
            'query': self.email
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=auth
        )

        return response
    
