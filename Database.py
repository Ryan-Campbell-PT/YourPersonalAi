import sqlite3
from datetime import datetime

def runFetchCommand(sqlStatements = []):
    conn = getConnection()
    fetchReturn = []

    for statement in sqlStatements:
        cursor = conn.execute(statement)
        fetchReturn.append([command for command in cursor])

    closeConnection(conn)
    return fetchReturn

def runSetCommand(sqlStatements = []):
    conn = getConnection()

    for sqlString in sqlStatements:
        conn.execute(sqlString)

    closeConnection(conn)
    return

#in the future, can pass a string into this to get different db's
def getConnection():
    conn = sqlite3.connect("events.db")
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        date TEXT NOT NULL
        )
    """)

    conn.commit()
    return conn

def closeConnection(connection):
    connection.commit()
    connection.close()
    return


def getDateFromEnt(ent):
    date = datetime.today().date()
    textLower = ent.text.lower()

    # first start with the basics, simple string recoginition
    if(textLower == "tomorrow"):
        date = date.replace(day= date.day + 1)
        return date
    elif(textLower == "yesterday"):
        date = date.replace(day=date.day - 1)
        return date
    elif(textLower == "today"):
        return date
    
    # if its not a simple string, then hopefully its a month and a date 
    monthAndDate = textLower.replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
    date = datetime.strptime(monthAndDate, "%B %d").replace(year=datetime.today().year).date()

    ## will need to add additional case that includes when just the date is stated, not month
    return date

def saveEventToDB(doc, event):
    for ent in doc.ents:
        date = getDateFromEnt(ent)
        sqlStatement = f"INSERT INTO Events (action, date) VALUES ({event}, '{str(date)}')"

        runSetCommand([sqlStatement])

    return