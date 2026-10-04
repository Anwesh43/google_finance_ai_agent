from tools.serp_finance_tools import getStockDetails, getTrendingStocks, searchCompanyStocks
from typing import Dict 
import json 

def writeFile(fileName : str, data: Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")


if __name__ == "__main__":
    writeFile("test_trending_stock.json", getTrendingStocks())
    writeFile("test_stock_details_aapl.json", getStockDetails("AAPL:NASDAQ", duration="1Y"))
    nvidiaResults = searchCompanyStocks("nvidia")

    writeFile("test_search_company.json", nvidiaResults)
    if "stock" in nvidiaResults and "exchange" in nvidiaResults:
        newStockId = f"{nvidiaResults["stock"]}:{nvidiaResults["exchange"]}"
        writeFile("test_stock_details_nvidia.json", getStockDetails(newStockId, "1M"))