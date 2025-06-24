# 📈 Trade Tracker CLI

A simple and lightweight command-line tool to manage and track stock trades using SQLite. Supports adding and querying trades with automatic timestamping.

---

## 🛠 Features

- ✅ Add stock trades (BUY or SELL)
- 🔍 Query all trades or filter by stock symbol
- 💾 SQLite-based persistence
- 💡 Easy-to-use CLI interface

---

## 📁 Project Structure

```
trade-tracker-cli/
├── models.py       # Trade dataclass model
├── database.py     # Database operations (create, insert, query)
├── trade_cli.py    # CLI entrypoint using argparse
└── README.md       # Project documentation
```

---

## 🚀 Run the CLI Tool

### ➕ Add a trade

```bash
python trade_cli.py add AAPL 10 175.5 BUY
```

### 📋 Query all trades

```bash
python trade_cli.py query
```

### 🔍 Query trades for a specific symbol

```bash
python trade_cli.py query --symbol AAPL
```
