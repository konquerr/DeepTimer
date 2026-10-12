import time as t

from requests import session

def main():

    # stores when the coding session starts
    # None means no session is currently active

    start_time = None

    while True:
        print("===== DEEPTIMER =====")
        print("1. Start coding session")
        print("2. End coding session")
        print("3. Exit")

        choice = input("Select an option:")

        if choice == "1":
            # TODO: Implement the logic to start a coding session
            print("Start session selected.")
        
        elif choice == "2":
            # TODO: Implement the logic to end a coding session
            print("End session selected.")
        
        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()