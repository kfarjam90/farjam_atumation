import requests

def joke():
    """
    Fetches a random joke from the JokeAPI and prints it to the console

    Raises:
        None

    Returns:
        None
    """
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['type'] == 'single':
            print(data['joke'])
        if data['type'] == 'twopart':
            print(f"{data['setup']}\n{data['delivery']}")

    elif response.status_code == 401:
        print("API key is missing or invalid")
    elif response.status_code == 404:
        print("not found")
    else:
        print("Failed to fetch joke")

joke()