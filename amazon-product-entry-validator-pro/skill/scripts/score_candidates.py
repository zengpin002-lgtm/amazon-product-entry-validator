#!/usr/bin/env python3
import argparse
import csv

WEIGHTS = {
    "demand": 20,
    "competition": 18,
    "profit": 20,
    "fba": 12,
    "differentiation": 12,
    "compliance_ip": 10,
    "supply_chain": 8,
}
TRUE_VALUES = {"1", "true", "yes", "verified", "pass", "positive"}


def is_true(row, field):
    return row.get(field, "").strip().lower() in TRUE_VALUES


def number(row, field):
    value = row.get(field, "").strip()
    return None if value == "" else float(value)


def decide(row):
    if is_true(row, "red_gate"):
        return "REJECT", "red IP/compliance/safety gate"
    if not is_true(row, "direct_market_verified"):
        return "DATA INCOMPLETE", "direct-substitute market not verified"
    if not is_true(row, "concentration_scope_verified"):
        return "DATA INCOMPLETE", "concentration scope unresolved"

    concentration = number(row, "product_concentration_pct")
    entrants = is_true(row, "durable_new_brand_entry_verified")
    if concentration is not None and concentration >= 45 and not entrants:
        return "ENTRY_BLOCKED", "high direct-market concentration without durable new-brand entry"
    if not is_true(row, "new_product_sales_share_verified"):
        return "DATA INCOMPLETE", "new-product sales share not verified"
    if not is_true(row, "conservative_profit_positive"):
        return "LOSS", "conservative contribution profit is not positive"
    if not is_true(row, "inventory_exit_verified"):
        return "CASH_RISK", "50-unit exit path not verified"
    if not is_true(row, "official_fba_verified"):
        return "CONDITIONAL SAMPLE", "Amazon-official FBA fee not verified"
    return "PASS", "all hard gates passed"


ap = argparse.ArgumentParser()
ap.add_argument("input_csv")
ap.add_argument("--output", default="scored_candidates.csv")
a = ap.parse_args()
with open(a.input_csv, encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    missing_scores = [key for key in WEIGHTS if row.get(key, "").strip() == ""]
    row["weighted_score"] = (
        ""
        if missing_scores
        else round(sum(float(row[key]) * weight / 10 for key, weight in WEIGHTS.items()), 1)
    )
    row["status"], row["gate_reason"] = decide(row)

order = {
    "PASS": 0,
    "CONDITIONAL SAMPLE": 1,
    "HOLD FOR PURCHASE": 2,
    "DATA INCOMPLETE": 3,
    "ENTRY_BLOCKED": 4,
    "CASH_RISK": 5,
    "LOSS": 6,
    "REJECT": 7,
}
rows.sort(
    key=lambda row: (
        order.get(row["status"], 99),
        -float(row["weighted_score"]) if row["weighted_score"] != "" else 0,
    )
)
fields = list(rows[0].keys()) if rows else ["product", "weighted_score", "status", "gate_reason"]
with open(a.output, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(a.output)
