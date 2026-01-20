from services.food_service import foodService
from services.recipe_service import recipeService

def getFoodItem(foodId : str):
    print(f"Calling getFoodItem tool with args {foodId}")
    return foodService.getFoodItem(foodId=foodId)

def searchFoodName(query : str):
    print(f"Calling searchFoodName tool with {query}")
    return foodService.getSearch(query=query)

def searchRecipe(foodName : str):
    print(f"Calling searchRecipe tool with args {foodName}")
