#!/usr/bin/env python3
"""Calculate chargeable freight weight and landed unit cost."""

import argparse
import json


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--product-cost-cny", type=float, required=True)
    p.add_argument("--exchange-cny-per-usd", type=float, required=True)
    p.add_argument("--units-per-carton", type=float, required=True)
    p.add_argument("--carton-length-cm", type=float, required=True)
    p.add_argument("--carton-width-cm", type=float, required=True)
    p.add_argument("--carton-height-cm", type=float, required=True)
    p.add_argument("--carton-gross-kg", type=float, required=True)
    p.add_argument("--volumetric-divisor", type=float, required=True)
    p.add_argument("--freight-cny-per-kg", type=float, required=True)
    p.add_argument("--packaging-cny", type=float, default=0)
    p.add_argument("--labeling-cny", type=float, default=0)
    p.add_argument("--inspection-cny", type=float, default=0)
    p.add_argument("--domestic-freight-cny", type=float, default=0)
    p.add_argument("--duty-rate", type=float, default=0)
    args = p.parse_args()

    positive = [
        args.product_cost_cny,
        args.exchange_cny_per_usd,
        args.units_per_carton,
        args.carton_length_cm,
        args.carton_width_cm,
        args.carton_height_cm,
        args.carton_gross_kg,
        args.volumetric_divisor,
        args.freight_cny_per_kg,
    ]
    if any(v <= 0 for v in positive):
        p.error("required numeric inputs must be greater than zero")
    if args.duty_rate < 0:
        p.error("duty-rate cannot be negative")

    volume_cm3 = args.carton_length_cm * args.carton_width_cm * args.carton_height_cm
    volumetric_kg = volume_cm3 / args.volumetric_divisor
    chargeable_kg = max(args.carton_gross_kg, volumetric_kg)
    freight_unit_cny = chargeable_kg * args.freight_cny_per_kg / args.units_per_carton
    local_unit_cny = (
        args.product_cost_cny
        + args.packaging_cny
        + args.labeling_cny
        + args.inspection_cny
        + args.domestic_freight_cny
    )
    duty_unit_cny = local_unit_cny * args.duty_rate
    landed_unit_cny = local_unit_cny + duty_unit_cny + freight_unit_cny

    print(json.dumps({
        "carton_volume_cm3": round(volume_cm3, 2),
        "volumetric_weight_kg": round(volumetric_kg, 3),
        "actual_weight_kg": round(args.carton_gross_kg, 3),
        "chargeable_weight_kg": round(chargeable_kg, 3),
        "freight_unit_cny": round(freight_unit_cny, 2),
        "duty_unit_cny": round(duty_unit_cny, 2),
        "landed_unit_cny": round(landed_unit_cny, 2),
        "landed_unit_usd": round(landed_unit_cny / args.exchange_cny_per_usd, 2),
    }, indent=2))


if __name__ == "__main__":
    main()
