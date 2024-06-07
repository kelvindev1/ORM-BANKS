from helpers import (
    exit_program,
    list_banks,
    find_bank_by_name,
    find_bank_by_id,
    create_bank,
    update_bank,
    delete_bank,
    list_owners,
    find_owner_by_name,
    find_owner_by_id,
    create_owner,
    update_owner,
    delete_owner,
    list_bank_owners
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_banks()
        elif choice == "2":
            find_bank_by_name()
        elif choice == "3":
            find_bank_by_id()
        elif choice == "4":
            create_bank()
        elif choice == "5":
            update_bank()
        elif choice == "6":
            delete_bank()
        elif choice == "7":
            list_owners()
        elif choice == "8":
            find_owner_by_name()
        elif choice == "9":
            find_owner_by_id()
        elif choice == "10":
            create_owner()
        elif choice == "11":
            update_owner()
        elif choice == "12":
            delete_owner()
        elif choice == "13":
            list_bank_owners()
        else:
            print("Invalid choice")





def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all banks")
    print("2. Find bank by name")
    print("3. Find bank by id")
    print("4: Create bank")
    print("5: Update bank")
    print("6: Delete bank")
    print("7. List all owners")
    print("8. Find owner by name")
    print("9. Find owner by id")
    print("10: Create owner")
    print("11: Update owner")
    print("12: Delete owner")
    print("13: List all owners in a bank")


if __name__ == "__main__" :
    main()