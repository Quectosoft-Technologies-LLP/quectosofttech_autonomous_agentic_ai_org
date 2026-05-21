from src.orchestration.openclaw.dag import DAG, DAGNode
from src.orchestration.openclaw.dag_runner import DAGRunner

def test_dag_runner_executes_dependencies_in_order():
    dag = DAG([
        DAGNode('a', 'start'),
        DAGNode('b', 'merge', depends_on=['a']),
    ])
    runner = DAGRunner(dag)
    result = runner.run({
        'start': lambda ctx: {'value': 1},
        'merge': lambda ctx: {'from_a': ctx['depends_on']['a']['value']},
    })
    assert result['state']['b']['from_a'] == 1
