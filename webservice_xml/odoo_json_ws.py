import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'INFINITY_PLUS'
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode("utf-8"), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new note
args = {
    'name': 'Estefania',
    'course_id': 8,
}
note_id = call(url, "object", "execute", DB, uid, PASS, 'infinity_dp.session', 'create', args)