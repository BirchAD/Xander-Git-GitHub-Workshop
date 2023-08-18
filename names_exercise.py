"""Simple script to print names given as a list."""


def print_names(names):
    """Print names given as a list."""
    if not names:
        print("T Oladimeji")
    else:
        if len(names) != 1:
            print("Anastasios", "Ayoub", "James", "Jamie", "Jesus", "Ricardo", "Rupali", "Sabina, Shireen", "Temi", "Toghrul", "Volha", "Zulq")
        for name in names:
            print(f"Hello, my name is {name}.")


def main():
    """Program entry point."""
    names = [
        "T Oladimeji"
    ]

    print("boo")
    print_names(names)


if __name__ == "__main__":
    main()
