"""Reproducible, entirely ILLUSTRATIVE economic scenarios.

This script DOES NOT fit parameters or predict actual AI employment, prices,
consumer welfare, tax needs, or optimal migration rates. It formalises a few
conditional propositions discussed in the article.

Run: python3 models/scenario.py
"""

from dataclasses import dataclass
from math import isfinite
from pathlib import Path
import csv


@dataclass(frozen=True)
class Product:
    price_0: float = 1000.0
    labor_0: float = 400.0
    other_0: float = 200.0
    automatable_labor_share: float = 1.0
    automation_fraction: float = 0.90
    ai_cost_1: float = 40.0
    audit_cost_1: float = 30.0

    def __post_init__(self):
        values = [self.price_0, self.labor_0, self.other_0,
                  self.automatable_labor_share, self.automation_fraction,
                  self.ai_cost_1, self.audit_cost_1]
        if not all(isfinite(v) for v in values):
            raise ValueError('Non-finite scenario values')
        if self.price_0 <= 0 or min(values[1:]) < 0:
            raise ValueError('Price must be positive; costs and shares non-negative')
        if self.automatable_labor_share > 1 or self.automation_fraction > 1:
            raise ValueError('Automation shares must be between 0 and 1')

    @property
    def unit_cost_0(self):
        return self.labor_0 + self.other_0

    @property
    def remaining_labor_ratio(self):
        return 1 - self.automatable_labor_share * self.automation_fraction

    @property
    def unit_cost_1(self):
        return (self.labor_0 * self.remaining_labor_ratio +
                self.other_0 + self.ai_cost_1 + self.audit_cost_1)

    def scenario(self, price_1: float, elasticity: float, q_0: float = 100) -> dict:
        if price_1 <= 0 or elasticity < 0 or q_0 <= 0:
            raise ValueError('price_1 > 0; elasticity >= 0; q_0 > 0')
        ratio = price_1 / self.price_0
        q_1 = q_0 * ratio ** (-elasticity)
        revenue_0 = self.price_0 * q_0
        revenue_1 = price_1 * q_1
        labor_hours_ratio = self.remaining_labor_ratio
        return {
            'scenario_type': 'ILLUSTRATIVE_NOT_ESTIMATED',
            'price_0_EUR': self.price_0,
            'price_1_EUR': price_1,
            'cost_0_EUR': self.unit_cost_0,
            'cost_1_EUR': self.unit_cost_1,
            'margin_0_EUR': self.price_0 - self.unit_cost_0,
            'margin_1_EUR': price_1 - self.unit_cost_1,
            'elasticity_ASSUMED': elasticity,
            'quantity_ratio': q_1 / q_0,
            'revenue_ratio': revenue_1 / revenue_0,
            'labor_hours_ratio_per_unit': labor_hours_ratio,
            'labor_hours_ratio_total': labor_hours_ratio * q_1 / q_0,
            'price_below_cost': price_1 < self.unit_cost_1,
        }


def write_scenarios(path: Path):
    model = Product()
    cases = [
        model.scenario(price_1=1000, elasticity=0.5),
        model.scenario(price_1=500, elasticity=0.5),
        model.scenario(price_1=500, elasticity=1.2),
        model.scenario(price_1=100, elasticity=0.5),
        model.scenario(price_1=100, elasticity=1.0),
        model.scenario(price_1=100, elasticity=1.2),
        model.scenario(price_1=100, elasticity=1.5),
    ]
    path.parent.mkdir(exist_ok=True, parents=True)
    with path.open('w', newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fieldnames=list(cases[0]))
        writer.writeheader()
        writer.writerows(cases)
    print(f'Wrote {len(cases)} illustrative scenarios to {path}')
    print(f'Base cost: €{model.unit_cost_0:.2f}; AI cost: €{model.unit_cost_1:.2f}')


if __name__ == '__main__':
    write_scenarios(Path(__file__).resolve().parent.parent / 'outputs' / 'illustrative_scenarios.csv')
