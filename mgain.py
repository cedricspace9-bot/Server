from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is live and running!"}

# Add your webhook/forwarding logic here
