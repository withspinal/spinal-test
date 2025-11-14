FROM ghcr.io/astral-sh/uv:0.9.9-python3.14-trixie-slim

RUN useradd -ms /bin/sh -u 1001 app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app


# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable;


COPY --chown=app:app src/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy the project into the image
COPY --chown=app:app src /app
ENV PYTHONPATH="/app"

# Ensure the server logs requests
ENV GRANIAN_LOG_ACCESS_ENABLED=true

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-editable;


ENV PATH="/app/.venv/bin:$PATH"

USER app
EXPOSE 8000

CMD ["./entrypoint.sh"]
