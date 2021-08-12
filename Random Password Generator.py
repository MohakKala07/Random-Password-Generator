class Foo(object):
    x = 3251

    def _call_(self, limit):
        Foo.x = ((Foo.x * Foo.x) / 100) % 10000
        Foo.x = int(Foo.x)
        return int(Foo.x % limit)


foo = Foo()


def generate_password(len1):
    pass1 = []
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    spchar = ["$","*","#","!","%","&","@"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]

    count = 0
    count_alpha = 0
    count_Alpha = 0
    count_sp = 0
    count_nums = 0
    temp = foo(26)
    pass1.append(alpha[temp])
    count_alpha += 1
    while (count < len1 - 2):
        turn = foo(4)
        if (turn == 0):
            if ((count_Alpha == 1) and (count_sp < 1 or count_alpha < 2 or count_nums < 1)):
                continue
            else:
                temp = foo(26)
                pass1.append(Alpha[temp])
                count += 1
                count_Alpha += 1
        elif (turn == 1):
            if ((count_alpha == 2) and (count_sp < 1 or count_Alpha < 1 or count_nums < 1)):
                continue
            else:
                temp = foo(26)
                pass1.append(alpha[temp])
                count += 1
                count_alpha += 1
        elif (turn == 2):
            if ((count_nums == 1) and (count_Alpha < 1 or count_sp < 1 or count_alpha < 2)):
                continue
            else:
                temp = foo(10)
                pass1.append(nums[temp])
                count += 1
                count_nums += 1
        elif (turn == 3):
            if ((count_sp == 1) and (count_Alpha < 1 or count_alpha < 2 or count_nums < 1)):
                continue
            else:
                temp = foo(7)
                pass1.append(spchar[temp])
                count += 1
                count_sp += 1


    temp = foo(26)
    pass1.append(Alpha[temp])
    print("\n~~~~~~~~~~~~~~~~~~~~\n")
    print("\n\t\tPASSWORD: ")
    print("".join(pass1))
    print("\n~~~~~~~~~~~~~~~~~~~~\n\t")



while (1):
    print("~~~~~~~~~~~~~~~~~~~~\n")
    print("\t\tRANDOM PASSWROD GENERATOR\n")
    print("~~~~~~~~~~~~~~~~~~~~\n\n\n")
    choice = input("\t1. Generate Password\n\t2. Exit\n\n\tEnter your choice(1/2): ")
    choice=int(choice)
    if (choice == 1):
        len1 = input("Enter Required Length: ")
        len1=int(len1)
        if (len1 < 12 or len1 > 32):
            print("\n\t\tERROR!!\n\t(Password should contain at least 12 characters and at max 32 characters) \n\t")


        else:
            generate_password(len1)

    elif (choice == 2):
        exit()

    elif(choice>2 and choice<1):
        print("\n\tINVALID CHOICE!!\n\t")