import argparse
from database import create_table, insert_trade, query_trades

def main():
    create_table()

    parser = argparse.ArgumentParser(description="Trade Transaction CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: Add trade
    add_parser = subparsers.add_parser("add", help="Add a new trade")
    add_parser.add_argument("symbol", type=str, help="Stock symbol")
    add_parser.add_argument("quantity", type=int, help="Number of shares")
    add_parser.add_argument("price", type=float, help="Price per share")
    add_parser.add_argument("trade_type", choices=["BUY", "SELL"], help="Type of trade")

    # Subcommand: Query trades
    query_parser = subparsers.add_parser("query", help="Query trades")
    query_parser.add_argument("--symbol", type=str, help="Filter by stock symbol")

    args = parser.parse_args()

    if args.command == "add":
        insert_trade(args.symbol, args.quantity, args.price, args.trade_type)
        print(f"✅ Trade added: {args.trade_type} {args.quantity} {args.symbol.upper()} @ ${args.price}")
    elif args.command == "query":
        trades = query_trades(args.symbol)
        if trades:
            print("📊 Trade Records:")
            for trade in trades:
                print("•", trade)
        else:
            print("No trades found.")

if __name__ == "__main__":
    main()
