import sqlite3
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CAMINHO = RAIZ / "data" / "notas.db"


def conectar() -> sqlite3.Connection:
    CAMINHO.parent.mkdir(parents=True, exist_ok=True)
    conexao = sqlite3.connect(CAMINHO)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar() -> None:
    with conectar() as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                texto TEXT NOT NULL,
                revisada INTEGER NOT NULL DEFAULT 0,
                criada_em TEXT NOT NULL DEFAULT (datetime('now'))
            )
            """
        )
