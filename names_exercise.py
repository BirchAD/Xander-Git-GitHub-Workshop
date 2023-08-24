"""Simple script to print names given as a list."""


def print_names(names):
    """Print names given as a list."""
    if not names:
        print("Please add your name.")
    else:
        if len(names) != 1:
            print("List of names for everyone in cohort 11:")
        for name in names:
            print(f"Hello, my name is {name}.")


def main():
    """Program entry point."""
    names = [
        "Andrew"
    ]

    print("boo")
    print_names(names)


if __name__ == "__main__":
    main()
