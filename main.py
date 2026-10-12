import time as t

from requests import session

def main():

    # stores when the coding session starts
    # None means no session is currently active

    start_time = None

    while True:
        print("\n===== DEEPTIMER =====")
        print("1. Start coding session")
        print("2. End coding session")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            # TODO: Implement the logic to start a coding session
            if start_time != None:
                    print("Already running timer!")
                    continue
            print("\nStart session selected.")
            start_time = t.time()
            


        elif choice == "2":
            # TODO: Implement the logic to end a coding session
            print("\nEnd session selected.")

            if start_time == None:
                print("\nThere are no sessions active!")

            
            if start_time != None:
                end_time = t.time()
                duration = int(end_time - start_time)
                print(f"You were locked in for {duration}s")
                start_time = None

        elif choice == "3":
            print("\nExiting...")
            break

        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()