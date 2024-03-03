import os
def get_env(param_name: str):
    prod = is_prod()
    env_param_name = 'PROD_' + param_name if prod else 'DEV_' + param_name
    var_from_env = os.getenv(env_param_name)
    return var_from_env

def is_prod():
    return os.environ.get("uwclubs_env") == "prod"