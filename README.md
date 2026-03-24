# DevTrack


## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
```

## Run

```bash
python -m django runserver --settings=devtrack.settings
```

Server starts at `http://127.0.0.1:8000/`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/reporters/ | Create a reporter |
| GET | /api/reporters/ | List all reporters |
| GET | /api/reporters/?id=1 | Get reporter by ID |
| POST | /api/issues/ | Create an issue |
| GET | /api/issues/ | List all issues |
| GET | /api/issues/?id=1 | Get issue by ID |
| GET | /api/issues/?status=open | Filter issues by status |

## Example

```bash
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Alice", "email": "alice@example.com", "team": "Backend"}'
```
