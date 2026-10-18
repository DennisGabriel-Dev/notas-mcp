from mcp.server.mcpserver import MCPServer
from typing import Any
from db import inicializar, conectar

inicializar()

mcp = MCPServer("notas")

@mcp.tool()
def create_note(title: str, text: str) -> dict[Any, Any]:
    """Cria uma nova nota"""
    if not title or not text:
        return {'error': 'Título e texto são obrigatórios'}
    with conectar() as conexao:
        cursor = conexao.execute(
            "INSERT INTO notas (titulo, texto) VALUES (?, ?)",
            (title, text),
        )
        nota_id = cursor.lastrowid

    return {"id": nota_id, "title": title, "text": text}


@mcp.tool()
def get_note(id: int) -> dict[Any, Any]:
    """Obtém uma nota específica"""
    if not id:
        return {'error': 'ID é obrigatório'}
    with conectar() as conexao:
        cursor = conexao.execute(
            "SELECT * FROM notas WHERE id = ?",
            (id,),
        )
        nota = cursor.fetchone()
    return {'id': nota['id'], 'title': nota['titulo'], 'text': nota['texto']}