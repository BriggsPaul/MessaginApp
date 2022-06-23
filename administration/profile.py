from roles import role_list

#SOLID DESIGN PRINCIPLES
#If changes need to be made to this profile, it should only impact the entity that uses it directly ~~sort of~~

class Profile:
    def __init__(self, username, password=1234):
        self.username = username
        self.password = password
        pass

    def get_profile_picture():
        pass

    def get_user_role():
        pass

    def get_user_settings():
        pass

    def is_authenticated():
        pass
    
    def get_friend_list():
        pass

class ProfileFactory:
    # Class setup to be a profile factory (is this good for structure or nah who knows?)
    def __init__(self, username):
        return Profile(username)
        
    def create_new_account(self, username, password):
        return Profile(username, password)


