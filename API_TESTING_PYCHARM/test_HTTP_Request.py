import requests

class TestClass:
    @staticmethod
    def test_get_api_request():
        req = requests.request('GET','https://httpbin.org/get')
        print(req.json())


    @staticmethod
    def test_get_api_requests():
        url = 'https://reqres.in/api/users?page=2'
        req = requests.get(url)
        print(req.json())

    @staticmethod
    def test_post_api_request():
        request_json={
            "name":"Aman",
            "job":"ABC"
        }
        header = {"Content-Type":"application/json"}
        res = requests.request("POST", "https://reqres.in/api/user",json=request_json,headers=header)
        print(res.json())

    import requests

# class TestClass:
#     def test_post_api_request(self):
#         url = 'https://httpbin.org/post'
#         data = {"name": "Aman", "email": "aman@example.com"}
#         res = requests.post(url, json=data)
#         assert res.status_code == 200, f"Expected status code 200, got {res.status_code}"
#         json_data = res.json()
#         response_json = json_data.get('json')
#         assert response_json is not None, "Response JSON does not contain 'json'"
#         assert response_json == data, f"Expected data {data}, but got {response_json}"
#         print(res.json())
#
#         # Assert Response Object
#         assert req.status_code == 200, "API call is failed"
#         assert pages==2, "Page size is wrong"
#         assert email=='aman@gmail.com', "Email is wrong"
#         print("Response assertion is passed")

    def test_post_api_request(self):
        request_json = {
            'name': "Aman",
            'job': 'SDET'
        }
        header = {'Content-Type': "application/json"}
        res = requests.request('POST', 'https://reqres.in/api/users', json=request_json, headers=header)
        response_json = res.json()
        print(res.json())
        if id in response_json:
            self.user_id = response_json['id']
            print(self.user_id, 'user id is ----------')
        else:
            print('id not available')
        # putting assertions
        assert res.status_code == 201, 'status code is 201 '



