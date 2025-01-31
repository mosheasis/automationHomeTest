# we can store test data in this module like users
users = [
    {"name": "standard_user", "password": "secret_sauce"},
    {"name": "locked_out_user", "password": "secret_sauce"},
    {"name": "performance_glitch_user", "password": "secret_sauce"},
    {"name": "error_user", "password": "secret_sauce"},
    {"name": "error_user", "password": "secret_sauce"},
    {"name": "visual_user", "password": "secret_sauce"},
]


def get_user():
    return users[0].get("name")


def get_password():
    return users[0].get("password")
