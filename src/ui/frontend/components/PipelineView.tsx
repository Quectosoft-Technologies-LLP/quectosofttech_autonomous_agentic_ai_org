import React from 'react';

type Node = { id: string; status: string };

export default function PipelineView({ nodes }: { nodes: Node[] }) {
  return (
    <section>
      <h2>Pipeline</h2>
      <ol>
        {nodes.map((node) => <li key={node.id}>{node.id} · {node.status}</li>)}
      </ol>
    </section>
  );
}
