import add_collect_books
import database

def test_show_collect_books():
    # Arrange
    # Connect to database
    cnx = database.connect_mysql()
    assert cnx is not None, "Connection is OK"
    # Create a cursor object, which is used to execute SQL statements
    cursor = cnx.cursor()

    # Act
    add_collect_books.main()

    # Assert
    cursor.execute("USE library")
    cursor.execute("SELECT * FROM account WHERE account = \"user1\";")
    accounts = cursor.fetchall()
    # Collect_books in account "user1"
    assert accounts[0][7] is "hi", "Book \"hi\" adds to collect_books correctively"
    cursor.close()
    cnx.close()
