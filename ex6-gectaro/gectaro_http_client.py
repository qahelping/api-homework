import requests
from datetime import datetime
from models import PostResourceRequests, PostProjectTaskResource
from typing import Union


class GectaroHttpClient:
    def __init__(self, base_url, token, project_id="85880"):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.base_url = base_url
        self.project_id = project_id

    def get_projects_resource_requests(self):
        response = self.session.get(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests"
        )
        return response

    def get_projects_resource_requests_id(self, request_id):
        response = self.session.get(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{request_id}"
        )
        return response

    def post_projects_resources(self, json_data: PostProjectTaskResource):
        response = self.session.post(
            f"{self.base_url}/v1/projects/{self.project_id}/resources",
            json=json_data.model_dump(),
        )
        return response

    def post_projects_resource_requests(self, data: Union[dict, PostResourceRequests]):
        # data может быть либо dict, либо моделью ProjectTaskRequestBody
        response = self.session.post(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests",
            # если data - это dict, не меняем,
            # а если модель - то конвертируем в словарь
            # с помощью .model_dump()
            json=data if isinstance(data, dict) else data.model_dump(),
        )

        return response

    def put_projects_resource_requests(
        self, request_id, data: Union[dict, PostResourceRequests]
    ):
        # data может быть либо dict, либо моделью ProjectTaskRequestBody
        response = self.session.put(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{request_id}",
            # если data - это dict, не меняем,
            # а если модель - то конвертируем в словарь
            # с помощью .model_dump()
            json=data if isinstance(data, dict) else data.model_dump(),
        )

        return response

    def delete_projects_resource_requests(self, request_id):
        response = self.session.delete(
            f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{request_id}"
        )

        return response

    def get_companies(self):
        response = self.session.get(f"{self.base_url}/v1/companies")
        return response

    def get_company_resource_requests(self, company_id):
        response = self.session.get(
            f"{self.base_url}/v1/companies/{company_id}/resource-requests"
        )
        return response
