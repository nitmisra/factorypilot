"""Explainable threshold-based anomaly detection."""
import pandas as pd

# Illustrative demo thresholds only; not safety or engineering limits.
DEFAULT_THRESHOLDS = {
    "motor_temperature_c": {"limit": 85.0, "operator": ">", "severity": "high"},
    "vibration_mm_s": {"limit": 6.0, "operator": ">", "severity": "high"},
    "conveyor_speed_m_s": {"limit": 0.75, "operator": "<", "severity": "medium"},
    "throughput_units_min": {"limit": 85.0, "operator": "<", "severity": "medium"},
}


def detect_anomalies(df: pd.DataFrame, thresholds=None):
    """Return a list of findings for threshold violations in the supplied data."""
    rules = thresholds or DEFAULT_THRESHOLDS
    findings = []
    if df.empty:
        return findings

    for signal, rule in rules.items():
        if signal not in df.columns:
            continue
        value = float(df[signal].iloc[-1])
        limit = float(rule["limit"])
        violated = value > limit if rule["operator"] == ">" else value < limit
        if violated:
            findings.append({
                "signal": signal,
                "severity": rule["severity"],
                "observed_value": value,
                "operator": rule["operator"],
                "threshold": limit,
                "timestamp": str(df["timestamp"].iloc[-1]),
                "reason": (
                    f"{signal}={value} {rule['operator']} configured limit {limit}"
                ),
            })
    return findings
