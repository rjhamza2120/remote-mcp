from fastmcp import FastMCP
import random 
import json 

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int, b:int) -> int:
    """Adds two numbers.
    
    Args:
        a: First number to add.
        b: Second number to add.
    
    Returns:
        The sum of a and b."""
    
    return a + b

@mcp.tool
def random_number(min:int=1, max:int=100) -> int:
    """Generates a random number within the range.
    
    Args:
        min: Minimum value (default: 1).
        max: Maximum value (default: 100).
        
    Returns:
        A random integer between min and max."""
    
    return random.randint(min, max)

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server"""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "RJ"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)