from cuadrados import cuadrado

def main():
    while True:
        try:
            num = int(input("Input a number: "))
            if num < 0:
                raise Exception

            if num == 0:
                break
            print(cuadrado(num))

        except Exception as e:
            print("You have got to input a valid number")

if __name__ == "__main__":
    main()
