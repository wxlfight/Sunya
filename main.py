import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# --- Configuration & Initialization ---
# Read Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase_client: Client | None = None

# Initialize Supabase client
if SUPABASE_URL and SUPABASE_SERVICE_KEY:
    try:
        supabase_client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
        print("Supabase client initialized successfully.")
    except Exception as e:
        print(f"ERROR: Failed to initialize Supabase client: {e}")
        # Depending on policy, might want to prevent app startup or just log
else:
    print("WARNING: SUPABASE_URL or SUPABASE_SERVICE_KEY environment variables not set. Supabase client not initialized.")


# --- FastAPI App Instance ---
app = FastAPI(
    title="Sunya API",
    description="API for the Sunya project, reflecting the 'Emptiness Self'.",
    version="0.1.0",
)

# --- API Endpoints ---
@app.get("/")
async def read_root():
    """Root endpoint providing a welcome message."""
    return {"message": "Welcome to the Sunya API - The 'Emptiness Self' Project"}

@app.get("/health/supabase")
async def health_check_supabase():
    """Checks if the Supabase client was initialized successfully."""
    if supabase_client:
        # For a more thorough check later, you could try a simple, non-destructive read,
        # like fetching schemas, but for now, just checking initialization is enough.
        # Example: try: supabase_client.table('some_table').select('id', head=True).limit(1).execute()
        return {"status": "ok", "message": "Supabase client appears to be initialized."}
    else:
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail="Supabase client is not initialized. Check environment variables (SUPABASE_URL, SUPABASE_SERVICE_KEY)."
        )

# Placeholder for future endpoints
# @app.get("/health")
# async def health_check_general():
#     return {"status": "ok"} 