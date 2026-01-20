from services.base_http_client import BaseHTTPClient, QueryParameterBuilder
import os 
from dotenv import load_dotenv 

load_dotenv()

class RecipeService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["FOOD_BASE_URL"])
        self.authClient = BaseHTTPClient(os.environ["OAUTH_BASE_URL"])
        self.authClient.authorize("connect/token", os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"])
    
    def searchRecipe(self, query : str):
        qpb = QueryParameterBuilder()
        qpb.addParameter("method", "recipes.search.v3").addParameter("format", "json").addParameter("search_expression", query)

        response = self.client.getCall(f"?{qpb.build()}", headers = {"Authorization": f"Bearer {self.authClient.accessToken}"})
        return response["recipes"]["recipe"]

recipeService = RecipeService()
if __name__ == "__main__":
    print(recipeService.searchRecipe("Chicken soup"))
