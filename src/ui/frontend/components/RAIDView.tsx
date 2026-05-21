import React from 'react';

type RAIDEntry = { title: string; status: string; score: number; owner: string };

export default function RAIDView({ entries }: { entries: RAIDEntry[] }) {
  return (
    <section>
      <h2>RAID Register</h2>
      <ul>
        {entries.map((entry) => (
          <li key={`${entry.title}-${entry.owner}`}>{entry.title} · {entry.status} · score {entry.score} · {entry.owner}</li>
        ))}
      </ul>
    </section>
  );
}
