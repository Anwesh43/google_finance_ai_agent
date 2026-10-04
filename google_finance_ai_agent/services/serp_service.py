from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class SerpService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["SERP_BASE_URL"])

    def _handleError(self, e):
        print("Error", e)
        return {
            "message": str(e),
            "status": "Error"
        }
    
    def getTrendingStocks(self):
        try:
            qpParams = {
                "api_key": os.environ["SERP_API_KEY"],
                "engine": "google_finance_markets",
                "trend": "indexes"
            }
            response = self.client.getCall("search", qpParams = qpParams)
            resultObjects = {}
            if "markets" in response:
                markets = response["markets"]
                for k, markets in markets.items():
                    resultObjects[k] = []
                    for market in markets:
                        obj = {}
                        obj["stockId"] = market["stock"]
                        obj["name"] = market["name"]
                        obj["price"] = market["price"]
                        resultObjects[k].append(obj)
                return resultObjects

        except Exception as e:
            return self._handleError(e)

    def getStockDetails(self, stockId : str, duration : str = '1D'):
        try:
            qpParmas = {
                "api_key": os.environ["SERP_API_KEY"],
                "engine": "google_finance",
                "q": stockId,
                "window": duration
            }
            response = self.client.getCall("search", qpParams = qpParmas)
            return response["graph"] 
        except Exception as e:
            return self._handleError(e)

    def searchCompanyStocks(self, companyName : str):
        try:
            qpParams = {
                "engine": "google",
                "api_key": os.environ["SERP_API_KEY"],
                "q": f"{companyName} stock",
                "hl": "en",
                "gl": "us", 
                "location": "Austin, Texas, United States"
            }
            response = self.client.getCall("search", qpParams=qpParams)
            if "answer_box":
                return response["answer_box"]
        except Exception as e:
            return self._handleError(e)