import requests
from config import URL, LOGIN, PASSWORD, COMPANY_ID


class YougileApi:
    def __init__(self):
        self.url = URL
        self.token = self._get_token()

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def _get_token(self):
        creds = {
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": COMPANY_ID
        }
        resp = requests.post(f"{self.url}/auth/keys", json=creds)
        resp.raise_for_status()

        data = resp.json()
        return data.get("key") or data.get("token")

    def create_project(self, title: str):
        payload = {"title": title}
        return requests.post(f"{self.url}/projects", json=payload,
                             headers=self.headers)

    def get_project(self, project_id: str):
        return requests.get(f"{self.url}/projects/{project_id}",
                            headers=self.headers)

    def update_project(self, project_id: str, new_title: str):
        payload = {"title": new_title}
        return requests.put(f"{self.url}/projects/{project_id}", json=payload,
                            headers=self.headers)
