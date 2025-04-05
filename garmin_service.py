import os
from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

# Remove reading env vars from module level
# GARMIN_USERNAME = os.getenv("GARMIN_USERNAME")
# GARMIN_PASSWORD = os.getenv("GARMIN_PASSWORD")

async def test_garmin_login(username: str | None, password: str | None):
    """Attempts to login to Garmin Connect using provided credentials."""
    # Check the passed arguments
    if not username or not password:
        return {"status": "error", "message": "Garmin username or password not provided to function."}

    try:
        print(f"Attempting Garmin login for user: {username}")
        # Initialize Garmin client with provided credentials
        client = Garmin(username, password)
        
        # Get display name as a simple test that login worked
        display_name = client.get_full_name()
        print(f"Garmin login successful. Display Name: {display_name}")
        return {"status": "ok", "message": f"Garmin login successful. Display Name: {display_name}"}

    except GarminConnectConnectionError as e:
        print(f"Garmin connection error: {e}")
        return {"status": "error", "message": f"Garmin connection error: {e}"}
    except GarminConnectAuthenticationError as e:
        print(f"Garmin authentication error: {e}")
        return {"status": "error", "message": f"Garmin authentication error: {e}"}
    except GarminConnectTooManyRequestsError as e:
        print(f"Garmin Rate Limit error: {e}")
        return {"status": "error", "message": f"Garmin Rate Limit error: {e}"}
    except Exception as e:
        print(f"An unexpected error occurred during Garmin login: {e}")
        return {"status": "error", "message": f"An unexpected error occurred: {e}"} 