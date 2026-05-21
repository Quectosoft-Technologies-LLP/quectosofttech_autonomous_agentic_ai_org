"""Integration tests — Memory backends (requires Redis + ChromaDB running)"""
import pytest
import os

REDIS_AVAILABLE = bool(os.getenv("REDIS_URL"))
CHROMA_AVAILABLE = bool(os.getenv("CHROMADB_HOST"))


@pytest.mark.skipif(not REDIS_AVAILABLE, reason="Redis not configured")
@pytest.mark.asyncio
async def test_redis_store_and_retrieve():
    from src.memory.backends.redis_backend import RedisBackend
    backend = RedisBackend()
    await backend.connect()
    await backend.set("test:key", "test_value", ttl=10)
    result = await backend.get("test:key")
    assert result == "test_value"
    await backend.close()


@pytest.mark.skipif(not CHROMA_AVAILABLE, reason="ChromaDB not configured")
def test_chromadb_upsert_and_query():
    from src.memory.backends.chromadb_backend import ChromaDBBackend
    backend = ChromaDBBackend("test_collection")
    backend.upsert("doc1", "Quectosoft Technologies autonomous agents", {"source": "test"})
    results = backend.query("autonomous agents", n_results=1)
    assert len(results) >= 1
