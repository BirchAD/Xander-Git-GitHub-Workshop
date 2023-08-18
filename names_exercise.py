"""Simple script to print names given as a list."""


def print_names(names):
    """Print names given as a list."""
    if not names:
        print("Jamie")
    else:
        if len(names) != 1:
            print("T", "Zulq", "James", "Sabina", "Toghrul", "Shireen", "Ricardo", "Rupali","Ayoub","Temi", "Jesus", "Anastasous")
        for name in names:
            print(f"Hello, my name is {name}.")


def main():
    """Program entry point."""
    names = [
        "Jamie"
    ]

    print("boo")
    print_names(names)


if __name__ == "__main__":
    main()
