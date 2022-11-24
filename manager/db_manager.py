import sqlite3
from sqlite3 import Error


class DbManager:
    def __init__(self):
        super().__init__()

    def connection(self):
        conn = None
        try:
            conn = sqlite3.connect("./data.db")
            return conn
        except Error as e:
            print(e)

        return conn

    def init_db(self, conn):
        sql_create_team = """CREATE TABLE IF NOT EXISTS teams (
                              id INTEGER not null primary key autoincrement,
                              name VARCHAR(255) NOT NULL ,
                              pokemon_id_1 INT NOT NULL ,
                              pokemon_id_2 INT NOT NULL ,
                              pokemon_id_3 INT NOT NULL ,
                              pokemon_id_4 INT NOT NULL ,
                              pokemon_id_5 INT NOT NULL ,
                              date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"""

        try:
            c = conn.cursor()
            c.execute('PRAGMA foreign_keys = ON')  # Add foreign key support
            c.execute(sql_create_team)
        except Error as e:
            print(e)

    def add_team(self, conn, name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5):
        cur = conn.cursor()
        sql = """INSERT INTO teams (name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5) 
                    VALUES (?,?,?,?,?,?)"""
        cur.execute(sql, (name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5))
        conn.commit()
        return cur.lastrowid

    def fetch_teams(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM teams")
        return cur.fetchall()

    def fetch_team(self, conn, team_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
        return cur.fetchall()

    def update_team(self, conn, team_id, name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5):
        cur = conn.cursor()
        sql = """UPDATE teams SET name = ?,
        pokemon_id_1 = ?,
        pokemon_id_2 = ?,
        pokemon_id_3 = ?,
        pokemon_id_4 = ?,
        pokemon_id_5 = ? WHERE id = ?"""
        cur.execute(sql, (name, pokemon_id_1, pokemon_id_2, pokemon_id_3, pokemon_id_4, pokemon_id_5, team_id))
        conn.commit()
        return cur.lastrowid

    def delete_team(self, conn, team_id):
        sql = 'DELETE FROM teams WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
