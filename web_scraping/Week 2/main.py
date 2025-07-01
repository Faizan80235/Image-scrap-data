# request send
import requests

# url
url=requests.get("https://www.microsoft.com/en-us/download/details.aspx?id=49117")
# get request for html content from this url
response=requests.get(url)
# html content scrap
html_content=response.text

print(html_content)