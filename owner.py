#  mapping object Relationships

from __init__ import CURSOR, CONN
from bank import Bank

# ("Kelvinss", 11111, 0-73333-3333, "Nairobi", 1)
class Owner():

    all = {}

    def __init__(self, name, id_number, phone, address, bank_id, id = None):
        self.id = id
        self.name = name
        self.id_number = id_number
        self.phone = phone
        self.address = address
        self.bank_id = bank_id

    def __repr__(self):
        return ( f'<Owner {self.id}: {self.name}, {self.id_number} {self.phone}, {self.address}>,' + 
                f'<Bank ID: {self.bank_id}>' )
    
# let's add some properties
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def id_number(self):
        return self._id_number
    @id_number.setter
    def id_number(self, id_number):
        if isinstance(id_number, int):
            self._id_number = id_number
        else:
            raise ValueError("id_number must be an integer")
        
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, phone):
        if isinstance(phone, int):
            self._phone = phone
        else:
            raise ValueError("phone must be an integer")
        
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        if isinstance(address, str) and len(address):
            self._address = address
        else:
            raise ValueError("address must be a non-empty string")
        
    @property
    def bank_id(self):
        return self._bank_id
    @bank_id.setter
    def bank_id(self, bank_id):
        if type(bank_id) is int and Bank.find_by_id(bank_id):
            self._bank_id = bank_id
        else:
            raise ValueError("bank_id must reference a department in the database")



# create a table method to add a column named bank_id to store the relationship as a foreign key in the owners table.
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners(
            id INTEGER PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            id_number INTEGER,
            phone INTEGER,
            address VARCHAR(35) NOT NULL,
            bank_id INTEGER,
            FOREIGN KEY (bank_id) REFERENCES owners(id))
        """
        CURSOR.execute(sql)
        CONN.commit()


# delete table 
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)
        CONN.commit()


# save 
    def save(self):
        sql = """
            INSERT INTO owners (name, id_number, phone, address, bank_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.id_number,
                             self.phone, self.address, self.bank_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

# update 
    def update(self):
        sql = """
        UPDATE owners
        SET name = ?, id_number = ?, phone = ?, address = ?, bank_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id_number, self.phone,
                             self.address, self.bank_id, self.id))
        CONN.commit()

# delete 
    def delete(self):
        sql = """
            DELETE FROM owners WHERE
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
         # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # set the id to None
        self.id = None



# create
    @classmethod
    def create(cls, name, id_number, phone, address, bank_id):
        owner = cls (name, id_number, phone, address, bank_id)
        owner.save()
        return owner


# instance_from_db
    @classmethod
    def instance_from_db(cls, row):
        owner = cls.all.get(row[0])
        if owner:
            owner.name = [1]
            owner.id_number = [2]
            owner.phone = [3]
            owner.address = [4]
            owner.bank_id = [5]
        else:
            owner = cls(row[1], row[2], row[3], row[4], row[5])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner
    
# get_all method
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM owners
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    

# find_by_id
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


# find_by_name
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM owners
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

#  ---> update the Bank class to Compute associated Owner instances




# owner = Owner("Kelvinss", 11111, 0-73333-3333, "Nairobi", 1)

# owner.create_table()
# owner.drop_table()
# owner.save()
# print(owner)

# owner.update()

# owner.create("Kelvin222", 11111, 0-73333-3333, "Nairobi", 1)
# print(owner.create("Kelvin222", 11111, 0-73333-3333, "Nairobi", 1))