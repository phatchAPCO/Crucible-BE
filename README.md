# Crucible-BE

AI Processing Backend Service for Project Tsunami

## Tech Stack

- **Framework**: FastAPI 0.116.1
- **Language**: Python 3.12+
- **Database**: PostgreSQL 16 with pgvector
- **Cache**: Redis 7
- **Package Manager**: uv

## Quick Start

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- uv package manager

### Development Setup

1. **Install uv** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Create virtual environment**:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
uv pip install -e ".[dev]"
```

4. **Copy environment variables**:
```bash
cp .env.template .env
# Edit .env with your configuration
```

5. **Start services with Docker**:
```bash
docker-compose up -d postgres redis
```

6. **Run the application**:
```bash
uvicorn app.main:app --reload --port 8000
```

7. **Access the API**:
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/v1/health

## Docker Development

Run everything with Docker Compose:
```bash
docker-compose up
```

## Project Structure

```
crucible-be/
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # Core configuration
│   ├── models/        # Database models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   └── utils/         # Utilities
├── tests/             # Test files
├── config/            # Configuration files
├── docker-compose.yml # Docker configuration
└── pyproject.toml     # Dependencies
```

## API Endpoints

- `POST /v1/tasks/process` - Submit processing task
- `POST /v1/context/upload` - Upload context files
- `GET /v1/context/{id}` - Retrieve context
- `POST /v1/context/search` - Semantic search
- `GET /v1/models/available` - List available models
- `WS /v1/stream/{task_id}` - Real-time streaming

## Testing

```bash
pytest
pytest --cov=app tests/
```

## Development Phases

- [x] Phase 1: Core Infrastructure
- [ ] Phase 2: AI Integration
- [ ] Phase 3: Vector Operations
- [ ] Phase 4: Advanced Features
- [ ] Phase 5: Production Readiness