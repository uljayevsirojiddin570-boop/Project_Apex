while True:
    choice = input("Choose (start/check/exit): ")
    if choice == "start":
        print("Engine started")
    elif choice == "check":
        print("RPM: 1000")
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")