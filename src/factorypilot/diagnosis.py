"""Evidence-oriented, rule-based incident investigation."""
import pandas as pd


def investigate_incident(df: pd.DataFrame, finding: dict):
    """Summarize signal behavior and provide cautious hypotheses."""
    signal = finding["signal"]
    values = df[signal].astype(float)
    midpoint = max(1, len(values) // 2)
    early_mean = float(values.iloc[:midpoint].mean())
    recent_mean = float(values.iloc[midpoint:].mean())
    delta = recent_mean - early_mean

    hypotheses = {
        "motor_temperature_c": [
            "Possible increased mechanical load, cooling issue, or sensor problem."
        ],
        "vibration_mm_s": [
            "Possible imbalance, misalignment, looseness, bearing wear, or sensor issue."
        ],
        "conveyor_speed_m_s": [
            "Possible drive/control issue, mechanical resistance, or speed-sensor problem."
        ],
        "throughput_units_min": [
            "Possible line bottleneck, speed reduction, upstream/downstream blockage, or counting issue."
        ],
    }
    return {
        "signal": signal,
        "observed_value": finding["observed_value"],
        "threshold": finding["threshold"],
        "severity": finding["severity"],
        "early_mean": round(early_mean, 3),
        "recent_mean": round(recent_mean, 3),
        "change": round(delta, 3),
        "hypotheses": hypotheses.get(signal, ["Cause not determined."]),
        "caveat": "These are hypotheses from simulated data, not a confirmed equipment diagnosis.",
    }
