# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tree_utils import get_tree_image_base64

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tree")
def generate_tree(n: int = 5):
    """Generate a random labeled tree and return its image as base64"""
    img_b64 = get_tree_image_base64(n)
    return {"n": n, "image": img_b64}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
