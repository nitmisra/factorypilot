from factorypilot.incident_manager import create_incident, resolve_incident


def test_incident_lifecycle():
    finding = {
        "signal": "motor_temperature_c",
        "severity": "high",
        "observed_value": 90.0,
        "threshold": 85.0,
        "timestamp": "2026-01-01 08:59:00",
        "reason": "Temperature exceeded configured limit",
    }
    incident = create_incident(finding, "INC-TEST")
    assert incident["status"] == "open"
    resolved = resolve_incident(incident, "Simulation ended after operator review")
    assert resolved["status"] == "resolved"
    assert resolved["resolution_note"]
