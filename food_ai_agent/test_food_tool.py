import time 
from tools.food_tools import getFoodItem, searchFoodName

response = searchFoodName("paneer")
print(response)
time.sleep(1)
print("Getting food items++++++++++++++++++")

for item in response:
    time.sleep(1)
    print(f"Getting details for {item["name"]}")
    print(getFoodItem(item["id"]))
