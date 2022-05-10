import json
import requests

x = 1
final_urls = []

while len(final_urls) < 1000 :
    data=requests.get(f"https://api.unsplash.com/search/photos?query=portrait%20headshot%20human&client_id=C3kCVQd176QdBI_BxdDl1P4AdqJlBOLwOt4GuuiIRGc&per_page=1000&orientation=squarish&page={x}").json()

    # Opening JSON file
    #f = open('try1.json')

    for y in data['results'] :
        final_urls.append(y['urls']['full'])
    
    print('done with ', x)
    x = x+1
print(len(final_urls))

with open('unsplash.json', 'w') as f:
    json.dump(final_urls,f)
