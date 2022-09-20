print("Select from the options below")
option = int(input("enter 1 for conversion of naira to dollars \nenter 2 for conversion of dollars to naira: "))
if option == 1:
    def naira_to_dollar():
        print("Convert naira to dollar")
        naira = eval(input("Enter the amount in naira"))

        dollars = convert_to_naira(naira)

        print("That is ", dollars, "dollars. ")

    convert_to_naira = lambda naira: naira * 0.0023
    naira_to_dollar()

if option == 2:
    def dollar_naira():
        print("Convert dollars to naira")

        dollars = eval(input("Enter the amount in dollars"))

        naira = convert_to_naira(dollars)

        print("That is ", naira, "naira. ")


    convert_to_naira = lambda dollars: dollars * 429.18
    dollar_naira()
else:
    print("wrong input")
    print("Conversion stopped")
    quit()
