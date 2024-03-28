import psycopg2

conn = psycopg2.connect(dbname="message", user="iamratnikov", password="vr2609")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE anime (id SERIAL PRIMARY KEY, user_id VARCHAR(50), anime_name VARCHAR(50),"
#                " year INTEGER, rating INTEGER, genre VARCHAR(50), status VARCHAR(50))")
# anime = [("user_2", "Death Note", 2006, 9.2, "detective", "watching"),
#          ("user_3", "Jujutsu Kaisen", 2020, 9.3, "action", "completed"),
#          ("user_5", "Dr. Stone", 2019, 9.3, "adventure", "planning"),
#          ("user_6", "91 Days", 2016, 8.9, "crime", "completed"),
#          ("user_4", "Grand Blue", 2018, 9.5, "comedy", "planning"),
#          ("user_1", "Chainsaw Man", 2022, 9.3, "fantasy", "watching")]
# cursor.executemany("INSERT INTO anime (user_id, anime_name, year, rating, "
#                    "genre, status) VALUES (%s, %s, %s, %s, %s, %s)", anime)
# conn.commit()
cursor.execute("SELECT * FROM anime")
for i in cursor.fetchall():  # noqa C901
    print(f"{i[1]} - {i[2]} - {i[3]}- {i[4]}- {i[5]}- {i[6]}")

# cursor.execute("DROP TABLE orders")
# conn.commit()
cursor.close()
conn.close()
