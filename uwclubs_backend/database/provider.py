from supabase import create_client, Client
from uwclubs_backend.consts.secrets import SUPABASE_URL, SUPABASE_KEY

supabase_client: Client = None

def get_supabase_client():
    global supabase_client
    if not supabase_client:
        supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase_client