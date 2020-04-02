# pets [] it's a list #

pets = []
while True:
    pets_dict = dict.fromkeys(["pet_name", "pet_age", "pet_species"])
    pets_dict["pet_name"] = input("What is your pet name?")
    pets_dict["pet_age"] = input("What is you pet age?")
    pets_dict["pet_species"] = input("What is your pet species?")
    confirmation = input("Is this information correct?Can we save to our DB? Y/N ?")

    # if user enters Y we will add the information entered to our pets list #
    if confirmation == "Y":
        pets.append(pets_dict)

        addMore = input("Would you like to add more?Y/N?")
        if addMore == "Y":
            continue
        else:
            print("You entered these animals:")
            print("-- " * 18)

            # Access pets dic inside of the list and loop over the keys and values of each dict and print the values#
            for pets_dict in pets:
                for key, values in pets_dict.items():
                    print(values)

            break
