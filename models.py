from dataclasses import dataclass
from datetime import datetime

@dataclass
class Trade:
    symbol: str
    quantity: int
    price: float
    trade_type: str  # 'BUY' or 'SELL'
    timestamp: datetime = None

    def __str__(self):
        ts = self.timestamp if self.timestamp else "Now"
        return f"{self.trade_type} {self.quantity} {self.symbol} @ ${self.price} on {ts}"
