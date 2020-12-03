import requests


class Method:
    def run_main(self, url, params, data, headers, method):

        if method == 'GET':
            response = requests.get(url=url, params=params, headers=headers).json()
            return response
        else:
            response = requests.post(url=url, data=data, headers=headers).json()
            return response







