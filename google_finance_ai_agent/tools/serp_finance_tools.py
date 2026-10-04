from services.serp_service import SerpService 

serpService = SerpService()

def getTrendingStocks():
    print(f"Calling getTrendingStocks tool")
    return serpService.getTrendingStocks()

def getStockDetails(stockId : str, duration : str):
    print(f"Calling getStockDetails tool {stockId}")
    return serpService.getStockDetails(stockId=stockId, duration=duration)

def searchCompanyStocks(companyName : str):
    print(f"Calling searchCompanyStock tool {companyName}")
    return serpService.searchCompanyStocks(companyName=companyName)
