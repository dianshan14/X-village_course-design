import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

# check the type of response body
print(type(response.text))

# requirement 1
with open('music_show.json', 'w') as f:
    f.write(response.text)

# requirement 2
with open('music_show.txt', 'w') as f:
    # Because type of body is string, you should use `json.loads` instead of `json.load`
    json_body = json.loads(response.text)
    for show in json_body:
        f.write(show['title'] + ' : ' + show['startDate'] + ' ~ ' + show['endDate'] + '\n')
