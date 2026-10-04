from tools.serp_finance_tools import getStockDetails, getTrendingStocks, searchCompanyStocks, writeHTML
from prompts.finance_system_prompt import SYSTEM_PROMPT
from pydantic_ai import Agent 
from dotenv import load_dotenv 

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2', 
    tools = [getStockDetails, getTrendingStocks, searchCompanyStocks, writeHTML],
    system_prompt = SYSTEM_PROMPT
)

async def analyseUSStocks(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')