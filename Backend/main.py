# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tree_utils import get_tree_image_base64

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for testing)
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Labeled Tree API! Use /tree?n=5"}

@app.get("/tree")
def generate_tree(n: int = 5):
    """Generate and return random labeled tree image"""
    img_b64 = get_tree_image_base64(n)
    return {"n": n, "image": img_b64}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
