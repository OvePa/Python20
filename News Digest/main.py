import requests
from send_email import send_email

topic = "tesla"
api_key = "0abe2ce74bcd4cb08462d65759082b2d"
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}&from=2023-07-02&"
    "sortBy=publishedAt&"
    "apiKey=0abe2ce74bcd4cb08462d65759082b2d&"
    "language=en"
)

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article's title and description
body = ""
for article in content["articles"][:5]:
    if article["title"] is not None:
        body = (
            "Subject: Today's news"
            + "\n\n"
            + body
            + article["title"]
            + "\n"
            + article["description"]
            + "\n"
            + article["url"]
            + "\n"
        )


body = body.encode("utf-8")
send_email(body)
