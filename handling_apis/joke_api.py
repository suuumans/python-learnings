
import requests

def fetch_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        joke_data = data['data']
        catagory = joke_data["categories"]
        joke = joke_data["content"]
        return catagory,joke
    else:
        raise Exception("Failed to fetch joke data")

def main():
    try:
        catagory, joke = fetch_joke()
        print(f"Catagory: {catagory} \n Joke: {joke}")
    except Exception as e:
        print(f"Error: {e}")
        

if __name__ == "__main__":
    main()


# if this file don't run, then try installing "requests" library by typing "pip install requests" for windows
# or "pip3 install requests" (for linux & unix or mac) in the terminal. Then run this file.