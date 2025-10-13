from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import traceback

# Uncomment this if you have vector_db implemented
# from vector_db.vector_store import search_similar

app = FastAPI(title="GenAI COTS Parts Selector")

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class RecommendRequest(BaseModel):
    searchTerm: str

# Response model
class Part(BaseModel):
    partName: str
    score: float
    cost: float
    leadTime: int
    material: str
    sustainability: float
    rating: float
    simulation: Dict

# Dummy database (remove once real DB is ready)
DUMMY_PARTS = [
    {
        "partName": "Bearing A1",
        "score": 0.92,
        "cost": 25,
        "leadTime": 5,
        "material": "Stainless Steel",
        "sustainability": 0.8,
        "rating": 4.5,
        "simulation": {
            "predicted_max_stress": 12345,
            "uncertainty": 0.05,
            "verification_status": "ok"
        }
    },
    {
        "partName": "Bearing B2",
        "score": 0.88,
        "cost": 30,
        "leadTime": 7,
        "material": "Aluminum Alloy",
        "sustainability": 0.7,
        "rating": 4.2,
        "simulation": {
            "predicted_max_stress": 11500,
            "uncertainty": 0.07,
            "verification_status": "ok"
        }
    },
    {
        "partName": "Bearing C3",
        "score": 0.85,
        "cost": 28,
        "leadTime": 6,
        "material": "Carbon Steel",
        "sustainability": 0.6,
        "rating": 4.0,
        "simulation": {
            "predicted_max_stress": 11000,
            "uncertainty": 0.1,
            "verification_status": "ok"
        }
    }
]

@app.post("/api/v1/recommend")
def recommend(req: RecommendRequest):
    try:
        query = req.searchTerm
        print("🔍 Received query:", query)

        # Use this if you have a real semantic search
        # results = search_similar(query)

        # For now, return dummy recommendations
        results = DUMMY_PARTS
        print("✅ Returning results:", results)

        return {"recommendations": results}

    except Exception as e:
        print("❌ ERROR in /api/v1/recommend:", str(e))
        traceback.print_exc()
        return {"error": str(e)}



@app.get("/")
def root():
    return {"message": "Backend is running!"}
