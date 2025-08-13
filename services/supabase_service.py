import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_TABELA = os.getenv("SUPABASE_TABELA", "Contacts")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    res = supabase.table(SUPABASE_TABELA).select("*").execute()
    if res.data is None:
        return []
    return res.data


