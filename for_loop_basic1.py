#Basic - Print all integers from 0 to 150
for count in range (0,151):
    print(count)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
start = 5
end = 1000
for multiFive in range (start, end+1):
    if (multiFive % 5 == 0):
        print(multiFive)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo
start = 1
end = 100
for dojoCount in range (start, end+1 ):
    if (dojoCount % 10 == 0):
        print("Coding Dojo")
    if (dojoCount % 5 == 0):
        print ("Coding")

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
start = 1
end = 500000
odd = 0
for finalSum in range (start, end+1):
    if(finalSum % 2 != 0):
        odd += finalSum
print(odd)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
start = 2018
end = 0
for posNum in range (start, end, -4):
    if posNum % 2 >=0:
        print(posNum)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 0
highNum = 100
multi= 3
for flexCount in range (lowNum, highNum):
    if flexCount % 3 == 0:
        print(flexCount)