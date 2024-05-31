import jsonlines
from datetime import date


class Bond:
    isin: str
    coupon: float
    issue_date: date
    maturity_date: date
    prices: list[float]

    def __init__(self, isin, coupon, issue_date, maturity_date) -> None:
        self.isin = isin
        self.coupon = coupon
        self.issue_date = issue_date
        self.maturity_date = maturity_date
        self.prices = []

    def __str__(self) -> str:
        return self.isin


isin_to_bond = {}

with jsonlines.open('bonds.jsonl') as lines:
    for line in lines.iter(type=dict, skip_invalid=True):
        isin_to_bond[line['ISIN']] = Bond(
            line['ISIN'],
            line['coupon'],
            line['issue date'],
            line['maturity date']
        )

print(isin_to_bond)
