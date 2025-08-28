# Product Requirements Document: Crucible-BE
## AI Processing Backend Service

### Executive Summary
Crucible-BE serves as the AI processing core of Project Tsunami, providing a model-agnostic backend service for AI-augmented workflow operations. It handles prompt engineering, context management, and response processing between user inputs and AI model outputs.

### Product Vision
Build a production-ready AI backend service that efficiently processes diverse input types, manages context intelligently, routes requests to appropriate AI models, and delivers structured responses while maintaining security and scalability.

## Technology Stack

### Core Platform
- **Language**: Python 3.13.7
- **Framework**: FastAPI 0.116.1
- **ASGI Server**: Uvicorn with Gunicorn
- **Package Manager**: uv

### Data Layer
- **Primary Database**: PostgreSQL 16 with pgvector extension
- **Cache**: Redis 7
- **ORM**: SQLAlchemy 2.0.43

### AI/ML Infrastructure
- **Task Queue**: Celery with Redis broker
- **Primary LLM**: Anthropic Claude Sonnet 4 (1M token context)
- **Fallback LLM**: OpenAI GPT models

### Development & Operations
- **Testing**: pytest with pytest-asyncio
- **Containerization**: Docker with multi-stage builds
- **Documentation**: OpenAPI 3.0 auto-generated

## Core Components

### 1. Context Parser
- Processes documents (PDF, DOCX, TXT, MD, XLSX)
- Handles structured data (JSON, CSV, XML)
- Performs OCR on images when necessary
- Extracts and preserves metadata
- Chunks content for optimal processing

### 2. Vector Engine
- Generates embeddings for semantic search
- Manages pgvector collections in PostgreSQL
- Implements hybrid search (semantic + keyword)
- Handles relevance scoring and ranking

### 3. Prompt Builder
- Constructs model-specific prompts
- Optimizes for context windows
- Manages role-based formatting
- Implements token counting and truncation

### 4. Model Router
- Abstracts provider interfaces
- Implements failover and retry logic
- Supports streaming responses
- Tracks usage and costs

### 5. Response Dispatcher
- Validates and sanitizes outputs
- Converts between formats (markdown, JSON)
- Implements response caching
- Handles error formatting

## API Specification

### REST Endpoints
- `POST /v1/tasks/process` - Submit processing task
- `POST /v1/context/upload` - Upload context files
- `GET /v1/context/{id}` - Retrieve context
- `POST /v1/context/search` - Semantic search
- `GET /v1/models/available` - List models
- `POST /v1/sessions/create` - Create session
- `POST /v1/sessions/{id}/message` - Add message

### WebSocket
- `WS /v1/stream/{task_id}` - Real-time streaming

### Authentication
- Self-hosted Supabase Auth
- JWT tokens (15min access, 7day refresh)
- API keys for programmatic access
- Role-based access control (RBAC)

## Performance Requirements

### Response Times
- Document parsing: < 2s for 10MB files
- Embedding generation: < 500ms per chunk
- Model routing overhead: < 100ms
- Standard API response: < 5s

### Scalability
- 100 concurrent users
- 1000 requests/minute
- 50MB max document size
- 1M vectors per collection

### Reliability
- 99.9% uptime SLA
- Automatic failover
- Circuit breaker patterns
- Graceful degradation

## Security Requirements

### Data Protection
- Encryption at rest and in transit (TLS 1.3)
- Secure file upload with virus scanning
- Input sanitization and validation
- PII detection and masking

### Compliance
- GDPR-compliant data handling
- Comprehensive audit logging
- Data retention policies
- Right to deletion

## Development Phases

### Phase 1: Core Infrastructure (Weeks 1-2)
- FastAPI application setup
- Authentication system
- Database configuration
- Docker containerization

### Phase 2: AI Integration (Weeks 3-4)
- LLM provider clients
- Prompt builder
- Context parser
- Response dispatcher

### Phase 3: Vector Operations (Weeks 5-6)
- Qdrant integration
- Embedding pipeline
- Semantic search
- RAG implementation

### Phase 4: Advanced Features (Weeks 7-8)
- WebSocket streaming
- Session management
- Advanced parsing
- Caching layer

### Phase 5: Production Readiness (Weeks 9-10)
- Security hardening
- Performance optimization
- Monitoring setup
- Documentation

## Success Metrics

### Technical
- API response time < 2s (p95)
- Error rate < 0.1%
- Test coverage > 80%
- Zero critical vulnerabilities

### Business
- Support all specified input formats
- Route to 3+ AI providers
- Process 10,000+ daily requests
- Maintain 99.9% availability

## Risk Mitigation

### Technical Risks
- **Model API changes**: Maintain abstraction layer
- **Provider rate limits**: Implement caching and queuing
- **Vector DB scaling**: Design sharding strategy
- **Context window limits**: Smart chunking algorithms

### Operational Risks
- **Cost overruns**: Usage monitoring and alerts
- **Data privacy**: Strong encryption policies
- **Performance degradation**: Comprehensive monitoring
- **Vendor lock-in**: Provider-agnostic architecture

## Dependencies

### External Services
- Anthropic Claude API (primary)
- OpenAI API (fallback)
- Local file storage with S3 backup
- Cloudflare Tunnel for secure access

### Internal Dependencies
- Arc-FE frontend
- Corporate authentication system
- Internal network infrastructure

## Open Questions

1. Fine-tuned model support requirements?
2. Maximum file size constraints?
3. Multi-language support timeline?
4. Usage-based billing implementation?
5. Prompt customization level needed?