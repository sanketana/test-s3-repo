import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("tkaddressbook-fda5f-firebase-adminsdk-e0jvd-7016f0595f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://tkaddressbook-fda5f/firebaseio.com"
})

input_json = """{
	{
		"name": "Jaivant Cherukuri",
		"email": "jaivant@gmail.com",
		"year": 2010
	},

	{
		"name": "Krethick",
		"email": "krethick@gmail.com",
		"year": 2008
	}
}"""	



ref = db.reference("/")
#ref.set(input_json)