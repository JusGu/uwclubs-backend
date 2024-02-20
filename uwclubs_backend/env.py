import os

def is_prod():
    return os.environ.get("uwclubs_env") == "prod"