import requests

def fetch_current_rate():
    """Fetch current NGN to USD rate from a free API"""
    url = "https://api.exchangerate-api.com/v4/latest/NGN"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        usd_rate = data['rates']['USD']
        print(f"1 NGN = ${usd_rate:.6f} USD")
        print(f"$1 USD = ₦{1/usd_rate:.2f} NGN")
        
        return data
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    fetch_current_rate()