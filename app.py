sizes = {}

def main():

    template = int(input("Please choose a template: \n [0] Top \n [1] Bottom \n [2] Custom: "))

    if template == 0:
        keys = ["Bust", "Waist", "Shoulder Width", "Sleeve Length"]
    elif template == 1:
        keys = ["Waist", "Hips", "Length"]
    else:
        keys = None

    for k in keys:
        sizes.update({k: 0})

    if sizes.keys() is None:

        while True: 
            clothesParts = input("Enter the part of those garment being measured (enter exit to stop): ")

            if clothesParts.lower() == "exit":
                break
            else:
                partSize = float(input("Enter the measurement in cm: "))


    else: 
        for k in keys:
            partSize = float(input(f"Enter size in cm for {k}: "))
            sizes.update({k: round((partSize * 0.393701))})

    print(str(sizes))

if __name__ == "__main__":
    main()
