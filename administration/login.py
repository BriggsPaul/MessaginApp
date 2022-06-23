
# prompt user for username and password
#   this requires UI which we don't have -> just a script + command line for now
# encrypt both
# lookup username in the database
# compare passwords
# "login" -> how do I represent this?

from database import username_password_db, username_profile_db

def process_login_flow():
    username = input("Input username...")
    password = input("Input password...")

    if username not in username_password_db:
        print("Username was not found in database")
        exit()

    if username in username_password_db and username_password_db[username] == password:
        print("You have successfully logged in")
        return username_profile_db[username]

    elif username in username_password_db and username_password_db[username] != password:
        print("Incorrect password for username {user}".format(user=username))
        exit()

    exit()

    

if __name__ == "__main__":
    profile = process_login_flow() 
    print(profile)