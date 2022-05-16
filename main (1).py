def translation(x, y):
    #two dimensional array containing all the significant and unique numerals in roman as well as their arabic counterparts
    library_key = [(0, 1, "I"), (1, 4, "IV"), (2, 5, "V"), (3, 9, "IX"),
                   (4, 10, "X"), (5, 40, "XL"), (6, 50, "L"), (7, 90, "XC"),
                   (8, 100, "C"), (9, 400, "CD"), (10, 500, "D"),
                   (11, 900, "CM"), (12, 1000, "M")]
    #creating the final string an initializing it blank
    roman = ""
    if y == "A":
        #counting the number of thousands in the inputed number and storing it as an int
        ms = int(x) / 1000
        ms = int(ms)
        #adding one m onto the string for every thousand
        i = 0
        while i < ms:
            roman = roman + library_key[12][2]
            i += 1
        #pow_editer counts the digit that the loop is working on, it is what allows me to itterate through the 1000s, 100s, 10s, and 1s place separately
        pow_editer = 1000
        #subtracting all the thousands from the inputed number and storing it as a temp
        temp = int(x) - (ms * pow_editer)
        #loop continues until it goes through every single digit
        while pow_editer > 1:
            #num_next_dij stores the specific number at a digit place
            num_next_dij = int(temp / (pow_editer / 10))
            new_temp = num_next_dij

            o = 0
            #creates an array for all the significant numerals for the digit the program is working through
            sig_values = []
            #iterates through every single value in library_key
            while o < 13:
                #checks to see if the arabic number in the library_key array corresponds with the digit the program is working on and stores the ones that do into the sig_values array
                if (library_key[o][1] /
                    (pow_editer / 10)) >= 1 and (library_key[o][1] /
                                                 (pow_editer / 10)) < 10:

                    sig_values.append(library_key[o])

                o = o + 1
            #once the digit is isolated, the program pulls out roman numerals and subtracts their values after appending them to the string. this continues until the num_next_dij is 0
            while num_next_dij > 0:
                if num_next_dij == 9:
                    roman = roman + "" + sig_values[3][2]
                    num_next_dij = num_next_dij - 9
                elif num_next_dij >= 5 and num_next_dij != 9 and num_next_dij != 4:
                    roman = roman + "" + sig_values[2][2]
                    num_next_dij = num_next_dij - 5
                elif num_next_dij == 4:
                    roman = roman + "" + sig_values[1][2]
                    num_next_dij = num_next_dij - 4
                elif num_next_dij < 4 and num_next_dij > 0:
                    while num_next_dij > 0:
                        roman = roman + "" + sig_values[0][2]
                        num_next_dij = num_next_dij - 1

            #subtracts the value that was stored in the already completed digit and gets a new temp
            temp = (int(temp) - int((new_temp * (pow_editer / 10))))
            #prepares the program to itterate through the next digit by decreasing the power by a factor of 10
            pow_editer = pow_editer / 10
        #prints the completed string after every digit has been counted through separately
        print(roman)
        #adds an explanation for why someone who spammed the numbers may have a few Ms on their screen
        if ms > 4:
            print(
                "there are no numerals officially recognized past 1000, so it can be tricky displaying massive numbers"
            )
    elif y == "R":
        print("roman numeral translation coming soon")


num = 0
while num == 0:
    AorR = input("are you translating an arabic(A) or (R)roman numeral?(A/R)")
    if AorR == "A":
        #gets user input for a number
        Anumber = input("what Arabic number would you like to  translate?")
        #begines filtering out invalid inputs before begining the translation and promting the user for another
        isdigit = True
        try:
            int(Anumber)
        except ValueError:
            isdigit = False
        if isdigit == False:
            print("please do a positive whole number")
        elif int(Anumber) == 0:
            print("nulla")
        elif float(Anumber) < 1 or (float(Anumber) % 1 != 0):
            print("pleyase do a positive whole number :)")
        else:
            translation(Anumber, AorR)
            another = input("woulf you like to translate another?(y/n)")
            if another == "n":
                num += 1
                print("thank you for participating!")
    elif AorR == "R":
        Rnumber = input("what roman numeral would you like to translate?")
        isString = True
        try:
            str(Rnumber)
        except ValueError:
            isString = False
        if isString == False:
            print("please do a Roman Numeral")
        else:
            translation(Rnumber, AorR)
            another = input("woulf you like to translate another?(y/n)")
