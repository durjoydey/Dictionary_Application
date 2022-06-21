dictionary = {}
filename = 'keyword.txt'
z = 0
name = []
description = []
code = []
flag = 0;


def display_dictionary():
    i = len(name)
    y = i - z
    print("Name of the Keyword\t\tDescription of the Keyword\t\tSample Code")
    for x in range(y):
        print(name[x], "\t\t", description[x], "\t\t", code[x])


while True:
    choice = int(input(
        "1.Add Keyword\n 2.Search Keyword\n 3.Display Keyword\n 4.Update Keyword\n 5.Delete Keyword\n 6.File Open\n 7.Exit\n Enter Your Choice:"))

    if choice == 1:
        name.append(str(input("Enter the name of the keyword: ")))
        description.append(str(input("Enter the description of the keyword: ")))
        code.append(str(input("Enter the sample code of the keyword: ")))


    elif choice == 2:
        search_name = input("Enter the name:")
        i = len(name)
        for x in range(i):
            if name[x] == search_name:
                print(search_name, "'s description is", description[x], "and sample code is", code[x])
                flag = 1
        if flag == 0:
            print("keyword wasn't found.\nPlease add this keyword in your dictionary.")
            name.append(str(input("Enter the name of the keyword: ")))
            description.append(str(input("Enter the description of the keyword: ")))
            code.append(str(input("Enter the sample code of the keyword: ")))

    elif choice == 3:

        display_dictionary()

    elif choice == 4:
        n = int(input(
            "1.Edit name of the keyword\n 2.Edit description of the keyword  \n 3.Edit sample code of the keyword \n Enter Your Choice:"))
        if n == 1:
            edit_name = input("Enter the name you want to edit:")
            i = len(name)
            for x in range(i):
                if name[x] == edit_name:
                    name[x] = str(input("Enter new name of the keyword:"))
                    flag = 1
                    display_dictionary()
            if flag == 0:
                print("Keyword isn't found in your dictionary.")
        elif n == 2:
            edit_name = input("Enter the name you want to edit:")
            i = len(name)
            for x in range(i):
                if name[x] == edit_name:
                    description[x] = str(input("Enter new description of the keyword:"))
                    flag = 1
                    display_dictionary()
            if flag == 0:
                print("Keyword isn't found in your dictionary")
        elif n == 3:
            edit_name = input("Enter the name you want to edit:")
            i = len(name)
            for x in range(i):
                if name[x] == edit_name:
                    code[x] = str(input("Enter new sample code of the keyword:"))
                    flag = 1
                    display_dictionary()
            if flag == 0:
                print("Keyword isn't found in your dictionary")

    elif choice == 5:
        dictionary = str(input("Enter the dictionary you want to delete:"))
        i = len(name)
        for x in range(i):
            if name[x] == dictionary:
                if x == i - 1:
                    z += 1
                else:
                    name[x] = name[x + 1]
                    description[x] = description[x + 1]
                    code[x] = code[x + 1]
                    z += 1
    elif choice == 6:
        with open(filename, 'a') as file_object:
            file_object.write(
                "del.\n The del statement in Python is used to delete an object.\n numbers = [1, 2, 3]\n del numbers[0]\n print(numbers)\n")

    else:
        break