from .base_request import BaseRequest


class Api(BaseRequest):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_data(self, endpoint, endpoint_id):
        return self.get(endpoint, endpoint_id)

    def put_data(self, endpoint, endpoint_id, data):
        return self.put(endpoint, endpoint_id, data, is_json=True, expected_error=False)

    def patch_data(self, endpoint, endpoint_id, data):
        return self.patch(endpoint,endpoint_id, data, is_json=True, expected_error=False)

    def delete_data(self, endpoint, endpoint_id):
        return self.delete(endpoint, endpoint_id)
