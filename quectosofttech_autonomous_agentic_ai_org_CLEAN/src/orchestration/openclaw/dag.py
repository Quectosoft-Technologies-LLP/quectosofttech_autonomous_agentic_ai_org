from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class DAGNode:
    node_id: str
    action: str
    depends_on: List[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

class DAG:
    def __init__(self, nodes: List[DAGNode]):
        self.nodes = {n.node_id: n for n in nodes}
        self._validate()

    def _validate(self):
        missing = []
        for node in self.nodes.values():
            for dep in node.depends_on:
                if dep not in self.nodes:
                    missing.append((node.node_id, dep))
        if missing:
            raise ValueError(f'missing dependencies: {missing}')
        self.topological_order()

    def topological_order(self) -> List[str]:
        temporary = set()
        permanent = set()
        order: List[str] = []

        def visit(node_id: str):
            if node_id in permanent:
                return
            if node_id in temporary:
                raise ValueError(f'cycle detected at {node_id}')
            temporary.add(node_id)
            for dep in self.nodes[node_id].depends_on:
                visit(dep)
            temporary.remove(node_id)
            permanent.add(node_id)
            order.append(node_id)

        for node_id in sorted(self.nodes):
            visit(node_id)
        return order
