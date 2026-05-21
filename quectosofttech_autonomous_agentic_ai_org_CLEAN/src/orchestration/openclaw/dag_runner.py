from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, Any
from .dag import DAG

@dataclass
class NodeResult:
    node_id: str
    status: str
    output: Any

class DAGRunner:
    def __init__(self, dag: DAG):
        self.dag = dag

    def run(self, handlers: Dict[str, Callable[[dict], Any]]):
        state = {}
        results = []
        for node_id in self.dag.topological_order():
            node = self.dag.nodes[node_id]
            handler = handlers.get(node.action)
            if handler is None:
                raise KeyError(f'no handler for action {node.action}')
            inputs = {dep: state[dep] for dep in node.depends_on}
            output = handler({'node': node.node_id, 'depends_on': inputs, 'metadata': node.metadata})
            state[node_id] = output
            results.append(NodeResult(node_id=node_id, status='completed', output=output))
        return {'results': results, 'state': state}
