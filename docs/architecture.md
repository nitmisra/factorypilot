# Architecture Notes

## Request/data flow

Synthetic telemetry → threshold detector → finding/incident → rule-based investigation → manual retrieval → copilot response → operator review.

## Design principles

- Keep detection deterministic and independently testable.
- Pass observed values and timestamps to the explanation layer rather than asking an LLM to infer them.
- Ground maintenance recommendations in retrieved documentation.
- Show uncertainty and preserve human approval for interventions.
- Keep the data simulator replaceable by a future read-only connector.
- Never connect this prototype to real control systems.

## Future extensions

- Persist and query incidents from SQLite.
- Add anomaly detection with a labelled evaluation dataset.
- Replace keyword retrieval with embeddings and a vector index.
- Add an LLM adapter with schema-validated output and API cost/latency tracking.
- Add voice input/output only after the text workflow is reliable.
