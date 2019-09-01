import json
from collections import defaultdict
from pprint import pprint

import requests


url = 'https://data.kingcounty.gov/resource/f29f-zza5.json'

def call_api(offset):
    r = requests.get(
        url,
        params = {
            '$where': "inspection_date>='2019-01-01T00:00:00.000'",
            '$limit': 1000,
            '$offset': offset,
            '$order': ':id'
        },
    )
    assert r.status_code == 200, r.json()
    return r.json()


grades = defaultdict(list)
violation_points = defaultdict(list)
inspection_scores = defaultdict(list)

offset = 0
data = call_api(offset)
while len(data) > 0:
    print(offset)

    for item in data:
        zip_code = item.get('zip_code')
        grade = item.get('grade')
        points = item.get('violation_points')
        inspection_score = item.get('inspection_score')

        if zip_code:
            if grade:
                grades[zip_code].append(int(grade))
            if points:
                violation_points[zip_code].append(int(points))
            if inspection_score:
                inspection_scores[zip_code].append(int(inspection_score))

    offset += 1000
    data = call_api(offset)

data = {
    'grades': {x: {'score': sum(y) / len(y), 'len': len(y)} for x, y in grades.items()},
    'violation_points': {x: {'score': sum(y) / len(y), 'len': len(y)} for x, y in violation_points.items()},
    'inspection_scores': {x: {'score': sum(y) / len(y), 'len': len(y)} for x, y in inspection_scores.items()},
}

# pprint(data)

json.dump(data, open('./app/static/data/ratings.json', 'w'))
