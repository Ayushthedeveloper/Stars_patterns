from pygame import mixer
mixer.init()
mixer.music.load("C:\\Users\\User\\Music\\Peecha Chhute - Lyrical Video _ Ramaiya Vastavaiya _ Girish Kumar, Shruti Haasan ( 128kbps ).mp3")
mixer.music.play()

print("\t\t\t\t\tHello user !! Welcome to my program  :) \n")
print("\t - It is Program Developed by Ayush Kumar Srivsatava \n")
print("Note:- please enter the row number greater than 4 \n")
x = int(input("Select the option from following to display. \n 1. square \n 2. Increasing triangle pattern \n 3. Decreasing triangle pattern \n 4. Right side increasing triangle "
      "\n 4. right side decreasing triangle \n 5. Hill pattern \n 6. Reverse hill pattern \n "
      "7. diamond \n 8. Butterfly \n 9. Pyramid \n 10. Hollow Triangle \n"))

try:
    if x == 1:
        # spuare pattern
        n = int(input("Give the number of rows"))
        for j in range(n):  # outer loop determine the row
            for i in range(n):  # inner loop detremine column
                print("*", end="  ")
            print()
        print()
    elif x == 2:
        #  increasing triangle pattern

        n = int(input("Give the number of rows"))
        for j in range(n):
            for i in range(j + 1):  # range of inner loop will be (j+1)
                print("*", end="  ")
            print()
        print()
    elif x == 3:
        # decreasing triangle pattern
        n = int(input("Give the number of rows"))
        for j in range(n):
            for i in range(j, n):  # range of inner loop will be (i, n)
                print("*", end="  ")
            print()
        print()
    elif x == 4:
        # right side decreasing triangle

        n = int(input("Give the number of rows"))
        for j in range(n):
            for i in range(j):
                print(" ", end=" ")
            for i in range(j, n):
                print("*", end=" ")
            print()
        print()
    elif x == 5:
        # HILL PATTERN

        n = int(input("Give the number of rows"))
        for j in range(n):
            for i in range(j, n):
                print(" ", end=" ")
            for i in range(j + 1):
                print("*", end=" ")
            for i in range(j):
                print("*", end=" ")
            print()
        print()
    elif x == 6:
        # REVERSE HILL PATTERN

        n = int(input("Give the number of rows"))
        for j in range(n):
            for i in range(j + 1):
                print(" ", end=" ")
            for i in range(j, n - 1):
                print("*", end=" ")
            for i in range(j, n):
                print("*", end=" ")
            print()
        print()
    elif x == 7:
        # DIAMOND PATTERN
        n = int(input("Give the number of rows"))
        for i in range(n - 1):
            for j in range(i, n):
                print(" ", end=" ")
            for j in range(i):
                print("*", end=" ")
            for j in range(i + 1):
                print("*", end=" ")
            print()

        for i in range(n):
            for j in range(i + 1):
                print(" ", end=" ")
            for j in range(i, n - 1):
                print("*", end=" ")
            for j in range(i, n):
                print("*", end=" ")
            print()
    elif x == 8 :
        # BUTTTERFLY PATTERN

        n = int(input("Give the number of rows"))
        for i in range(n):
            for j in range(i + 1):
                print("*", end=" ")
            for j in range(i, n - 1):
                print(" ", end=" ")
            for j in range(i, n):
                print(" ", end=" ")
            for j in range(i + 1):
                print("*", end=" ")
            print()

        for i in range(n):
            for j in range(i, n):
                print("*", end=" ")
            for j in range(i):
                print(" ", end=" ")
            for j in range(i + 1):
                print(" ", end=" ")
            for j in range(i, n):
                print("*", end=" ")
            print()
    elif x==9 :
        # PALINDROME TRIANGLE

        n = int(input("Give the number of rows"))
        for i in range(n):
            for j in range(i, n):
                print(" ", end=" ")
            for j in range(i):
                print("*", end=" ")
            for j in range(i + 1):
                print("*", end=" ")
            print()
        print()
    elif x == 10:
        #  Hollow triangle

        n = int(input("Give the number of rows"))
        for i in range(1, n):
            for j in range(1, 8 ):
                if i == 4 or i + j == 5 or j - i == 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    else :
        print("Enter a Valid input")
except Exception as e:
    print(e)

print("Thanks for using my program")






















































