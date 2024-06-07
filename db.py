from __init__ import CONN, CURSOR
from bank import Bank
from owner import Owner

def store_database():
        Owner.drop_table()
        Bank.drop_table()
        Bank.create_table()
        Owner.create_table()
        

        # create the data
        branch1 = Bank.create("KCB Bank", "Kelvin Mutugi", "Nairobi, Tom Mboya Street")
        branch2 = Bank.create("Coop-Bank", "Timon Dando", "Nairobi, Haile Sellasie")
        branch3 = Bank.create("Equity Bank", "Mike Robe", "Nairobi, Parliament Road")

        Owner.create("Calvin", 12345678, 254711111111, "Nairobi, Kenya", branch1.id)
        Owner.create("Valentine", 2345679, 254744444444, "Nairobi, kenya", branch1.id)
        Owner.create("Sarafina", 87654321, 254722222222, "Kajiando, kenya", branch2.id)
        Owner.create("Kibet", 87654321, 254733333333, "Kiambu, Kenya", branch3.id)

store_database()

print("Successfully stored the database")

