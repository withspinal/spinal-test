#!/bin/sh

set -e

PORT="${PORT:-8000}"

uv run alembic upgrade head
uv run python -m scripts.seed_dev
exec granian --interface asgi main:app --host 0.0.0.0 --port "$PORT" --reload
