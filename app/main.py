from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Practice API",
    description="FastAPI service designed for CI/CD pipeline practice and interviews",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "CI/CD practice application"}


@app.get("/health")
def health():
    return {"status": "healthy"}
