"""SQLite persistence helpers for incidents and operator actions."""
import sqlite3
from pathlib import Path


def initialize_database(db_path="factorypilot.db"):
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS incidents (
                incident_id TEXT PRIMARY KEY,
                status TEXT NOT NULL,
                signal TEXT NOT NULL,
                severity TEXT NOT NULL,
                observed_value REAL,
                threshold REAL,
                timestamp TEXT,
                summary TEXT,
                resolution_note TEXT
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS operator_actions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                incident_id TEXT NOT NULL,
                action TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
    return str(path)


def save_incident(incident, db_path="factorypilot.db"):
    initialize_database(db_path)
    with sqlite3.connect(db_path) as connection:
        connection.execute("""
            INSERT OR REPLACE INTO incidents
            (incident_id, status, signal, severity, observed_value,
             threshold, timestamp, summary, resolution_note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            incident["incident_id"], incident["status"], incident["signal"],
            incident["severity"], incident["observed_value"], incident["threshold"],
            incident["timestamp"], incident["summary"], incident.get("resolution_note"),
        ))


def record_operator_action(incident_id, action, db_path="factorypilot.db"):
    initialize_database(db_path)
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            "INSERT INTO operator_actions (incident_id, action) VALUES (?, ?)",
            (incident_id, action),
        )
