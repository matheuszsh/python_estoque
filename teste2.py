import sqlite3

conn = sqlite3.connect("estoque.db")
cur = conn.cursor()

resp = cur.execute("SELECT quantidade FROM produtos WHERE codigo = '000p01' AND quantidade > 0")

print(resp.fetchone())