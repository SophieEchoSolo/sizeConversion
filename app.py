sizes = {}


def main():
    while True: 
        clothesParts = input("Enter the part of those garment being measured (enter exit to stop): ")

        if clothesParts.lower() == "exit":
            break


        partSize = float(input("Enter the measurement in cm: "))

        if clothesParts.lower() == "exit":
            break

        sizes.update({clothesParts: round((partSize * 0.393701))})

    print(str(sizes))

if __name__ == "__main__":
    main()
