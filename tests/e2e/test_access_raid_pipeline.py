from src.ui.backend.main import access_approval_workflow, WorkflowPayload, raid_evaluate, RAIDPayload

def test_access_then_raid_pipeline():
    workflow = access_approval_workflow(WorkflowPayload(agent_id='backend_engineer', action_type='read', resource='project_requirements', operation='writing_code'))
    raid = raid_evaluate(RAIDPayload(entry_id='e2e-raid-1', agent_id='backend_engineer', task_id='e2e-task', raid_type='RISK', title='Pipeline risk', description='Pipeline risk', likelihood=3, impact=4, category='GENERAL'))
    assert workflow['access']['allowed'] is True
    assert raid['decision']['action'] in {'VP_REVIEW', 'CSUITE_GATE', 'HUMAN_HITL', 'AUTONOMOUS'}
