---
name: amazon-product-entry-validator
description: Validate whether an Amazon product deserves deeper research using a direct-substitute market definition, evidence completeness, concentration risk, new-entrant signals, competitor reproducibility, and basic profitability gates. Use for Amazon product ideas, ASIN-based opportunity checks, candidate screening, market-entry reports, and decisions to continue, hold, or reject before supplier sampling.
---

# Amazon Product Entry Validator Lite

Reject weak opportunities before spending on samples, inventory, or full reports.

## Normalize the decision

Record marketplace, product, fulfillment method, target price, store stage, trial quantity, budget, and requested decision. Classify the output as candidate screening or single-product validation. Never issue purchase approval from the Lite workflow.

## Build the direct market

Define the direct substitute by buyer task, structure, material, pack count, price band, and use case. Record seed query, filters, period, parent/child handling, inclusions, exclusions, and sample count. Keep adjacent alternatives separate.

Capture:

- product, brand, and seller concentration;
- Top 3 and Top 10 share;
- new-product count and new-product sales share;
- low-review new-brand performance;
- price, rating, review, age, fulfillment, and variant structure for representative ASINs.

Prefer the narrowest valid market. If a broad category conflicts with the direct market, label `Conflict` and use neither as a final conclusion until scopes are reconciled.

## Apply entry gates

Read `references/evidence-gates.md`. A direct-market concentration near or above 50% is a material blocker unless several low-review new brands gained durable, reproducible share. Do not let demand or a high score override an entry blocker.

Analyze both:

- why winners sell: traffic, parent/variant asset, images, price, reviews, delivery, promotion, keywords, and page clarity;
- why products fail: VOC, returns, quality, packaging, fit, durability, and expectation mismatch.

Mark every winning advantage as reproducible, conditional, or non-reproducible for the target store.

## Use evidence states

Use only `Verified`, `Estimated`, `Conflict`, `Blocked`, and `Not applicable`. Mark `Blocked` only after the named source or tool was actually attempted. Never invent paid-tool metrics.

## Decide

Run `scripts/check_entry_gates.py` when structured inputs are available. Output one status:

- `CONTINUE RESEARCH`: no Lite blocker found;
- `DATA INCOMPLETE`: software-accessible decision data is missing;
- `ENTRY_BLOCKED`: market structure blocks a new entrant;
- `LOSS`: basic conservative economics are negative;
- `REJECT`: compliance, safety, or IP red gate.

`CONTINUE RESEARCH` is not sample or purchase approval. Use `references/report-schema.md` for the report.
