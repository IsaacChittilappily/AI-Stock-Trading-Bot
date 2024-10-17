# function to get the html request data from a given url

def get_data(url: str) -> str:

    import requests

    r = requests.get(url)
    data = r.json()
    # make get a request and assign the returned data to a variable

    return data
