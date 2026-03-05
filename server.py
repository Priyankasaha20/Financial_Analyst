from mcp.server.fastmcp import FastMCP
import yfinance as yf

# Initialize the MCP server
mcp = FastMCP("Finance-Multi-Agent")

@mcp.tool()
async def get_stock_price(ticker: str) -> str:
    """Fetches the current price and basic info for a stock ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        current_price = info.get('regularMarketPrice') or info.get('currentPrice')
        return f"The current price of {ticker} is ${current_price}. Sector: {info.get('sector')}"
    except Exception as e:
        return f"Error fetching data for {ticker}: {str(e)}"

if __name__ == "__main__":
    mcp.run()