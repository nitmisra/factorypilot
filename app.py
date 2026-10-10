import streamlit as st
import plotly.express as px

from factorypilot.simulator import simulate_telemetry
from factorypilot.detector import detect_anomalies
from factorypilot.diagnosis import investigate_incident
from factorypilot.knowledge_base import retrieve_guidance
from factorypilot.copilot import build_copilot_answer

st.set_page_config(page_title="FactoryPilot AI", page_icon="🏭", layout="wide")
st.title("🏭 FactoryPilot AI")
st.caption("Factory operations copilot · simulated packaging/conveyor line")

with st.sidebar:
    st.header("Simulation controls")
    scenario = st.selectbox(
        "Operating scenario",
        ["normal", "overheating", "high_vibration", "throughput_drop"],
        format_func=lambda x: {
            "normal": "Normal operation",
            "overheating": "Motor overheating",
            "high_vibration": "High vibration",
            "throughput_drop": "Throughput drop",
        }[x],
    )
    duration = st.slider("Duration (minutes)", 30, 180, 60, step=30)
    seed = st.number_input("Random seed", min_value=0, max_value=999999, value=42)
    st.warning("Synthetic data only. Do not use this demo to operate real equipment.")

df = simulate_telemetry(scenario=scenario, duration_minutes=duration, seed=int(seed))
findings = detect_anomalies(df)
latest = df.iloc[-1]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Motor temperature", f"{latest['motor_temperature_c']:.1f} °C")
c2.metric("Vibration", f"{latest['vibration_mm_s']:.2f} mm/s")
c3.metric("Conveyor speed", f"{latest['conveyor_speed_m_s']:.2f} m/s")
c4.metric("Throughput", f"{latest['throughput_units_min']:.1f} units/min")

st.subheader("Telemetry trends")
signals = st.multiselect(
    "Signals to display",
    ["motor_temperature_c", "vibration_mm_s", "conveyor_speed_m_s", "throughput_units_min"],
    default=["motor_temperature_c", "throughput_units_min"],
)
if signals:
    chart_df = df.melt(id_vars=["timestamp"], value_vars=signals, var_name="Signal", value_name="Value")
    fig = px.line(chart_df, x="timestamp", y="Value", color="Signal", title="Simulated telemetry")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Detected findings")
if findings:
    st.dataframe(findings, use_container_width=True, hide_index=True)
    selected = findings[0]
    investigation = investigate_incident(df, selected)
    query = st.text_input(
        "Ask the copilot about this incident",
        value="Why might this be happening, and what should I check first?",
    )
    if st.button("Investigate incident", type="primary"):
        guidance = retrieve_guidance(query + " " + selected["signal"])
        answer = build_copilot_answer(query, investigation, guidance)
        st.markdown(answer)
else:
    st.success("No configured threshold violations detected in this simulated run.")

with st.expander("View telemetry data"):
    st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Thresholds and sensor values are illustrative assumptions, not manufacturer-approved operating limits.")
