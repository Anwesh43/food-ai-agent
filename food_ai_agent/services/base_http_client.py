import requests 
from typing import Dict 
import time 
class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL
        self.accessToken = ""
        # self._authorize(authorizationEndpoint, clientId = clientId, clientSecret = clientSecret)

    def authorize(self, endpoint: str, clientId : str, clientSecret: str):
        if not(self.accessToken == ""):
            return self.accessToken
        data = {
            "grant_type": "client_credentials",
            "scope": "basic"
        }
        response = requests.post(f"{self.baseURL}/{endpoint}", auth=(clientId, clientSecret), data = data)
        resJson = response.json()
        print("RES_JSON", resJson)
        self.accessToken = resJson["access_token"]
        return self.accessToken 

    def getCall(self, endpoint: str, headers: Dict):
        print(f"Calling {self.baseURL}/{endpoint}")
        response = requests.get(f"{self.baseURL}/{endpoint}", headers=headers)
        return response.json()
        

class QueryParameterBuilder:
    def __init__(self):
        self.queryMap = {}

    def addParameter(self, key : str,  value : str):
        self.queryMap[key] = value 
        return self 
    
    def build(self) -> str:
        qvValues = []
        for k, v in self.queryMap.items():
            qvValues.append(f"{k}={v}")
        return "&".join(qvValues)


    