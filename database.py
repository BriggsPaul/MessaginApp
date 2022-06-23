from profile import Profile

username_password_db = {
    "paul": "1234",
    "admin": "abcd",
    "rich": "password"
}


username_profile_db = {
    "paul": Profile("paul"),
    "admin": Profile("admin"),
    "rich": Profile("rich")
}


def call_function_that_returns_db_object():
    print("find library that does this")
    return None

database = call_function_that_returns_db_object()