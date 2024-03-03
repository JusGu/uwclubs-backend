from uwclubs_backend.consts.env import get_env
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = get_env('SUPABASE_URL')
SUPABASE_KEY = get_env('SUPABASE_KEY')