import databasefunctions
def main():
    database_password=input("Password to your database: ")
    databasefunctions.drop_table(database_password)
    databasefunctions.table_creation(database_password)
    databasefunctions.acc_table_overview(database_password)
    pass
if __name__ == '__main__':
    main()