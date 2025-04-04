
import requests

def fetch_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        quote_data = data['data']
        quote = quote_data["content"]
        author = quote_data["author"]
        return quote, author
    else:
        raise Exception("Failed to fetch quote data")

if __name__ == "__main__":
    try:
        quote, author = fetch_quote()
        print(f"Quote: {quote} \n Author: {author}")
    except Exception as e:
        print(f"Error: {e}")