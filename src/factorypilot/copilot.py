"""LLM-free, evidence-grounded answer formatter for the initial MVP."""


def build_copilot_answer(question, investigation, guidance):
    lines = [
        "### Incident assessment",
        f"**Question:** {question}",
        f"**Signal:** `{investigation['signal']}`",
        f"**Observed value:** {investigation['observed_value']}",
        f"**Configured threshold:** {investigation['threshold']}",
        f"**Trend change (first half to second half):** {investigation['change']}",
        "",
        "### Possible explanations",
    ]
    lines.extend([f"- {item}" for item in investigation["hypotheses"]])
    lines.extend(["", "### Relevant maintenance guidance"])
    if guidance:
        for section in guidance:
            lines.append(section)
    else:
        lines.append("No matching passage was found in the sample troubleshooting guide.")
    lines.extend([
        "",
        f"> **Caution:** {investigation['caveat']}",
        "Follow the site's approved safety and maintenance procedures. Have a qualified operator or technician validate any intervention.",
    ])
    return "\n".join(lines)
