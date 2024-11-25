from vanna.remote import VannaDefault
import vanna.flask as vanna_flask
m_vn = VannaDefault(model='chinook', api_key='253e0c6afda74a15bcaa5e81e24e67ee')
#vn.connect_to_...() # Connect to your database here

#from vanna.flask import VannaFlaskApp
a = vanna_flask.VannaFlaskApp(vn=m_vn)
a.run()
