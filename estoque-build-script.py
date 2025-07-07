import sqlite3

conn = sqlite3.connect("estoque.db")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE produtos (
    codigo        VARCHAR (6)  NOT NULL
                               UNIQUE
                               PRIMARY KEY,
    nome          VARCHAR (20) NOT NULL,
    preco         REAL         NOT NULL,
    quantidade    INTEGER      NOT NULL,
    categorias_id INTEGER,
    FOREIGN KEY (
        categorias_id
    )
    REFERENCES categorias (id) 
);
  """)

cur.execute("""
    CREATE TABLE log_produtos (
    id_log           INTEGER     PRIMARY KEY AUTOINCREMENT,
    data_hora        TEXT        DEFAULT (datetime('now') ),
    tipo_evento      TEXT        NOT NULL,
    valor_anterior   TEXT,
    novo_valor       TEXT,
    codigo_produto   VARCHAR (6) NOT NULL,
    campo            TEXT,
    instancia        INTEGER,
    instancia_codigo VARCHAR,
    FOREIGN KEY (
        codigo_produto
    )
    REFERENCES produtos (codigo) 
);
""")

cur.execute("""
    CREATE TABLE categorias (
    id   INTEGER      PRIMARY KEY AUTOINCREMENT
                      UNIQUE,
    nome VARCHAR (20) NOT NULL
);
""")

conn.commit()