from src.ui.backend.main import events, health

def test_events_snapshot_returns_trace_and_events():
    health()
    payload = events()
    assert payload['trace_id']
    assert payload['count'] >= 1
