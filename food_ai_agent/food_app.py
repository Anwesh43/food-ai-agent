from agents.food_ai_agent import streamFoodAnalysis
import sys 
import asyncio
if __name__ == "__main__" and len(sys.argv) > 1:
    asyncio.run(streamFoodAnalysis(" ".join(sys.argv[1:])))

    