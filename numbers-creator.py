print('\n\nWelcome to numbers Creator, \nHere you will have the chance to know how number(s) are created using a multiply operation and this apps will help you as well to determine the prime number')
print('Please help yourself, Enjoy..')
x = range (2, (int(input("Insert from zero to how many number? "))+1))
y = 0
for n in x :
    print ("bilangan ke", n, "\n===============================")
    #print ("Kombinasi yang mungkin terjadi adalah")
    y = 0
    for j in range(2,n) :
        # if n%j == 0 :
        if n%j == 0 :
            # while n % j == 0 :
                # if n % j == 0 :
            print (n, " equals ", j, " * ", (int (n/j)))
            y += 1
            # break
         

    if y == 0 :  
        print ("Ini adalah bilangan Prima!!")
    print ("\n")
            