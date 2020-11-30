import requests
import json
# r = requests.get("http://127.0.0.1:5000/")
# json_resp = json.loads(r.text)
# json_resp

students = {"student1":"Anna Levy", "spec1":"Data Science", "student2":"Amy Rosa", "spec2":"Data Science", \
    "student3":"Bryant Novas", "spec3":"Data Science", "student4":"Clariza Mayo", "spec4":"Data Science"}
headers = {"Content-Type": "application/json"}
r = requests.post("http://127.0.0.1:5000/", params=students, headers=headers)
json_resp = json.loads(r.text)
json_resp

student = {"student3":"Bryant Novas"}
headers = {"Content-Type": "application/json"}
r = requests.delete("http://127.0.0.1:5000/", params=student, headers=headers)
json_resp = json.loads(r.text)
json_resp