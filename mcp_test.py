from mcp.server.mcpserver import MCPServer

mcp = MCPServer("teste")

@mcp.tool()
def hello() -> str:
    """Diz olá ao usuário"""
    return "Meu primeiro MCP!"

@mcp.tool()
def sum(a: int, b: int) -> dict[str, int]:
    """Soma dois números"""
    return {'number1': a, 'number2': b, 'result': a + b}