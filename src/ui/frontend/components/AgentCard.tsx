import React from 'react';

type Agent = { id: string; name: string; tier: number; role: string; department: string };

export default function AgentCard({ agent }: { agent: Agent }) {
  return (
    <article>
      <h3>{agent.name}</h3>
      <p>{agent.id}</p>
      <p>Tier {agent.tier} · {agent.role} · {agent.department}</p>
    </article>
  );
}
