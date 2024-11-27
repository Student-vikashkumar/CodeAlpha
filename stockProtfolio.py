import yfinance as yf
from tabulate import tabulate

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}  # Dictionary to store stocks with shares

    def add_stock(self, ticker, shares):
        """Add stock to the portfolio."""
        ticker = ticker.upper()
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker}.")

    def remove_stock(self, ticker):
        """Remove stock from the portfolio."""
        ticker = ticker.upper()
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from the portfolio.")
        else:
            print(f"{ticker} is not in the portfolio.")

    def fetch_stock_data(self, ticker):
        """Fetch real-time stock data."""
        try:
            stock = yf.Ticker(ticker)
            info = stock.history(period="1d")
            latest_close = info['Close'].iloc[-1]
            return latest_close
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None

    def display_portfolio(self):
        """Display the current portfolio with real-time values."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        table = []
        total_value = 0

        print("\nFetching real-time stock data...\n")
        for ticker, shares in self.portfolio.items():
            price = self.fetch_stock_data(ticker)
            if price is not None:
                value = price * shares
                total_value += value
                table.append([ticker, shares, f"${price:.2f}", f"${value:.2f}"])
            else:
                table.append([ticker, shares, "N/A", "N/A"])

        print(tabulate(table, headers=["Ticker", "Shares", "Price", "Value"], tablefmt="grid"))
        print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")

# Main Program
def main():
    tracker = StockPortfolioTracker()

    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter the stock ticker symbol: ").strip()
            try:
                shares = int(input("Enter the number of shares: "))
                tracker.add_stock(ticker, shares)
            except ValueError:
                print("Invalid input. Shares must be a number.")
        elif choice == "2":
            ticker = input("Enter the stock ticker symbol to remove: ").strip()
            tracker.remove_stock(ticker)
        elif choice == "3":
            tracker.display_portfolio()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
