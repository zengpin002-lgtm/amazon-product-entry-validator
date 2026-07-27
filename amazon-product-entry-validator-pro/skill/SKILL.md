---
name: amazon-product-entry-validator-pro
description: Produce purchase-grade Amazon product entry decisions using SellerSprite and Amazon evidence, direct-market concentration, new-brand success, competitor traffic reproducibility, official FBA fees, landed cost, stress profit, inventory exit, IP and compliance gates. Use for deep product validation, supplier sample decisions, 50-100 unit trial orders, profitability reports, and PASS, HOLD, ENTRY_BLOCKED, CASH_RISK, LOSS, or REJECT decisions.
---

# Amazon Product Entry Validator Pro

Build an auditable product decision. Never recommend first and search for supporting data afterward.

## Confirm the contract

Record product boundary, marketplace, fulfillment, store stage, budget, target price, batch size, timing, prohibited risks, available sources, missing sources, and requested report type. Separate candidate screening, single-product validation, and purchase decision.

## Complete the evidence stack

Read `references/purchase-gates.md` and `references/report-schema.md`.

1. Build a direct-substitute market and keep adjacent alternatives separate.
2. Use batch exports for market size, concentration, new-product share, price bands, and historical periods.
3. Use current Amazon pages and listing-level extensions to cross-check ASIN price, age, BSR, fulfillment, variants, dimensions, fees, images, and page claims.
4. Use available price/rank history for price position, promotion, stock signals, review direction, and seasonality.
5. Analyze winner assets and failure/VOC evidence.
6. Recalculate FBA fees with Amazon's current official tool before a purchase decision.
7. Add supplier, packaging, freight, sample, IP, compliance, and store-specific evidence.

Use `Verified`, `Estimated`, `Conflict`, `Blocked`, and `Not applicable`. Do not convert software-accessible missing data into a report limitation before attempting the software.

## Decide before scoring

Run hard gates before weighted scoring. Use `scripts/score_candidates.py` for structured candidate ranking, `scripts/landed_cost_model.py` for freight and landed cost, and `scripts/profit_model.py` for scenarios.

Test:

- base, conservative, optimistic, 20% price-down, doubled-return, and clearance economics;
- 50-unit inventory exit and 100-unit upper limit;
- direct-market concentration and durable new-brand entry;
- traffic, parent/variant, price, review and Listing reproducibility;
- official versus third-party FBA fee conflict;
- IP, compliance, safety, supplier and claim risk.

Output only `PASS`, `CONDITIONAL SAMPLE`, `HOLD FOR PURCHASE`, `DATA INCOMPLETE`, `ENTRY_BLOCKED`, `CASH_RISK`, `LOSS`, or `REJECT`. A weighted score cannot override a hard gate.

## Perform adversarial review

Before release, state the strongest failure case, least reproducible winner advantage, price-down result, return-rate shock, inventory exit path, and evidence that would reverse the decision. Return to data collection if any answer depends on accessible but uncollected evidence.

## Produce the report

Lead with the decision, strongest veto, and evidence boundaries. Put a visual ASIN overview near the front. Separate what evidence supports from what it does not support. Never expose internal team orchestration, private store data, credentials, or hidden reasoning.
