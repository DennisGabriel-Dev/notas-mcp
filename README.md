# agent-mcp

Estudo de servidor MCP em Python. Dois arquivos sobem no Inspector:

- `mcp_test.py` — tools `hello` e `sum`
- `mcp_notas.py` — notas em SQLite (`create_note`, `get_note`)

O banco fica em `data/notas.db` e é criado ao carregar `mcp_notas.py`. A tabela `notas` tem `id`, `titulo`, `texto`, `revisada` e `criada_em`.

## Subir no Inspector

O `mcp dev` usa Node 18+ (aqui, usei a versão 24 do nvm) e o `uv`.

```bash
nvm install 24
nvm use 24
source venv/bin/activate
curl -LsSf https://astral.sh/uv/install.sh | sh
mcp dev mcp_notas.py
```

Abra a URL que o terminal imprimir. Em **Servers**, clique em **Connect**. A aba **Tools** lista as funções.

Para o exemplo de teste sem banco:

```bash
mcp dev mcp_test.py
```

