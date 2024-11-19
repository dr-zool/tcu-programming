from lxml import etree
import requests

weather_url = "https://weather.com/en-BZ/weather/today/l/db7a1f2416ccaaa8536b92cdb14a40bca64d8720ca08e793df87ab065fc0cbfc"

response = requests.get(weather_url)

if response.status_code == 200:
    dom = etree.HTML(response.text)
    elements = dom.xpath(
        "//span[@data-testid='TemperatureValue' and contains(@class,'CurrentConditions')]")

    if elements:
        temperature = elements[0].text
        print(f"The current temperature in Tokyo Prefecture is: {temperature}")
    else:
        print("Temperature element not found.")
else:
    print("Failed to fetch the webpage.")
