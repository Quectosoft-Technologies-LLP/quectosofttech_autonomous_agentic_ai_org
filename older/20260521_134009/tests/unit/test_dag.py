"""Unit tests — OpenClaw DAG"""
import pytest
from src.orchestration.openclaw.dag import DAG, DAGNode


def make_dag() -> DAG:
    dag = DAG(dag_id="test_dag")
    dag.add_node(DAGNode(
        node_id="requirements",
        agent_id="requirements_agent",
        task={"prompt": "Write PRD"},
        depends_on=[],
    ))
    dag.add_node(DAGNode(
        node_id="design",
        agent_id="architect_agent",
        task={"prompt": "Design system"},
        depends_on=["requirements"],
    ))
    return dag


def test_ready_nodes_initial():
    dag = make_dag()
    ready = dag.ready_nodes()
    assert len(ready) == 1
    assert ready[0].node_id == "requirements"


def test_no_ready_after_blocked():
    dag = make_dag()
    dag.nodes["requirements"].status = "running"
    assert dag.ready_nodes() == []


def test_design_ready_after_requirements_done():
    dag = make_dag()
    dag.nodes["requirements"].status = "success"
    ready = dag.ready_nodes()
    assert any(n.node_id == "design" for n in ready)


def test_not_complete_while_pending():
    dag = make_dag()
    assert not dag.is_complete()


def test_complete_when_all_done():
    dag = make_dag()
    for node in dag.nodes.values():
        node.status = "success"
    assert dag.is_complete()
