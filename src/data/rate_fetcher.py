import requests
from datetime import datetime

class RateFetcher:
    """Base class for fetching exchange rates"""
    
    def __init__(self, base_currency="NGN"):
        self.base_currency = base_currency
        self.last_fetch_time = None
        self.current_rates = {}
    
    def fetch_rates(self):
        """Override in subclass"""
        raise NotImplementedError
    
    def get_rate(self, target_currency):
        """Get rate for specific currency"""
        return self.current_rates.get(target_currency)


class APIRateFetcher(RateFetcher):
    """Fetches rates from ExchangeRate-API"""
    
    def __init__(self):
        super().__init__()
        self.api_url = "https://api.exchangerate-api.com/v4/latest/NGN"
    
    def fetch_rates(self):
        """Fetch current rates"""
        response = requests.get(self.api_url)
        data = response.json()
        
        self.current_rates = data['rates']
        self.last_fetch_time = datetime.now()
        
        return self.current_rates
    
    def display_major_currencies(self):
        """Show USD, GBP, EUR rates"""
        if not self.current_rates:
            self.fetch_rates()
        
        for currency in ['USD', 'GBP', 'EUR']:
            rate = self.current_rates[currency]
            print(f"1 NGN = {rate:.6f} {currency}")
            print(f"1 {currency} = ₦{1/rate:.2f} NGN\n")


# Test
if __name__ == "__main__":
    fetcher = APIRateFetcher()
    fetcher.display_major_currencies()