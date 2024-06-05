from __init__ import CONN, CURSOR

from bank import Bank
from owner import Owner

import ipdb
# Bank.create_table()
# CURSOR.execute("PRAGMA table_info(banks)").fetchall()   a very powerful command for create and delete tables
# Bank.drop_table()

# first create a table by this Bank.create_table()
# insert into the table like: Branch = Bank("KCB BANK", "Kelvin Mutugi", "Nairobi Tom Mboya Street")
# next you save like:  Branch.save()
# execute as you query : banks = CURSOR.execute('SELECT * FROM banks')
# [row for row in banks]

ipdb.set_trace()