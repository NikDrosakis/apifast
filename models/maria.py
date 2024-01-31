# -*- coding: utf-8 -*-
import mariadb
import sys
from typing import Union
from pydantic import BaseModel

class Book(BaseModel):
 title: str
 author: str

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="n130177",
        host="127.0.0.1",
        port=9906,
        database="nikosdrosakisgr"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor


def fetch(id):
	mariac = conn.cursor(prepared=True)
	#mariac.execute(q)
	mariac.execute("SELECT * FROM books WHERE id=?", (id))
	row = mariac.fetchone()
	mariac.close()
	return row

def fetchall(table):
	mariac = conn.cursor(prepared=True)
	mariac.execute("SELECT * FROM " + table)
#	mariac.execute(q)
	row = mariac.fetchall()
	mariac.close()
	return row
	
def insert(q,args):
	mariac = conn.cursor(prepared=True)
	mariac.execute(q, args)
	mariac.commit()
	if mariac.lastrowid:
		return mariac.lastrowid
	else:
		return false
	mariac.close()
def update(q,args):
	mariac = conn.cursor(prepared=True)
	mariac.execute(q, args)
	mariac.commit()
	if mariac.lastrowid:
		return mariac.lastrowid
	else:
		return false
	mariac.close()
def delete(q,args):
	mariac = conn.cursor(prepared=True)
	mariac.execute(q, args)
	mariac.commit()
	if mariac.lastrowid:
		return mariac.lastrowid
	else:
		return false
	mariac.close()

