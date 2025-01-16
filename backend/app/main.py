from fastapi import FastAPI
from .database import engine, Base
from .routers import items  # Assume you have a separate router file
from .models import Item  # Assuming you have an Item model

app = FastAPI()

# Create all tables in the database (if not exist)
Base.metadata.create_all(bind=engine)

# Include the router for CRUD operations
app.include_router(items.router)
