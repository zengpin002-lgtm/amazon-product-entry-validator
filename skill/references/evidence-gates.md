# Evidence and entry gates

## Required evidence

| Layer | Minimum evidence |
|---|---|
| Market boundary | Direct substitutes, exclusions, filters, period, sample count |
| Demand | Current sales or search evidence with source and date |
| Structure | Product, brand, seller, Top 3 and Top 10 concentration |
| Entry | New-product count, sales share, low-review new-brand examples |
| Reproducibility | Traffic, parent/variant, price, review and Listing advantages |
| Economics | Price, referral fee, FBA estimate, product and freight assumptions |
| Risk | IP, compliance, safety and central product claims |

## Hard gates

- Return `DATA INCOMPLETE` when the direct market or concentration scope is not verified.
- Return `ENTRY_BLOCKED` when direct-market concentration is at least 45% and durable new-brand entry is not verified.
- Return `DATA INCOMPLETE` when new-product count is available but new-product sales share is not.
- Return `LOSS` when conservative contribution profit is not positive.
- Return `REJECT` for a red IP, compliance, or safety gate.

The 45% script trigger is an early-warning threshold. Interpret the provider's exact concentration definition before the final decision.
