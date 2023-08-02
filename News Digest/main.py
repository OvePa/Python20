import requests

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
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
