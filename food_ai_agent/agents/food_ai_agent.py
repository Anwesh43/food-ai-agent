from pydantic_ai import Agent 
from tools.food_tools import getFoodItem, searchFoodName, searchRecipe
from prompts.food_system_prompt import SYSTEM_PROMPT

agent = Agent(
    model="ollama:qwen3:8b",
    tools = [getFoodItem, searchFoodName, searchRecipe],
    system_prompt = SYSTEM_PROMPT
)

async def streamFoodAnalysis(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end="")

