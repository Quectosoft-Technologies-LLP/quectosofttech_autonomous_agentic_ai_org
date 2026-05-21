import React from 'react';
import AgentCard from './components/AgentCard';
import RAIDView from './components/RAIDView';
import PipelineView from './components/PipelineView';

export default function App() {
  const agent = { id: 'backend_engineer', name: 'Backend Engineer', tier: 4, role: 'backend_engineer', department: 'engineering' };
  const raid = [{ title: 'Pipeline risk', status: 'OPEN', score: 12, owner: 'backend_engineer' }];
  const nodes = [{ id: 'requirements', status: 'done' }, { id: 'implementation', status: 'running' }];
  return (
    <main>
      <h1>Quectosoft Autonomous Agentic AI Org</h1>
      <AgentCard agent={agent} />
      <RAIDView entries={raid} />
      <PipelineView nodes={nodes} />
    </main>
  );
}
