from services.base_http_client import BaseHTTPClient, QueryParameterBuilder
import os 
from dotenv import load_dotenv 

load_dotenv()

class FoodService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["FOOD_BASE_URL"])
        self.authClient = BaseHTTPClient(os.environ["OAUTH_BASE_URL"])
        self.accessToken = self.authClient.authorize("connect/token", os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"])
    
    def getSearch(self, query : str):
        queryParameterBuilder = QueryParameterBuilder()
        queryParameterBuilder.addParameter("method", "foods.search").addParameter("search_expression", query)
        queryParameterBuilder.addParameter("format", "json").addParameter("include_sub_categories", "true")
        queryParameterBuilder.addParameter("flag_default_serving", "true").addParameter("include_food_attributes", "true")
        queryParameterBuilder.addParameter("max_results", "10").addParameter("language", "en").addParameter("page_number", "0")
        queryStr = queryParameterBuilder.build()
        endpoint = f"?{queryStr}"
        data = self.client.getCall(endpoint, {"Authorization": f"Bearer {self.accessToken}"})
        result = []
        for food in data["foods"]["food"]:
            foodItem = {}
            foodItem["id"] = food["food_id"]
            foodItem["name"] = food["food_name"]
            result.append(foodItem)
        return result 
    
    def getFoodItem(self, foodId : str):
        queryParameterBuilder = QueryParameterBuilder()
        queryParameterBuilder.addParameter("method", "food.get.v5").addParameter("food_id", foodId).addParameter("format", "json")
        queryStr = queryParameterBuilder.build()
        endpoint = f"?{queryStr}"
        data = self.client.getCall(endpoint, {"Authorization": f"Bearer {self.accessToken}"})
        if len(data["food"]["servings"]["serving"]) == 0:
            return {}
        serving = data["food"]["servings"]["serving"][0]
        return serving 
    

foodService = FoodService()