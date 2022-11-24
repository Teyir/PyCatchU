from pages import main_page
from manager import db_manager

# Start sqlite
conn = db_manager.DbManager().connection()
if conn is not None:
    db_manager.DbManager().init_db(conn)
    # db_manager.DbManager().add_team(conn=conn, name="Test", pokemon_id_1=1, pokemon_id_2=2, pokemon_id_3=3, pokemon_id_4=4, pokemon_id_5=5)
    print(db_manager.DbManager().fetch_teams(conn))
    print(db_manager.DbManager().fetch_team(conn, team_id=1))
else:
    print("Error! cannot create the database connection.")


app = main_page.App()
app.mainloop()