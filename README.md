# code-assistant-api

An AI coding agent exposed over HTTP — submit coding tasks and receive planned solutions and generated code.

## Features

- Submit coding tasks with context files and language preferences
- List and inspect task status and results
- Register and configure AI coding agents
- Powered by pydantic-ai for agent orchestration
- Fully typed with Pydantic models

## Quick start

```bash
# Install dependencies
uv sync

# Run the server
uv run uvicorn code_assistant_api.main:app --reload
```

Open http://localhost:8000/docs for interactive API documentation.

## API overview

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/tasks` | Submit a new coding task |
| GET | `/api/v1/tasks` | List all tasks |
| GET | `/api/v1/tasks/{id}` | Get task details |
| DELETE | `/api/v1/tasks/{id}` | Remove a task |
| GET | `/api/v1/agents` | List available agents |
| GET | `/api/v1/agents/{id}` | Get agent configuration |
| POST | `/api/v1/agents` | Register a new agent |

## Example usage

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Submit a coding task
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a Python function to sort a list", "language": "python"}'

# List tasks
curl http://localhost:8000/api/v1/tasks

# Get task details
curl http://localhost:8000/api/v1/tasks/<task-id>
```

## Configuration

Copy `.env.example` to `.env` and set your environment variables:

- `AI_MODEL` — model identifier (default: openai:gpt-4o)
- `AI_API_KEY` — API key for the AI provider
- `HOST` — server host (default: 0.0.0.0)
- `PORT` — server port (default: 8000)

## Docker

```bash
docker compose up --build
```

## Development

```bash
# Install with dev dependencies
uv sync --all-extras

# Run linting
uv run ruff check .

# Run type checking
uv run mypy .

# Run tests
uv run pytest
```
