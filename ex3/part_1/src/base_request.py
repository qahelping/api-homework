import requests


class BaseRequest:

    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(
            self, url, request_type, payload=None, is_json=False,
            expected_error=False
    ):
        print(f'Request to: {url}')
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST' or 'PUT' or 'PATCH':
                if is_json:
                    response = requests.post(url, json=payload)
                else:
                    response = requests.post(url, data=payload)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        # log part
        print(f'{request_type} example')
        print(response.url)
        print(response.status_code)
        print(response.reason)
        print(response.text)
        print(response.json())
        print('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        if endpoint_id is None:
            url = f'{self.base_url}/{endpoint}'
        else:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response

    def post(
            self, endpoint, endpoint_id, body, is_json=False,
            expected_error=False
    ):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(
            url, 'POST', payload=body, is_json=is_json,
            expected_error=expected_error
        )
        return response.json()['message']

    def put(
            self, endpoint, endpoint_id, body, is_json=False,
            expected_error=False
    ):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(
            url, 'PUT', payload=body, is_json=is_json,
            expected_error=expected_error
        )
        return response.json()['message']

    def patch(
            self, endpoint, endpoint_id, body, is_json=True,
            expected_error=False
    ):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(
            url, 'PATCH', payload=body, is_json=is_json,
            expected_error=expected_error
        )
        return response.json()['message']

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']
