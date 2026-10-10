# FactoryPilot AI

An industrial AI portfolio project: a simulated packaging/conveyor line operations copilot.

## MVP capabilities

- Generate reproducible synthetic telemetry for a conveyor motor.
- Simulate normal operation, overheating, high vibration, and throughput drop.
- Detect configured threshold violations.
- Provide a Streamlit dashboard with telemetry charts and incident findings.
- Lay the foundation for evidence-grounded diagnosis and RAG-based maintenance guidance.

> This is a simulation for demonstration and learning. It is not designed to monitor or control real industrial equipment. Thresholds are illustrative and must not be used as safety limits.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate           # Windows

pip install -r requirements.txt
pip install -e .
streamlit run app.py
```

## Run tests

```bash
pytest -q
```

## Project structure

```text
factorypilot-ai/
├── app.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── src/factorypilot/
│   ├── __init__.py
│   ├── simulator.py
│   ├── detector.py
│   ├── incident_manager.py
│   ├── diagnosis.py
│   ├── copilot.py
│   ├── knowledge_base.py
│   └── database.py
├── data/manuals/conveyor_troubleshooting.md
├── tests/
│   ├── test_simulator.py
│   ├── test_detector.py
│   └── test_incident_manager.py
└── docs/
    ├── architecture.md
    ├── sample_incident.md
    └── evaluation.md
```

## MVP architecture

1. `simulator.py` creates reproducible synthetic telemetry.
2. `detector.py` applies explicit, configurable rules to identify threshold violations.
3. `incident_manager.py` converts findings into incident records.
4. `diagnosis.py` correlates signals and provides cautious, rule-based hypotheses.
5. `knowledge_base.py` retrieves relevant passages from the included sample troubleshooting guide.
6. `copilot.py` formats an evidence-grounded answer. The initial version works without an LLM API.
7. `database.py` persists incidents and operator actions in SQLite.
8. `app.py` provides the Streamlit UI.

## Suggested development sequence

1. Run tests and inspect the synthetic scenarios.
2. Explore the dashboard and threshold findings.
3. Add incident persistence and an operator action log.
4. Improve diagnosis and retrieval evaluation.
5. Optionally connect an LLM through an adapter, keeping API keys in environment variables.
6. Evaluate fault-detection precision/recall and answer grounding before making claims about performance.

## Portfolio evidence to publish

- Screenshots of normal and fault scenarios.
- A short end-to-end demo video.
- Architecture diagram.
- Test results and evaluation methodology.
- Clear separation between simulated results and real-world claims.
