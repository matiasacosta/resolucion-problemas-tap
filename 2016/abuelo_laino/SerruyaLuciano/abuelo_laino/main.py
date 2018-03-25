import re

REGEX = re.compile(r'\w*i\w*')
def main():
    cadena = input()

    if not REGEX.match(cadena):
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
