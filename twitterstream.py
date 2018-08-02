import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = "DhuY0SqOoPJ6MMhjI70tZ06UM"
api_secret = "cMlO7DC2ClD9tkuCpRvl6sT7DfWAwutXj1YzATulOrZLCeDIiC"
access_token_key = "118002838-TjJSwtXwuuL425qX5PNi2BIlEzA07hmbsHqCpYbP"
access_token_secret = "0EglvUENdexE0I6qYizgqIeeHF8BcrWnh8GXi1DUvEsgG"

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('output.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
