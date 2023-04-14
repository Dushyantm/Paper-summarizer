from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import datetime
from fastapi.responses import JSONResponse


# Assuming you have a function to search for papers in one of your existing Python files
# For example, if you have a function called "search_papers(query)" in the "main.py" file
from main import search_papers

app = FastAPI()



class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        return super(CustomJSONEncoder, self).default(obj)
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
async def search(query: str, max_results: int = 10):
    papers = search_papers(query, max_results)
    json_data = json.dumps(papers, cls=CustomJSONEncoder)  # Use the custom JSON encoder
    return JSONResponse(content=json.loads(json_data))
