#!/usr/bin/env python3
import argparse
import json


def calculate(inputs, price, return_loss_rate):
    referral = price * inputs["referral_rate"]
    advertising = price * inputs["ad_rate"]
    return_loss = price * return_loss_rate
    total = (
        referral
        + inputs["fba_fee"]
        + inputs["landed_cost"]
        + inputs["inbound_fee"]
        + inputs["coupon"]
        + advertising
        + return_loss
        + inputs["storage_allowance"]
    )
    profit = price - total
    return {
        "price": round(price, 2),
        "total_variable_cost": round(total, 2),
        "unit_profit": round(profit, 2),
        "net_margin_pct": round(profit / price * 100, 1) if price else None,
    }


parser = argparse.ArgumentParser()
for name in ["price", "fba_fee", "landed_cost"]:
    parser.add_argument(
        "--" + name.replace("_", "-"),
        type=float,
        required=True,
        dest=name,
    )
parser.add_argument("--referral-rate", type=float, default=0.15)
parser.add_argument("--ad-rate", type=float, default=0.20)
parser.add_argument("--coupon", type=float, default=0)
parser.add_argument("--return-loss-rate", type=float, default=0.03)
parser.add_argument("--storage-allowance", type=float, default=0.20)
parser.add_argument("--inbound-fee", type=float, default=0)
parser.add_argument("--clearance-price", type=float)
args = vars(parser.parse_args())

if args["price"] <= 0 or args["fba_fee"] < 0 or args["landed_cost"] < 0:
    parser.error("price must be positive and costs cannot be negative")

clearance_price = (
    args["clearance_price"]
    if args["clearance_price"] is not None
    else args["price"] * 0.60
)
scenarios = {
    "base": calculate(args, args["price"], args["return_loss_rate"]),
    "price_down_20pct": calculate(
        args, args["price"] * 0.80, args["return_loss_rate"]
    ),
    "returns_doubled": calculate(
        args, args["price"], args["return_loss_rate"] * 2
    ),
    "clearance": calculate(args, clearance_price, args["return_loss_rate"]),
}
scenarios["stress_pass"] = (
    scenarios["price_down_20pct"]["unit_profit"] > 0
    and scenarios["returns_doubled"]["unit_profit"] > 0
)
print(json.dumps(scenarios, ensure_ascii=False, indent=2))
