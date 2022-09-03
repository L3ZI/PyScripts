while True:
    lst = [] #defining list
    for i in range(0,10): #getting user input
        elements = input("Enter your ID card number : ")
        lst.append(elements) #append list


    element1 = lst[0] #list item scraping
    element2 = lst[1]

    concat = ("{}{}".format(element1,element2)) #concatanate scraped elements

    birth_year = "19" + concat  #generating birth year
    concat = int(concat) #converting string to int 
    birth_year = int(birth_year)
    age = 2022 - birth_year #calculating age


    #printing values
    #print("Birth Year ",concat)
    print("Birth Year : ",birth_year)
    print("Age : ",age)
    print("========")
    #print(element1)
    #print(element2)
    #print(lst)
