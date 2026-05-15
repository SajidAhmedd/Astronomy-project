import requests
import send_email

topic = "tesla"

api_key = "de3e58bae8a343e1b25e8ac49263f137"

url = "https://newsapi.org/v2/everything?q=tesla&from=2026-04-13&sortBy=publishedAt&apiKey=de3e58bae8a343e1b25e8ac49263f137"

request = requests.get(url)

content = request.json()


body = ""
for article in content["articles"][:20]:
        if article["title"] is not None:
            body = "Subject: hey" \
                   + "\n" + body + article["title"] + "\n" \
                   + article["description"] \
                   + "\n" + article["url"] + 2*"\n"

        body = body.encode("utf-8")
        send_email.send_email(message=body)