from factorypilot.simulator import simulate_telemetry
from factorypilot.detector import detect_anomalies


def test_overheating_is_detected_at_end_of_run():
    findings = detect_anomalies(simulate_telemetry("overheating", duration_minutes=60, seed=42))
    assert any(item["signal"] == "motor_temperature_c" for item in findings)


def test_normal_scenario_has_no_high_threshold_findings():
    findings = detect_anomalies(simulate_telemetry("normal", duration_minutes=60, seed=42))
    assert findings == []
