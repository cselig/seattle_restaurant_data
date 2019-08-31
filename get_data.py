import requests
from pprint import pprint
from collections import defaultdict

r = requests.get("https://data.kingcounty.gov/resource/f29f-zza5.json?$where=inspection_date >= '2019-01-01T00:00:00.000'")
assert r.status_code == 200

data = r.json()
pprint(data[:5])

ratings = defaultdict(list)

for item in data:
    zip_code = item.get('zip_code')
    grade = item.get('grade')
    if zip_code and grade:
        ratings[zip_code].append(int(grade))

pprint({x: (sum(y) / len(y), len(y)) for x, y in ratings.items()})
pprint({x: sum(y) / len(y) for x, y in ratings.items()})
