import json
import requests

x = 1
final_urls = []

while x < 11 :
    data=requests.get(f"https://api.generated.photos/api/v1/faces?page={x}&per_page=100", headers={"Authorization": "API-Key p704MyubUCdU5-eNeJdz8w"}).json()

    # Opening JSON file
    #f = open('try1.json')
    
    for y in data['faces'] :
        final_urls.append(y['urls'][-1]['512'])

    print('done with ', x)
    x = x+1

print(final_urls)


with open('fake.json', 'w') as f:
    json.dump(final_urls,f)