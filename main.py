import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration --- M
# Read Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# Basic check to see if the variables are loaded (optional: can be removed later)
if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    print("WARNING: SUPABASE_URL or SUPABASE_SERVICE_KEY environment variables not set.")
    # Depending on the setup, you might want to raise an error here
    # raise ValueError("Supabase credentials must be set in environment variables or .env file")
else:
    print("Supabase URL and Service Key loaded from environment.") # For debug, remove later


# --- FastAPI App Instance --- M
app = FastAPI(
    title="Sunya API",
    description="API for the Sunya project, reflecting the 'Emptiness Self'.",
    version="0.1.0",
)

# --- API Endpoints --- M
@app.get("/")
async def read_root():
    """Root endpoint providing a welcome message."""
    return {"message": "Welcome to the Sunya API - The 'Emptiness Self' Project"}

# Placeholder for future endpoints
# @app.get("/health")
# async def health_check():
#     return {"status": "ok"}

# Example of how you might initialize the Supabase client later:
# from supabase import create_client, Client
# if SUPABASE_URL and SUPABASE_SERVICE_KEY:
#     supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
# else:
#     supabase = None # Or handle the error appropriately 