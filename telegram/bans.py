import os
import json

from config import banned_users_db_path


def __update_database():
    with open(banned_users_db_path, "w") as saving_file:
        json.dump(banned_users, saving_file)

def ban_user_id(user_id: int):
    banned_users.append(user_id)
    __update_database()


def unban_user_id(user_id: int):
    banned_users.remove(user_id)
    __update_database()


def is_banned(user_id: int):
    return user_id in banned_users


banned_users = []
if os.path.exists(banned_users_db_path):
    with open(banned_users_db_path, "r") as json_file:
        banned_users = json.load(json_file)
