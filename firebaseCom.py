import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

def main():
    cred = credentials.Certificate('/home/jason/Documents/google/CIO-firebase-service-acct-key.json')
    default_app = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://check-in-out-lists.firebaseio.com/', \
                    'databaseAuthVariableOverride' : { 'uid' : 'admin-server'} \
            })
    #user = auth.get_user('0CD7pHBp2BQYGysfjaP9o6XC0jk2')
    #print("fetched user: {0}" .format(user.uid))
    #ref = db.reference('/users/0CD7pHBp2BQYGysfjaP9o6XC0jk2')
    #ref = db.reference('/users')
    #follower_snap = ref.order_by_key().equal_to('xEeMnQmrAoNbeCLVD8Fcqw8yQan1').get()

    #	userRef = db.reference('/users')
    #	#Alphabetically return users by their email
    #	userSnap = userRef.order_by_child('email').get()
    #	print("Searching for me\n")
    #	for key, value in userSnap.items():
    #		#if(value == "element4lifex8@yahoo.com"):
    #		print(key)

    fuser = Fuser()
    #start reading from begining of users
    data_tree = fuser.user_snap_tree("")
    i=0;
    while(i<2):
        i+=1
        #search for first user then call user snap tree to get the next two
        count = 0
        for user,tree in data_tree:
            if(count == 0):
                #Collect a list of all the user id's that follow the current user 
                #print("COUNT FORMAT: {0}, {1}" .format(user, tree))
                followers = fuser.find_followers(user) 
            else:
                #get next 2 users to loop over
                data_tree = fuser.user_snap_tree(user)
            
            count += 1
            
class Fuser():
    def __init__(self):
        self.userId = ""
        self.userTree = {}

    #Take the user name and search for it in all other user's friends
    def find_followers(self, user):
        #get the current user's followers by returning every other user for their with their id in friends list
	#currUserRef = db.reference('/users').child(user)
	#return dict of all users by their email, this would require an index on rule for email for every user
        #friendSnap = currUserRef.order_by_child('email').get()

        #get all users
	userRef = db.reference('/users')
        #may need to user order by value to get the friend's value
        #Retieve all the users in the data base who have the current user listed in their friends list

        #right now the first user's ordered by key would be with value "true", last would be alphabetical maybs?
        follower_snap = userRef.order_by_child('friends').limit_to_first(3).get()
        #follower_snap = userRef.order_by_child('friends').equal_to('xEeMnQmrAoNbeCLVD8Fcqw8yQan1').get()

        print("finding followers")
	for key in follower_snap.items():
            #add here a writie of all the followers id's to the current user
            print("find: {0}" .format(key))
    
    def user_snap_tree(self, thisUser):
	#userRef = db.reference('/users/xBDl2rqFmwU3QcETKMtb8MFM3d43')
	userRef = db.reference('/users/')
        #Get 2 users at a time to search for their friends
        if(thisUser == ""): 
            tree =  userRef.order_by_key().limit_to_first(2).get()
        else:
            tree =  userRef.order_by_key().start_at(thisUser).limit_to_first(2).get()
        #return userRef.get().items()
        #tree = userRef.child('friends/7YXLNW9vH0h3UC26Lg5dAjtVrCj1').get() 
        return tree.items()
    
if __name__ == "__main__":
	main()
