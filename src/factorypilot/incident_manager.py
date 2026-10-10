"""Small incident lifecycle helpers."""


def create_incident(finding, incident_id="INC-0001"):
    """Convert a detector finding into an incident record."""
    return {
        "incident_id": incident_id,
        "status": "open",
        "signal": finding["signal"],
        "severity": finding["severity"],
        "observed_value": finding["observed_value"],
        "threshold": finding["threshold"],
        "timestamp": finding["timestamp"],
        "summary": finding["reason"],
    }


def resolve_incident(incident, resolution_note):
    """Return a resolved copy of an incident after a human records an outcome."""
    updated = dict(incident)
    updated["status"] = "resolved"
    updated["resolution_note"] = resolution_note
    return updated
