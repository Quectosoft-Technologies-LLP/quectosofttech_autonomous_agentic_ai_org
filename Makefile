.PHONY: setup run test lint docker-up docker-down pull-models health-check clean

# Quectosoft Technologies LLP — Autonomous Agentic AI Org
# Author: Subrit Dikshit <subrit@quectosofttech.com>

setup:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"
	pre-commit install
	@echo "\n✅ Setup complete. Run: cp .env.example .env"

run:
	uvicorn src.ui.backend.main:app --host 0.0.0.0 --port 8000 --reload

docker-up:
	docker compose up -d postgres redis chromadb neo4j \
		agent_memory_mcp team_memory_mcp dept_memory_mcp \
		project_memory_mcp org_memory_mcp
	@echo "✅ Infrastructure running. Verify with: make health-check"

docker-down:
	docker compose down

pull-models:
	ollama pull hermes3:1b
	ollama pull hermes3:8b
	ollama pull hermes3:70b
	@echo "✅ Models ready."

health-check:
	python scripts/health_check.py

test:
	pytest tests/ -v --cov=src --cov-report=term-missing

lint:
	ruff check src/ tests/
	mypy src/ --strict

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .ruff_cache dist build
