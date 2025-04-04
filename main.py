from fastapi import FastAPI

app = FastAPI(
    title="Sunya API",
    description="API for the Sunya project, reflecting the 'Emptiness Self'.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    """Root endpoint providing a welcome message."""
    return {"message": "Welcome to the Sunya API - The 'Emptiness Self' Project"}

# Placeholder for future endpoints
# @app.get("/health")
# async def health_check():
#     return {"status": "ok"} 