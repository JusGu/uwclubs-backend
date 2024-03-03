from uwclubs_backend.database.provider import get_supabase_client
from supabase import Client

supabase: Client = get_supabase_client()

def select_events(guild_id: str):
    response = supabase.table("events").select("*").eq("guild_id", guild_id).is_("deleted_at", "NULL").execute()
    return response