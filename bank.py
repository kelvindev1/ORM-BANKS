# first we will import our data base then create a banks table.
from __init__ import CURSOR, CONN


class Bank():

# Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, manager, location, id = None):
        self.id = id
        self.name = name
        self.manager = manager
        self.location = location
    def __repr__(self):
        return f'<Bank {self.id}: {self.name}, located {self.location} is Managed by {self.manager}>'

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
    def manager(self):
        return self._manager
    @manager.setter
    def manager(self, manager):
        if isinstance(manager, str) and len(manager):
            self._manager = manager
        else:
            raise ValueError("Manager must be a non-empty string")

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")


# creating tables
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS banks(
            id INTEGER PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            manager VARCHAR(30) NOT NULL,
            location VARCHAR(35) NOT NULL)
        """
        CURSOR.execute(sql)
        CONN.commit()

# delete for table
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS banks;
        """
        CURSOR.execute(sql)
        CONN.commit()


# mapping object to a table row
    def save(self):
        sql = """
            INSERT INTO banks (name, manager, location)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.manager, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

        # add the current Bank instance to the dict, using row's primary key as the dict key.
        type(self).all[self.id] = self

# create method
    @classmethod
    def create(cls, name, manager, location):
        bank = cls(name, manager, location)
        bank.save()
        return bank
    
# update method
    def update(self):
        sql = """
            UPDATE banks
            SET name = ?, manager = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.manager, self.location, self.id))
        CONN.commit()

# delete method
    def delete(self):
        sql = """
            DELETE FROM banks
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()




# mapping a database row to a python object

# instance_from_db() : maps data stored in banks table row into an instance of Bank.
    @classmethod
    def instance_from_db(cls, row):
        bank = cls.all.get(row[0])
        if bank:
            # ensure attributes match row values in case local object was modified
            bank.name = row[1]
            bank.manager = row[2]
            bank.location = row[3]
        else:
            # if not in dictionary, create new instance and add to dictionary
            bank = cls(row[1], row[2], row[3])
            bank.id = row[0]
            cls.all[bank.id] = bank
        return bank

# get_all() : returns all the banks in the database
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM banks
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]


# find_by_id : similar to get_all but use a WHERE clause.
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM banks
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

# find_by_name : similar to find by id but limits result to first row matching the specified name
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM banks
            WHERE name = ?
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

# delete method :  deletes the table row corresponding to the current Department instance.
    def delete(self):
        sql = """
            DELETE FROM banks
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # set id to None
        self.id = None 



# update of instances from Owner class
    def owners(self):
        from owner import Owner
        sql = """
            SELECT * FROM owners
            WHERE bank_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Owner.instance_from_db(row) for row in rows
            ]




# Branch = Bank("KCB BANK", "Kelvin Mutugi", "Nairobi Tom Mboya Street")
# Branch.create_table()
# Branch.save()
# print(Branch)
# Branch.drop_table()


# Bank.drop_table()
# Bank.create("KCB BANK", "Kelvin Mutugi", "Nairobi Tom Mboya Street")
# Bank.save()

# print(Bank.all)

# print(Bank.get_all())

# print(Bank.find_by_id(1))

# print(Bank.find_by_name("KCB BANK"))

