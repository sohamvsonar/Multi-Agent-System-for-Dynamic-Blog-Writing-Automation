# filename: get_nvidia_stock_price.py
import requests

def get_nvidia_stock_price():
    url = "https://finnhub.io/api/v1/quote"
    parameters = {
        'symbol': 'NVDA',
        'token': 'YOUR_API_KEY'  
    }
    
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        data = response.json()
        return data['c']  # Current price
    else:
        return None

current_price = get_nvidia_stock_price()

if current_price:
    print(f"Current Nvidia (NVDA) stock price: ${current_price:.2f}")
else:
    print("Failed to retrieve the stock price.")