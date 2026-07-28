"""Import positions from CSV export (exchange or wallet)."""
import csv
from core.portfolio import Position

def import_csv(path: str) -> list:
    out = []
    with open(path, newline="") as fp:
        for row in csv.DictReader(fp):
            out.append(Position(ticker=row["ticker"], chain=row.get("chain", "bsc"),
                                qty=float(row["qty"]), cost_basis=float(row["cost_basis"])))
    return out
