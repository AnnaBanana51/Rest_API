#store data to dict
#define a route like user = post that is going to create a new record for a student
#define a route student ID - paramter (google flask root parameters)
#2 methods that the root accepts, get - info about the student, delete - delete

from flask import Flask, request, jsonify

app = Flask(__name__)

d = {}

@app.route('/', methods=['GET'])
def get_records():
    return jsonify(d)

@app.route('/', methods=['POST'])
def create_record():
    added = {}
    for k,v in request.args.items():
        if not k in d.keys():
            added[k] = v
            d[k] = v
    return jsonify({"added": added, "current": d})

@app.route('/', methods=['DELETE'])
def delete_record():
    deleted = {}
    for k,v in request.args.items():
        try:
            d.pop(k)
            deleted[k] = v
        except:
            continue
    return jsonify({"deleted": deleted, "current": d})
                
if __name__ == '__main__':
    app.run(debug=True)