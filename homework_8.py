def work_with_phonebook():
    choice = show_menu()
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    phone_book = read_txt('phon.txt', fields)

    while (choice != 7):
        if choice == 1:                                                     # display data from the file
            print_result(phone_book)

        elif choice == 2:                                                   # find record by lastname
            last_name = input('lastname: ')
            line_num = find_data(phone_book, last_name, "Фамилия")

            if line_num != None:
                change_data(phone_book, line_num)                           # change data
            else:
                print("Record not found!")

        elif choice == 3:                                                   # find record by phone number
            number = input('number: ')
            line_num = find_data(phone_book, number, "Телефон")

            if line_num != None:
                change_data(phone_book, line_num)  # change data
            else:
                print("Record not found!")

        elif choice == 4:                                                   # add a new record
            add_data(phone_book, fields)

        elif choice == 5:                                                   # safe data into a file
            savechoice = savemenu()

            if savechoice == 1:
                write_txt("phon.txt", phone_book)
            elif savechoice == 2:
                write_txt(input("Enter new filename: "), phone_book)
            elif savechoice == 3:
                #considering that the first line number is 1!!!!
                line = input("enter number of lines you want to transfer to a new file (example 1,2,3): ")
                lineList = line.split(",")
                print(lineList)
                data = []

                for i in lineList:
                    data.append(phone_book[int(i)-1])                       # create a new data set with selected records

                write_txt(input("Enter new filename: "), data)              #save selected records into a new file
            elif savechoice == 4:
                print("Saving canceled!\n")


        elif choice == 6:
            check = input("Warning! ALL unsaved data will be LOST!!! Do you want to exit? (Y/N)")                     # you can't rid off me that simple
            if check == "Y" or check == "y":
                return print("....EXIT....")

        choice = show_menu()

#------------------------------------------------------------------------#
#display menu
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Cохранить справочник\n"
          "6. Выйти без сохранения")

    choice = int(input())
    return choice

#------------------------------------------------------------------------#
#display submenu
def submenu():
    print("\nВыберите необходимое действие:\n"
          "1. Изменить номер телефона\n"
          "2. Заменить комментарий\n"
          "3. Добавить комментарий\n"
          "4. Удалить запись\n"
          "5. Вернуться назад в основное меню")

    subchoice = int(input())
    return subchoice

#------------------------------------------------------------------------#
#save submenu
def savemenu():
    print("\nВыберите необходимое действие:\n"
          "1. Перезаписать файл\n"
          "2. Сохранит в новый файл\n"
          "3. Перенести часть дынных в новый файл\n"
          "4. Отмена")

    subchoice = int(input())
    return subchoice

#------------------------------------------------------------------------#
#read data from file
def read_txt(filename, fields):
    phone_book = []

    with open(filename, 'r', encoding = 'utf-8') as data:
        for line in data:
            #remove unwanted whitespace and dublicated spaces
            info = " ".join(line.split())

            #ignore empty lines and create a dictionary
            if info != "":
                list_clean = []
                #remove spaces
                for i in info.split(','):
                    list_clean.append(i.strip())

                record = dict(zip(fields, list_clean))
                phone_book.append(record)

    return phone_book

#------------------------------------------------------------------------#
#1. display data from the file
def print_result(phone_book):
    for line in phone_book:
        print(line)

#------------------------------------------------------------------------#
#2.3. find data
def find_data(phone_book, data_value, data_name):
    N = len(phone_book)

    #run over each line and compare the lastname with a record
    for i in range(N):
        if data_value == phone_book[i][data_name]:
            print(f"Record found!\n{phone_book[i]}")                        # check last name
            return i

#4. add a new record
def add_data(phone_book, fields):
    line = []
    add = "Y"
    print("To add a new record, please, enter the following information!")

    while add == "Y" or add == "y":
        line.append(input('lastname: '))
        line.append(input('firstname: '))
        line.append(input('phone number: '))
        line.append(input('comment(if any): '))

        record = dict(zip(fields, line))
        phone_book.append(record)
        print(f"Following record was addded\n{record}\n")

        add = input("Add a new record? (Y/N)")
        line = []

    return print("Done!")

#------------------------------------------------------------------------#
#safe the file
def write_txt(filename, phone_book):
    with open(filename, 'w', encoding = 'utf-8') as data:
        N = len(phone_book)

        for i in range(N):
            s = ""

            for v in phone_book[i].values():
                s = s + v + ","
            if i < N-1:
                data.write(f"{s[:-1]}\n")
            else:
                data.write(f"{s[:-1]}")                                     # no more empty line at the end of the file

    return print(f"File {filename} has probably been saved!")

#------------------------------------------------------------------------#
#change data
def change_data(phone_book, location):
    subchoice = submenu()
    while (subchoice != 5):

        if subchoice == 1:                                                  # change phone number
            new_number = input('Enter a new number: ')
            phone_book[location]["Телефон"] = new_number
            print("Phone number updated")
        elif subchoice == 2:                                                # replace the comment
            new_comment = input("Enter a new comment: ")
            phone_book[location]["Описание"] = new_comment
            print("Comment replaced")
        elif subchoice == 3:                                                # add a new comment
            new_comment = input("Enter a new comment: ")
            phone_book[location]["Описание"] += " | " + new_comment
            print("Comment added")
        elif subchoice == 4:                                                # delete the record
            del phone_book[location]
            print("Record has been deleted :(")
        elif subchoice == 5:                                                # go back to the main menu
            print("Done!")

        subchoice = submenu()


#run main function
work_with_phonebook()


























