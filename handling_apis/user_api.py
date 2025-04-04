
import requests

def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        username = user_data["login"]["username"]
        country = user_data['location']["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        username, country = fetch_user()
        print(f"Username: {username} \n Country: {country}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


# if this file don't run, then try installing "requests" library by typing "pip install requests" for windows
# or "pip3 install requests" (for linux & unix or mac) in the terminal. Then run this file.