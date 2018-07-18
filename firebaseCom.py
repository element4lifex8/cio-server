import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

def main():
	print "hello world"
	cred = credentials.Certificate('/home/jason/Documents/google/CIO-firebase-service-acct-key.json')
	default_app = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://check-in-out-lists.firebaseio.com/', \
			'databaseAuthVariableOverride' : { 'uid' : 'admin-server'} \
		})
	#user = auth.get_user('0CD7pHBp2BQYGysfjaP9o6XC0jk2')
	#print("fetched user: {0}" .format(user.uid)) 
	ref = db.reference('/users/0CD7pHBp2BQYGysfjaP9o6XC0jk2')
	print(ref.get())

if __name__ == "__main__":
	main()
