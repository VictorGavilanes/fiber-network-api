import sqlite3

conexion = sqlite3.connect(
    "fiber_network.db",
    check_same_thread=False
)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nodos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    ciudad TEXT NOT NULL
)
""")

conexion.commit()