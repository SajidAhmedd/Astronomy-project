import requests
import send_email

api_key = "de3e58bae8a343e1b25e8ac49263f137"
url = "https://newsapi.org/v2/everything?q=tesla&"\
       "from=2026-04-13&sortBy=publishedAt&"\
       "apiKey=de3e58bae8a343e1b25e8ac49263f137"

request = requests.get(url)

content = request.json()

body = ""
for item in content["articles"]:
    body = body + item["title"] + "\n" + item["description"] + 2*"\n"

body = body.encode("utf-8")
send_email.send_email(message=body)