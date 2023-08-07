"""Simple script to print names given as a list."""


def print_names(names):
    """Print names given as a list."""
    if len(names) == 0:
        print("Please add your name.")
    elif len(names) == 1:
        print(f"Hello, my name is {names[0]}.")
    else:
        print("List of names for everyone in cohort 11:")
        for name in names:
            print(f"Hello, my name is {name}.")


def main():
    """Program entry point."""
    names = [
        # Add name here
    ]

    print_names(names)


if __name__ == "__main__":
    main()
