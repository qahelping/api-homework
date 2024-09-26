import requests


class GectaroHttpClient:
    def __init__(self, token, base_url, project_id=85781, company_id=19047):
        self.session = requests.Session()
        self.session.headers['Authorization'] = f"Bearer {token}"
        self.base_url = base_url
        self.project_id = project_id
        self.company_id = company_id

    def set_project_id(self, new_project_id):
        self.project_id = new_project_id

    def get_projects_resource_requests(self):
        response = self.session.get(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests")
        return response

    def get_projects_resource_request_by_id(self, resource_request_id):
        response = self.session.get(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests"
                                    f"/{resource_request_id}")
        return response

    def post_projects_resource(self, data):
        response = self.session.post(f"{self.base_url}/v1/projects/{self.project_id}/resources",
                                     json=data)
        return response

    def post_projects_resource_request(self, data):
        response = self.session.post(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests",
                                     json=data)
        return response

    def delete_projects_resource(self, resource_id):
        response = self.session.delete(f"{self.base_url}/v1/projects/{self.project_id}/resources/{resource_id}")
        return response

    def put_projects_resource_request(self, resource_request_id, data):
        response = self.session.put(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests"
                                    f"/{resource_request_id}",
                                    json=data)
        return response

    def post_projects_orders(self, data):
        response = self.session.post(f"{self.base_url}/v1/projects/{self.project_id}/orders",
                                     json=data)
        return response

    def get_companies_contractors(self):
        response = self.session.get(f"{self.base_url}/v1/companies/{self.company_id}/contractors")
        return response

    def get_companies_stocks(self):
        response = self.session.get(f"{self.base_url}/v1/companies/{self.company_id}/stocks")
        return response

    def delete_companies_orders(self, order_id):
        response = self.session.delete(f"{self.base_url}/v1/projects/{self.project_id}/orders/{order_id}")
        return response

    def delete_projects_resource_request(self, resource_request_id):
        response = self.session.delete((f"{self.base_url}/v1/projects/{self.project_id}/resource-requests"
                                        f"/{resource_request_id}"))
        return response

    def get_companies_resource_request(self):
        response = self.session.get(f"{self.base_url}/v1/companies/{self.company_id}/resource-requests")
        return response
