import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERENCE_USERS_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_FILMS_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_FAVOURITE_FILMS_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user_command(self, telegram_id, username,
                                first_name, last_name):
        self.cursor.execute(sql_queries.START_INSERT_USER_QUERY,
                            (None,
                             telegram_id,
                             username,
                             first_name,
                             last_name,
                             None
                             )
                            )
        self.connection.commit()
    def sql_admin_select_user_command(self):
        self.cursor.row_factory = lambda cursor, row: {
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY
        )

    def sql_insert_user_form_command(self, telegram_id, nickname,
                                     age, PlaceOfBirth, biography, photo):
        self.cursor.execute(sql_queries.INSERT_USER_FORM_QUERY,
                            (None,
                             telegram_id,
                             nickname,
                             age,
                             PlaceOfBirth,
                             biography,
                             photo)
                            )
        self.connection.commit()

    def sql_select_user_form_by_telegram_id_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "PlaceOfBirth": row[4],
            "biography": row[5],
            "photo": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_BY_TELEGRAM_ID_QUERY, (telegram_id,)
        ).fetchall()

    def sql_select_user_forms_command(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "PlaceOfBirth": row[4],
            "biography": row[5],
            "photo": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY
        ).fetchall()

    def sql_insert_like_form_command(self, owner_telegram_id, liker_telegram_id):
        self.cursor.execute(sql_queries.INSERT_LIKE_FORM_QUERY,
                            (None,
                             owner_telegram_id,
                             liker_telegram_id,)
                            )
        self.connection.commit()

    def sql_select_liked_form_command(self, owner_telegram_id, liker_telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "owner_telegram_id": row[1],
            "liker_telegram_id": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_LIKE_FORM_QUERY,
            (owner_telegram_id, liker_telegram_id,)
        ).fetchall()



    def sql_update_user_form_command(self, nickname, age, PlaceOfBirth, biography, photo, telegram_id):
        self.cursor.execute(sql_queries.UPDATE_USER_FORM_QUERY,
                            (nickname,
                             age,
                             PlaceOfBirth,
                             biography,
                             photo,
                             telegram_id,)
                            )
        self.connection.commit()

    def sql_delete_user_form(self, telegram_id):
        self.cursor.execute(sql_queries.DELETE_USER_FORM_QUERY,
                            (telegram_id,)
                            )
        self.connection.commit()

    def sql_update_user_by_link(self, link, telegram_id):
        self.cursor.execute(sql_queries.UPDATE_USER_BY_LINK_QUERY,
                            (link, telegram_id,)
                            )
        self.connection.commit()

    def sql_select_user_link_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_LINK_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_owner_link_command(self, owner_link):
        self.cursor.row_factory = lambda cursor, row: {
            "telegram_id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_OWNER_LINK_QUERY,
            (owner_link,)
        ).fetchall()

    def sql_insert_reference_users(self, owner_telegram_id, reference_telegram_users):
        self.cursor.execute(sql_queries.INSERT_REFERENCE_USERS_QUERY,
                            (None,
                             owner_telegram_id,
                             reference_telegram_users,)
                            )
        self.connection.commit()

    def sql_select_existed_reference_command(self, reference_telegram_users):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_EXIST_REFERENCE_QUERY,
            (reference_telegram_users,)
        ).fetchall()

    def sql_select_all_reference_command(self, owner_telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_REFERENCE_QUERY,
            (owner_telegram_id,)
        ).fetchall()

    def sql_insert_films_command(self, link):
        self.cursor.execute(sql_queries.INSERT_FILMS_QUERY,
                            (None,
                             link,
                             )
                            )
        self.connection.commit()

    def sql_select_specific_films_command(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "link": row[1],
        }
        return self.cursor.execute(
            sql_queries.SELECT_SPECIFIC_FILMS_QUERY,
            (link,)
        ).fetchall()

    def sql_select_specific_films_for_favourite_command(self, films_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_SPECIFIC_FILMS_FOR_FAVOURITE_QUERY,
            (films_id,)
        ).fetchall()

    def sql_insert_favourite_films_command(self, owner_telegram_id, link):
        self.cursor.execute(sql_queries.INSERT_FAVOURITE_FILMS_QUERY,
                            (None,
                             owner_telegram_id,
                             link,
                             )
                            )
        self.connection.commit()

    def sql_select_owner_films_command(self, owner_telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_OWNER_FILMS_QUERY,
            (owner_telegram_id,)
        ).fetchall()


