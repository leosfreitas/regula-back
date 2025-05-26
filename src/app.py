from fastapi import FastAPI
from mongoengine import connect
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
import dotenv
from importlib import import_module

dotenv.load_dotenv()

connect(host=f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PWD')}@regula-ai.yxfwbrv.mongodb.net/")

app = FastAPI()

@app.get("/")
def test():
    return {"status": "OK v2 (3)"}

allowed_origins = [
    "http://localhost:5173",
    "https://regula-back-805c0d9fbbe1.herokuapp.com/",
    "https://regula-front-fb6r-oogyz5wlx-thiago-penhas-projects.vercel.app/"
]

if os.getenv("ENVIRONMENT") == "production":
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,          
    allow_credentials=True,                  
    allow_methods=["*"],                     
    allow_headers=["*"],                     
)

working_directory = os.path.dirname(os.path.abspath(__file__))
use_cases_directory = os.path.join(working_directory, "use_cases")
routes = glob.glob(os.path.join(use_cases_directory, "**/index.py"), recursive=True)

for route in routes:
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')
    
    try:
        module = import_module(module_name)
        print(f"Importando módulo: {module_name}")
        if hasattr(module, 'router'):
            app.include_router(module.router)
    except ModuleNotFoundError as e:
        print(f"Erro ao importar módulo {module_name}: {e}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)