import math,random,time
import threading
def otp():
    def start():
        def generateotp1(n):
            digits="0123456789"
            otp=""
            for i in range(n):
                otp+=digits[math.floor(random.random()*10)]
            return otp
        def generateotp2(n):
            string="abcdefghijklmnopqrstuvwxyz"
            otp=""
            length=len(string)
            for i in range(n):
                otp+=string[math.floor(random.random()*length)]
            return otp
        def generateotp3(n):
            string="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMMOPQRSTUVWXYZ<>!@#$%^&*()"
            otp=""
            length=len(string)
            for i in range(n):
                otp+=string[math.floor(random.random()*length)]
            return otp
        def generateotp6(n):
            string="0123456789abcdefghijklmnopqrstuvwxyz"
            otp=""
            length=len(string)
            for i in range(n):
                otp+=string[math.floor(random.random()*length)]
            return otp
        def generateotp4():
            if a:
                print(generateotp5())
            else:
                print("invaild otp \n")
                choice=int(input("press 1 to generate new otp or 0 to exit \n"))
                if choice==1:
                    start()
                else:
                    print("~~~~~!!!exiting!!!~~~~~")
                    exit()
        def generateotp5():
            print("\n--------------------------------------------------\n")
            print("choose the type of one time password needed \n")
            print("enter 1 for Alphabet password generation")
            print("enter 2 for Alphanumeric password generation")
            print("enter 3 for Alphanumericsymbol password generation")
            print("--------------------------------------------------\n")
            choice=float(input("enter your choice"))
            if choice==1:
                print("--------------------------------------------------\n")
                print("alhabet password generation \n")
                print("--------------------------------------------------\n")
                n=int(input("enter the length of password from('5-10')\n"))
                print("otp will be generated in 5 seconds \n")
                time.sleep(5)
                print("--------------------------------------------------\n")
                print(" one time password is : \t")
                print(generateotp2(n))
                print("\n the password will be sent to your mail \n")
                print("--------------------------------------------------\n")
            elif choice==2:
                print("--------------------------------------------------\n")
                print("alphanumeric password generation \n")
                print("--------------------------------------------------\n")
                n=int(input("enter the length of password from('5-10')\n "))
                print("otp will be generated is 5 seconds \n")
                time.sleep(5)
                print("--------------------------------------------------\n")
                print("one time password is: \t")
                print(generateotp6(n))
                print("\nthe password will be sent to your mail \n")
                print("--------------------------------------------------\n")
            elif choice==3:
                print("--------------------------------------------------\n")
                print("alphanumericsymbol password generation \n")
                print("--------------------------------------------------\n")
                n=int(input("enter the length of password from('5-10')\n "))
                print("otp will be generated is 5 seconds \n")
                time.sleep(5)
                print("--------------------------------------------------\n")
                print("one time password is: \t")
                print(generateotp3(n))
                print("\nthe password will be sent to your mail \n")
                print("--------------------------------------------------\n")
            else:
                print("--------------------------------------------------\n")
                print("enter a valid choice \n")
                choice=int(input("press 1 to generate new otp or 0 to exit \n"))
                if choice==1:
                    print("--------------------------------------------------\n")
                    generateotp4()
                else:
                    print("~~~~~!!!exiting!!!~~~~~\n")
                    print("\n--------------------------------------------------\n")
                    exit()
        def oop():
            print("!!!oops otp has expired!!!~~Exiting~~")
            exit()            
        print("\n--------------------------------------------------\n")
        print("password generation \n")
        print("--------------------------------------------------\n")
        print(generateotp1(4))
        timer=threading.Timer(10.0,oop)
        timer.start()
        print("the otp is valid for 10 seconds!!")
        print("!!kindly enter the above otp correctly!! \n")
        print("--------------------------------------------------\n")
        a=int(input(""))
        timer.cancel()
        generateotp4()
    start()
