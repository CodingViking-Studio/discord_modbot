"""
Databasefunctions for DiscordBot

Contains:
Generate DBs

Creator:    Florian Hillebold
"""
import sqlite3 as sq3

class gen_db():
    """
    Generates all msg-Databases
    and is used to manipulate
    """
    def __init__(self, path_2_db: str) -> None:
        """
        Initialize Databas and generate Tables if needed.

        Args:
            path_2_db (str): Path to databasefile
        """
        self.__db = sq3.connect(database=path_2_db)
        self.__curs = self.__db.cursor()

        # Check and/or create MESSAGES Table
        self.__curs.execute("""
                    SELECT count(name)
                    FROM sqlite_master
                    WHERE type='table'
                    AND name='MESSAGES'
                    """)

        if self.__curs.fetchone()[0] == 1:
            print("Table MESSAGES exists")
        else:
            self.__curs.execute("""
                    CREATE TABLE MESSAGES
                    (UID INTEGER PRIMARY KEY AUTOINCREMENT,
                    MSG_ID CHAR(32),
                    MSG_NAME CHAR(64) NOT NULL,
                    MSG_CONTENT CHAR(255) NOT NULL
                    );""")
            print("Table MESSAGES Created!")

        self.__db.commit()

    def close_connection(self) -> None:
        self.__db.close()

    def add_msg(self, data: dict) -> str:
        """
        Add a msg

        Args:
            data (dict): specified data as List containing
                            - id
                            - name
                            - content
        Return:
            info (str)
        """
        sql_statement = """
                        INSERT INTO MESSAGES
                        (MSG_ID,
                        MSG_NAME,
                        MSG_CONTENT
                        )
                        VALUES(?,?,?)
                        """

        if len(data) > 3:
            print("Too much data given!")
            return "ERROR, contact your Admin"
        else:
            print(f"Adding new msg with then Name {data['name']}")
            self.__curs.execute(
                sql_statement, [data['id'],
                                data['name'],
                                data['content']])
            self.__db.commit()
            return f"Message {data['name']} added to database."

    def check_user(self, msg_name: str) -> tuple:
        """check if a msg is part of the database

        Args:
            msg_name (str): specific message name

        Returns:
            tuple: true or false based on the outcome + msg_uid
        """
        # Get Message based on name
        self.__curs.execute(f"""
                            SELECT *
                            FROM MESSAGES
                            WHERE MSG_NAME='{msg_name}'
                            """)
        data = self.__curs.fetchall()
        if len(data) == 1:
            uid, msg_id, msg_name, msg_content = data[0]
            print(f"""
            The Message with the name {msg_name},
            has been found""")
            return (True, uid)
        elif len(data) > 1:
            print("Es wurden mehrer messages mit dem gleichen Namen gefunden. \
                  Bitte wenden sie sich an ihren Andministrator!")
            return (False, None)
        else:
            print(f"""
            NO Message with the name {msg_name},
            has been found""")
            return (False, None)

    def get_msg(self, msg_name: str) -> list:
        """
        Returns all Message by inputing the name

        Args:
            msg_name (str): message Name

        Returns:
            list: returns a List of all Informations
            for that specific message
        """
        # Get Message based on name
        self.__curs.execute(f"""
                            SELECT *
                            FROM MESSAGES
                            WHERE MSG_NAME='{msg_name}'
                            """)
        extracted_data = self.__curs.fetchall()
        self.__db.commit()
        return extracted_data

    def get_all_msgs(self) -> list:
        """
        Returns all Userdata

        Returns:
            list: returns a List of all Informations
        """
        # Get all Message based
        self.__curs.execute(f"""
                            SELECT *
                            FROM MESSAGES
                            """)
        extracted_data = self.__curs.fetchall()
        self.__db.commit()
        return extracted_data

    def del_msg(self, msg_uid: int, msg_name: str) -> None:
        """
        Delets a specific message

        Args:
            msg_UID (int): UID of the Message that should be deleted!
            msg_name (str): Name of the Message that should be deleted!
        """
        # Get Message based on name
        self.__curs.execute(f"""
                            SELECT *
                            FROM MESSAGES
                            WHERE MSG_NAME='{msg_name}' AND UID='{msg_uid}'
                            """)
        data = self.__curs.fetchall()
        if len(data) == 1:
            uid, msg_id, msg_name, msg_content = data[0]
            print(f"""
            The Message with the message_id {uid} 
            and name {msg_name}, has been found 
            and gets deleted""")

            self.__curs.execute(f"""
                            DELETE
                            from MESSAGES
                            WHERE MESSAGES.UID='{uid}'
                            """)
            
        elif len(data) > 1:
            print("Es wurden mehrer messages mit dem gleichen Namen gefunden. \
                  Bitte wenden sie sich an ihren Andministrator!")
        else:
            print(f"""
            NO Message with the name {msg_name} and 
            messasge_id {msg_uid}, has been found
            """)
        self.__db.commit()

if __name__ == "__main__":
    db_test = gen_db("resources/test.db")

    print(db_test.del_msg(2, "Test2"))