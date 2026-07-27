# Amazon Product Entry Validator

A free Codex Skill for rejecting weak Amazon product ideas before spending on samples, inventory, or full research.

## What it checks

- direct substitutes versus adjacent alternatives;
- product, brand, seller, Top 3 and Top 10 concentration;
- new-product count, sales share, and low-review new-brand entry;
- winner advantages versus store-reproducible advantages;
- basic conservative economics;
- IP, compliance, and safety red gates.

The Skill returns `CONTINUE RESEARCH`, `DATA INCOMPLETE`, `ENTRY_BLOCKED`, `LOSS`, or `REJECT`. `CONTINUE RESEARCH` is not purchase approval.

## Install

Install or copy the folder at `skill/amazon-product-entry-validator` into your Codex skills directory, then invoke:

```text
Use $amazon-product-entry-validator to validate this Amazon product idea.
```

## Input sources

The Skill can work with current Amazon evidence and user-provided exports. Paid-tool metrics must be supplied by the user or an authorized connector. It never invents proprietary data.

## Pro edition

The separately licensed Pro edition adds purchase-grade SellerSprite workflows, official FBA reconciliation, landed-cost calculation, stress-profit scenarios, inventory exit, automated ranking, and purchase decision reports.

## License

The Lite edition is released under the MIT License. Third-party Amazon, SellerSprite, Keepa, and other product names remain the property of their respective owners.
