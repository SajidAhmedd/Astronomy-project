import requests
import send_email

topic = "tesla"

api_key = "de3e58bae8a343e1b25e8ac49263f137"

url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey=de3e58bae8a343e1b25e8ac49263f137&language=en"

request = requests.get(url)

content = request.json()


body = "Subject: hey\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body =  body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email.send_email(message=body)