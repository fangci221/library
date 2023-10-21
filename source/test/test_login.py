import login
import database


def test_login():
    # Arrange
    # Connect to the database
    cnx = database.connect_mysql()
    assert cnx is not None, "Connection is OK"
    # Create a cursor object, which is used to execute SQL statements
    cursor = cnx.cursor()

    # Act
    login.main()

    # Assert
    # Check if the account is created
    cursor.execute("USE library")
    cursor.execute("SELECT * FROM account WHERE account = \"user1\";")
    accounts = cursor.fetchall()
    assert accounts is not None, "User is created"
    cursor.close()
    cnx.close()
