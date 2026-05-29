FROM python:3.14-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY src/ src/
RUN uv sync --no-dev --frozen

FROM python:3.14-slim

COPY --from=builder /app /app
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "zzttvmtp.main:app", "--host", "0.0.0.0", "--port", "8000"]
