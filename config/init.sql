-- Initialize database with pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create schema
CREATE SCHEMA IF NOT EXISTS crucible;

-- Set search path
SET search_path TO crucible, public;

-- Initial tables will be created by Alembic migrations