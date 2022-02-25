import functools
import xmlrpc.client
HOST = 'localhost'
PORT = 8069
DB = 'INFINITY_PLUS'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print ("Logged in as %s (uid:%d)" % (USER,uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('infinity_dp.session','search_read', [], ['name','seats'])
for session in sessions:
    print ("Session %s (%s seats)" % (session['name'], session['seats']))
    
'''    
# 3.create a new session
session_id = call('infinity_dp.course', 'search', {
    'name' : 'My session',
    'course_id' : 2,
})
'''
# 3.create a new session for the "Functional" course
course_id = call('infinity_dp.prueba1', 'search', [('name','ilike','Course 1')])[0]

session_id = call('infinity_dp.session', 'create', {
    'name' : 'Dorival Pichamba',
    'course_id' : course_id,
    'duration':12,
})
