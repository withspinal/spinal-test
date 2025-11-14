from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from api_models import ExampleSchema
from database import ExampleModel
from database.session import get_db
from settings import get_settings

app = FastAPI()

settings = get_settings()


@app.get("/test", response_model=list[ExampleSchema])
async def test_with_db_session(db: Session = Depends(get_db)) -> list[ExampleSchema]:

    rows = db.scalars(select(ExampleModel))
    examples = list(rows.all())
    if not examples:
        raise HTTPException(status_code=404, detail="No examples found")

    return [ExampleSchema.model_validate(e) for e in examples]
