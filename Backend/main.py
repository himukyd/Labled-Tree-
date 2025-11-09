from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tree_utils import get_all_tree_images

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome! Use /all_trees?n=3"}

@app.get("/all_trees")
def all_trees(n: int = 3):
    """
    Return all distinct labeled trees for given n as images (base64)
    """
    if n > 6:
        return {"error": "Too large! n must be <= 6 (n^(n-2) grows fast)."}
    images = get_all_tree_images(n)
    return {"n": n, "count": len(images), "trees": images}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
