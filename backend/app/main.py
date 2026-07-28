from fastapi import FastAPI
app = FastAPI()

@app.get("/user")
def get_user():
    return {"message": "AI E - CommerceAPI", "status": "success" , "version": "1.0.0"} 