from factorypilot.simulator import simulate_telemetry


def test_simulator_returns_expected_columns_and_rows():
    df = simulate_telemetry(duration_minutes=60)
    assert len(df) == 60
    assert {
        "timestamp", "motor_temperature_c", "vibration_mm_s",
        "conveyor_speed_m_s", "throughput_units_min", "scenario",
    }.issubset(df.columns)


def test_simulator_is_reproducible():
    assert simulate_telemetry("overheating", seed=42).equals(
        simulate_telemetry("overheating", seed=42)
    )


def test_overheating_increases_temperature():
    df = simulate_telemetry("overheating", seed=42)
    assert df["motor_temperature_c"].iloc[30:].mean() > df["motor_temperature_c"].iloc[:30].mean()


def test_throughput_drop_reduces_output():
    df = simulate_telemetry("throughput_drop", seed=42)
    assert df["throughput_units_min"].iloc[-1] < df["throughput_units_min"].iloc[0]
