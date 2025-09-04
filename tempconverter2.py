def Calculate(Degree1,Degree2,num):
    ans = 0
    if Degree1 == "C" and Degree2 == "F":
        ans = ((num*1.8) + 32)
    elif Degree1 == "C" and Degree2 == "K":
        ans = (num + 273.15)
    elif Degree1 == "F" and Degree2 == "C":
        ans = ((num - 32) * 0.5555)
    elif Degree1 == "F" and Degree2 == "K":
        ans = ((num - 32) * 5/9 + 273.15)
    elif Degree1 == "K" and Degree2 == "C":
        ans = (num - 273.15)
    elif Degree1 == "K" and Degree2 == "F":
        ans =  (num - 273.15) * 9/5 + 32
    else:
        print("An error has occured with the function: Calculate")
        pass
    return ans

def Convert(Deg_Type, zero, Deg_Type2):
    Deg_Short = Deg_Type[0]
    Deg2_Short = Deg_Type2[0]
    userin = int(input(f"Enter the degrees in {Deg_Type} that you would like to convert: "))
    if userin < zero:
        print(f"The temperature in {Deg_Type} that you entered is below absolute zero ({zero})°{Deg_Short}, please enter a valid temperature and try again")
    else:
        ans_temp = Calculate(Deg_Short,Deg2_Short,userin)
        print(f"{userin}°{Deg_Short} is equal to {ans_temp}°{Deg2_Short}\n")
        print("Thank you for using the Fahrenheit 404 temperature converter!")

Contin = True
cont = ""
print("Welcome to the Fahrenheit 404 temperature converter!")
while Contin:
    print("What would you like to do?:\n 1.Convert Celcius to Fahrenheit\n 2.Convert Celcius to Kelvin\n 3.Convert Fahrenheit to Celcius\n 4.Convert Fahrenheit to Kelvin\n 5.Convert Kelvin to Celcius\n 6.Convert Kelvin to Fahrenheit")
    user_in_main = int(input("Enter your choice (1 through 6): "))
    if user_in_main == 1:
        Convert("Celcius", -273.15, "Fahrenheit")
    elif user_in_main == 2:
        Convert("Celcius", -273.15, "Kelvin")
    elif user_in_main == 3:
        Convert("Fahrenheit", -459.67, "Celcius")
    elif user_in_main == 4:
        Convert("Fahrenheit", -459.67, "Kelvin")
    elif user_in_main == 5:
        Convert("Kelvin", 0, "Celcius")
    elif user_in_main == 6:
        Convert("Kelvin", 0, "Fahrenheit")
    else:
        print("The provided input is not a valid option, please input a number from one to 6 without spaces or punctuation and try again.")
    cont = input("\nWould you like to continue using the temperature converter(Y for yes N for no): ")
    cont = cont.lower()
    if cont == "y":
        print("Continuing program...\n")
        Contin = True
    elif cont == "n":
        print("Ending program...\n")
        Contin = False
    else:
        print("Invalid input, ending program...\n")
        Contin = False