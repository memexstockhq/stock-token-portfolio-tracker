"""Portfolio math: P&L, exposure, cost basis."""
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Position:
    ticker: str
    chain: str
    qty: float
    cost_basis: float
    price: float = 0.0

    @property
    def market_value(self) -> float:
        return self.qty * self.price

    @property
    def pnl(self) -> float:
        return (self.price - self.cost_basis) * self.qty

@dataclass
class Portfolio:
    positions: list = field(default_factory=list)

    def exposure_by_chain(self) -> Dict[str, float]:
        out = {}
        for p in self.positions:
            out[p.chain] = out.get(p.chain, 0) + p.market_value
        return out
