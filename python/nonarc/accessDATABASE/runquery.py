import pyodbc
connStr = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=\\cool\folder\bro\accessdatabase.mdb;"
    )
cnxn = pyodbc.connect(connStr)
sql = """\
{CALL queryname}
"""
crsr = cnxn.execute(sql)
cnxn.commit()
crsr.close()
cnxn.close()
