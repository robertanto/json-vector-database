from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from db_utils import JSONVectorSearch

app = FastAPI()
db = JSONVectorSearch()

class QueryIn(BaseModel):
    query: str
    n_results: int = 1

class AddIn(BaseModel):
    ids: List[str] 
    documents: List[dict]
    metadatas: Optional[List[dict]] = None

@app.post("/create")
def create_collection():
    db.clean()
    return {"detail": "Collection created"}

@app.post("/add") 
def add_documents(add_in: AddIn):
    db.add(add_in.ids, add_in.documents, add_in.metadatas)
    return {"detail": "Documents added"}

@app.post("/query")
def query(query_in: QueryIn):
    results = db.query_str(query_in.query, query_in.n_results)
    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    return results

@app.delete("/clean")
def clean():
    db.clean()
    return {"detail": "Collection deleted"}