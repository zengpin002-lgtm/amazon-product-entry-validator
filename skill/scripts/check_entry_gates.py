#!/usr/bin/env python3
import argparse
import json

TRUE_VALUES = {"1", "true", "yes", "verified", "pass", "positive"}


def truthy(data, key):
    return str(data.get(key, "")).strip().lower() in TRUE_VALUES


def decide(data):
    if truthy(data, "red_gate"):
        return "REJECT", "red IP/compliance/safety gate"
    if not truthy(data, "direct_market_verified"):
        return "DATA INCOMPLETE", "direct-substitute market not verified"
    if not truthy(data, "concentration_scope_verified"):
        return "DATA INCOMPLETE", "concentration scope unresolved"
    concentration = data.get("product_concentration_pct")
    if concentration is not None and float(concentration) >= 45:
        if not truthy(data, "durable_new_brand_entry_verified"):
            return "ENTRY_BLOCKED", "high concentration without durable new-brand entry"
    if not truthy(data, "new_product_sales_share_verified"):
        return "DATA INCOMPLETE", "new-product sales share not verified"
    if not truthy(data, "conservative_profit_positive"):
        return "LOSS", "conservative contribution profit is not positive"
    return "CONTINUE RESEARCH", "no Lite blocker found"


parser = argparse.ArgumentParser()
parser.add_argument("input_json")
args = parser.parse_args()
with open(args.input_json, encoding="utf-8-sig") as handle:
    payload = json.load(handle)
status, reason = decide(payload)
print(json.dumps({"status": status, "reason": reason}, ensure_ascii=False))
