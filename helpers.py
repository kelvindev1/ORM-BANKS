from bank import Bank
from owner import Owner

def exit_program():
    print("Goodbye!")
    exit()


def list_banks():
    banks = Bank.get_all()
    for bank in banks:
        print(bank)


def find_bank_by_name():
    name = input("Enter bank's name: ")
    bank = Bank.find_by_name(name)
    print(bank) if bank else print(
        f'Bank {name} not found')
    
def find_bank_by_id():
    id_ = input("Enter bank's id: ")
    bank = Bank.find_by_id(id_)
    print(bank) if bank else print(
        f'Bank {id_} not found')
    
def create_bank():
    name = input("Enter the bank's name: ")
    manager = input("Enter the bank's manager: ")
    location = input("Enter the bank's location: ")
    try:
        bank = Bank.create(name, manager, location)
        print(f'Successfully created {bank}')
    except Exception as exc:
        print(f'Error creating bank: ', exc)

def update_bank():
    id_ = input("Enter the bank's id: ")
    if bank := Bank.find_by_id(id_):
        try:
            name = input("Enter the bank's new name: ")
            bank.name = name
            manager = input("Enter the bank's new manager: ")
            bank.manager = manager
            location = input("Enter the bank's new Location: ")
            bank.location = location

            bank.update()
            print(f'You have Successfully updated: {bank}')
        except Exception as exc:
            print(f'Error updating bank: ', exc)
    else:
            print(f'Bank {id_} not found')


def delete_bank():
    id_ = input("Enter the bank's id: ")
    if bank := Bank.find_by_id(id_):

        bank.delete()
        print(f'Bank {id_} successfully deleted')
    else:
        print(f'Bank {id_} was not found')



# owners functions

def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner)

def find_owner_by_name():
    name = input("Enter owner's name: ")
    owner = Owner.find_by_name(name)
    print(owner) if owner else print(
        f"{name} is not a owner's name")
    
def find_owner_by_id():
    id_ = input("Enter owner's id: ")
    owner = Owner.find_by_id(id_)
    print(owner) if owner else print(
        f"{id_} is not a Owner's id")
    
def create_owner():
    name = input("Enter the owner's name: ")
    id_number = input("Enter the owner's id number: ")
    phone = input("Enter the owner's phone number: ")
    address = input("Enter the owner's address: ")
    bank_id = input("Enter the owner's bank id: ")

    try:
        bank = Bank.find_by_id(bank_id)
        if bank:
            owner = Owner.create(name, id_number, phone, address, bank_id)
            print(f'Sucess: {owner}')
    except Exception as exc:
        print(f'Error creating employee: ', exc)

def update_owner():
    id_ = input ("Enter owner's id: ")
    if owner := Owner.find_by_id(id_):
        try:
            name = input("Enter owner's name: ")
            owner.name = name
            id_number = input("Enter owner's ID number: ")
            owner.id_number = int(id_number)
            phone = input("Enter owner's phone number: ")
            owner.phone = int(phone)
            address = input("Enter owner's address: ")
            owner.address = address
            bank_id = input("Enter owner's new bank_id: ")
            owner.bank_id = int(bank_id)

            owner.update()
            print(f'You have successfully updated: {owner}')
        except Exception as exc:
            print(f'Error updating owner: {exc}')
    else:
        print(f'Owner {id_} not found')
    
def delete_owner():
    id_ = input("Enter Owner's id: ")
    if owner := Owner.find_by_id(id_):

        owner.delete()
        print(f"Owner {id_} successfuly deleted")
    else:
        print(f"Owner {id_} was not found")


def list_bank_owners():
    bank_id_ = input("Enter the bank's id: ")
    if bank := Bank.find_by_id(bank_id_):
        owners = bank.owners()
        if owners:
            for owner in owners:
                print(owner)
        else:
            print("No owners found for this bank")
    else:
        print(f'Bank {bank_id_} was not found')
