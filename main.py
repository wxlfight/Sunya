import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from supabase import create_client, Client
# Import the Garmin test function
from garmin_service import test_garmin_login

# Load environment variables from .env file
load_dotenv()

# --- Configuration & Initialization ---
# Read Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# Read Garmin credentials from environment variables
GARMIN_USERNAME = os.getenv("GARMIN_USERNAME")
GARMIN_PASSWORD = os.getenv("GARMIN_PASSWORD")

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

# Check if Garmin credentials are loaded
if not GARMIN_USERNAME or not GARMIN_PASSWORD:
    print("WARNING: GARMIN_USERNAME or GARMIN_PASSWORD environment variables not set.")
else:
    print("Garmin Username loaded from environment.") # Mask password


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

@app.get("/test/garmin-login")
async def test_garmin_login_endpoint():
    """Endpoint to test logging into Garmin Connect."""
    # Check if credentials were loaded correctly in main.py scope
    if not GARMIN_USERNAME or not GARMIN_PASSWORD:
        raise HTTPException(
            status_code=500, # Internal Server Error - Config issue
            detail="Server configuration error: Garmin credentials not loaded."
        )

    # Pass the loaded credentials to the service function
    result = await test_garmin_login(GARMIN_USERNAME, GARMIN_PASSWORD)
    if result["status"] == "error":
        raise HTTPException(
            status_code=401, # Unauthorized or specific error
            detail=result["message"]
        )
    return result

# Placeholder for future endpoints
# @app.get("/health")
# async def health_check_general():
#     return {"status": "ok"} 