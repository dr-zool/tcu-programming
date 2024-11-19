# Import the requests library
import requests

# Define the URL for the ISS (International Space Station) location API
URL = "http://api.open-notify.org/iss-now.json"

# Send a GET request to the API and store the response
response = requests.get(URL)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    data = response.json()

    # Print the parsed data (ISS location details)
    print("ISS Location Data:")
    print(data)
else:
    print(
        f"Error: Failed to retrieve data. Status code: {response.status_code}")
