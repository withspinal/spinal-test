from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import get_settings
from database.models.example_model import ExampleModel, ExampleType


def seed_local_dev_data() -> None:
    settings = get_settings()

    engine = create_engine(settings.database_url, echo=False)
    session = sessionmaker(engine, expire_on_commit=False)

    with session() as session:
        with session.begin():
            # Clear existing data (optional but ensures idempotent seeding)
            session.query(ExampleModel).delete()

            # Add two example rows
            example_1 = ExampleModel(
                type=ExampleType.EXAMPLE_1,
                col_1="First example",
                col_2="Optional data",
                active=True
            )

            example_2 = ExampleModel(
                type=ExampleType.EXAMPLE_2,
                col_1="Second example",
                col_2=None,
                active=True
            )

            session.add_all([example_1, example_2])

            print("✓ Successfully seeded 2 example rows")

    engine.dispose()


if __name__ == "__main__":
    seed_local_dev_data()
