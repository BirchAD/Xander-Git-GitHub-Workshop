def print_names(names):
    if len(names) == 0:
        print("Please add your name.")
    elif len(names) == 1:
        print(f"Hello, my name is {names[0]}.")
    else:
        print("List of names for everyone in cohort 11:")
        for name in names:
            print(f"Hello, my name is {name}.")

def main():
    names = [
        
        # Add name here
        Sabina Pun,
        
    ]

    print_names(names)

if __name__ == "__main__":
    main()