import requests
from send_email import send_email

api_key = "0abe2ce74bcd4cb08462d65759082b2d"
url = (
    "https://newsapi.org/v2/everything?q=tesla&"
    "from=2023-07-02&sortBy=publishedAt&apiKey="
    "0abe2ce74bcd4cb08462d65759082b2d"
)
# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article's title and description
body = ""
i = 0

for article in content["articles"]:
    if i == 5:
        break
    else:
        if article["title"] is not None:
            body = body + article["title"] + ":'\n " + article["description"]
        i += 1

body = body.encode("utf-8")
send_email(body)
