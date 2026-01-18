from services.food_service import foodService

def getFoodItem(foodId : str):
    print("Calling getFoodItem tool")
    return foodService.getFoodItem(foodId=foodId)

def searchFoodName(query : str):
    print("Calling searchFoodName tool")
    return foodService.getSearch(query=query)
