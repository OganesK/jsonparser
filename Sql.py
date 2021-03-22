import pyodbc

class Sql:
    def __init__(self, database, server):
        self.connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=" + server + ";"
            "Database=" + database + ";"
            "Trusted_Connection=yes;",
            autocommit=True
        )
        self.cursor = self.connect.cursor()
        self.request = ""

    def createTable(self, table, args, types):
        if len(args) != len(types):
            return

        self.request = "CREATE TABLE " + table + " ("
        for i in range(len(args)):
            self.request += str(args[i]) + ' ' + types[i] + ', '
        self.request = self.request[0:-2]
        self.request += ')'
        self.cursor.execute(self.request)

    def select(self, table, args):
        self.request = "SELECT "
        if args[0] != "*":
            for arg in args:
                self.request += str(arg) + ', '
            self.request = self.request[0:-2]
        else:
            self.request += "*"
        self.request += " FROM " + table
        self.cursor.execute(self.request)
        result = self.cursor.fetchall()
        return result


    def insert(self, table, args):
        self.request = "INSERT INTO "
        self.request += table + " VALUES ("
        for arg in args:
            self.request += str(arg) + ', '
        self.request = self.request[0:-2]
        self.request += ')'
        self.cursor.execute(self.request)

