print("!!Welcome to the health management system!!")


def getdate():
    import datetime
    return datetime.datetime.now()


def log_retrieve():
    log_ret = int(
        input("Enter your activity, Please enter 1 to LOG and 2 to RETRIEVE\n"))
    return log_ret


def exc_diet():
    e_d = int(
        input("Enter your activity, Please enter 1 for Excercise and 2 for Diet\n"))
    return e_d


def name():
    n = int(input("Please enter 1 for Harry, 2 for Rohan and 3 for Rishav\n"))
    return n


date = str(getdate())

a = log_retrieve()
b = exc_diet()
c = name()
if (a == 1):
    if(c == 1):
        if(b == 1):
            excerh = input("Enter the excercise\n")
            with open("Harry_Excerise.txt", "a") as f:
                f.write(date[0:19] + " " + excerh + "\n")
                print("Succesfully logged")
        elif(b == 2):
            dieth = input("Enter the diet\n")
            with open("Harry_Diet.txt", "a") as f:
                f.write(date[0:19] + " " + dieth + "\n")
                print("Succesfully logged")
        else:
            print("Please enter proper value\n")

    elif(c == 2):
        if(b == 1):
            excer = input("Enter the excercise\n")
            with open("Rohan_Excerise.txt", "a") as f:
                f.write(date[0:19] + " " + excer + "\n")
                print("Succesfully logged")
        elif(b == 2):
            diet = input("Enter the diet\n")
            with open("Rohan_Diet.txt", "a") as f:
                f.write(date[0:19] + " " + diet + "\n")
                print("Succesfully logged")
        else:
            print("Please enter proper value\n")

    elif(c == 3):
        if (b == 1):
            excerr = input("Enter the excercise\n")
            with open("Rishav_Excerise.txt", "a") as f:
                f.write(date[0:19] + " " + excerr + "\n")
                print("Succesfully logged")
        elif(b == 2):
            dietr = input("Enter the diet\n")
            with open("Rishav_Diet.txt", "a") as f:
                f.write(date[0:19] + " " + dietr + "\n")
                print("Succesfully logged")
    else:
        print("Please enter proper value\n")

elif(a == 2):
    if(c == 1):
        if(b == 1):
            with open("Harry_Excerise.txt") as f:
                for content in f:
                    print(content)
        elif(b == 2):
            with open("Harry_Diet.txt", "a") as f:
                content = f.readline()
                print(content)
        else:
            print("Please enter proper value\n")

    elif(c == 2):
        if(b == 1):
            with open("Rohan_Excerise.txt") as f:
                content = f.read()
                print(content + "\n")
        elif(b == 2):
            with open("Rohan_Diet.txt", "a") as f:
                content = f.read()
                print(content + "\n")
        else:
            print("Please enter proper value\n")

    elif(c == 3):
        if(b == 1):
            with open("Rishav_Excerise.txt") as f:
                for content in f:
                    print(content, end="")
        elif(b == 2):
            with open("Rishav_Diet.txt") as f:
                for content in f:
                    print(content, end="")
        else:
            print("Please enter proper value\n")

else:
    print("Please enter proper value")
