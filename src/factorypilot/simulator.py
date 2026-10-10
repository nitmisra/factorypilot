"""Generate reproducible synthetic telemetry for a packaging conveyor."""
import numpy as np
import pandas as pd


SUPPORTED_SCENARIOS = {"normal", "overheating", "high_vibration", "throughput_drop"}


def simulate_telemetry(scenario="normal", duration_minutes=60, seed=42):
    """Return one row per minute of simulated conveyor telemetry."""
    if scenario not in SUPPORTED_SCENARIOS:
        raise ValueError(f"Unsupported scenario: {scenario}")
    if duration_minutes < 1:
        raise ValueError("duration_minutes must be positive")

    rng = np.random.default_rng(seed)
    minute = np.arange(duration_minutes)

    temperature = 70 + rng.normal(0, 1.5, duration_minutes)
    vibration = 2.5 + rng.normal(0, 0.25, duration_minutes)
    speed = 1.0 + rng.normal(0, 0.02, duration_minutes)
    throughput = 100 + rng.normal(0, 2, duration_minutes)

    start = duration_minutes // 2
    elapsed = np.maximum(minute - start, 0)

    if scenario == "overheating":
        temperature += elapsed * 0.7
    elif scenario == "high_vibration":
        vibration += elapsed * 0.12
    elif scenario == "throughput_drop":
        speed -= elapsed * 0.01
        throughput -= elapsed * 0.7

    return pd.DataFrame({
        "timestamp": pd.Timestamp("2026-01-01 08:00:00")
        + pd.to_timedelta(minute, unit="min"),
        "motor_temperature_c": temperature.round(2),
        "vibration_mm_s": vibration.round(2),
        "conveyor_speed_m_s": speed.round(3),
        "throughput_units_min": throughput.round(2),
        "scenario": scenario,
    })
