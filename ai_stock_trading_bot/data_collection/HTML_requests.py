# function to get the html request data from a given url

def get_request(url: str) -> str:

    import requests

    # make a GET request and assign returned data to a variable
    r = requests.get(url)

    # check if request was successful (status code 200)
    if r.status_code != 200:
        raise Exception(f"API request failed with status code: {r.status_code}")

    # check if response contains error message
    if "Error Message" in r.text:
        raise Exception(f"API returned error: {r.json()['Error Message']}")
    
    data = r.json()

    return data
