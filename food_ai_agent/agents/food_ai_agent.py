from pydantic_ai import Agent 
from tools.food_tools import getFoodItem, searchFoodName

agent = Agent(
    model="ollama:qwen3:8b",
    tools = [getFoodItem, searchFoodName],
    system_prompt = "analyse food and the nutrients in it"
)

async def streamFoodAnalysis(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end="")
            
