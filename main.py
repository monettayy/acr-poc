def main():
    x = input("Enter your name: ")
    if x == "":
        print("you didnt type anything")
        y = input()
        if y == "":
            print("ok whatever")
        else:
            print("hello " + y)
    else:
        print("hello " + x)

main()
