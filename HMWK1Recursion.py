"""
Tovar, Brianna
CS2302, MW 1:30pm-2:50pm
HMWK 1, 8/26, due 8/28
Recursion
"""

#A
def bunnyEars(n):
    if n==0:#Base Case
        return 0
    l=range(n)
    total=0
    if l[n-1]//2: #not sure how to choose number in list,fix later
        return total+3
    else:
        return total+2
print('Letter A:Partial Correct')
print(bunnyEars(0))#returns correct
print(bunnyEars(1))#returns correct
print(bunnyEars(2))#returns incorrect

#B
def sumDigits(n):
    if n==0:#Base Case
        return 0
    else:
        return (n%10) + sumDigits(n//10)
    
print('Letter B:Correct')
print(sumDigits(10))#returns correct
print(sumDigits(28))#returns correct

#C
def count7(n):
    L=[n]
    key=7
    if L==[]:
        return 0
    if L[0]==key:
        return 1+count7(L[1:])
    else:
        return 0
    
print('Letter C:Partial correct')
print(count7(0))#returns correct
print(count7(7297))#returns incorrect
print(count7(777))#returns incorrect

#D
def changeXY(String):
    if String=="":
        return String
    if String[0]=='x':
        return String[0]=='y'
    else:
        return String
    
print('Letter D:Incorrect')
print(changeXY('xX'))#both return false, fix later
print(changeXY('xx'))

#E
def array11(array,key):
    total=0
    if array==[]:
        return 0
    if array[key]==11:#error, fix later
        return total+1
    else:
        return array11(array,key+1)

print('Letter E:Correct')
print(array11([2,11],0))#correct
print(array11([],0))#correct

#F
def array6(array,key):
    if array==[]:
        return 0
    if array[key]==6:
        return True
    else:
        return False
    
print('Letter F:Correct')
print(array6([],0))#correct
print(array6([6,7,8],0))#correct

#G
def nestParen(String):
    if String=="":
        return String
    if String=='(())':#modify to fit more strings, fix later
        return True
    else:
        return False
    
print('Letter G:Correct')
print(nestParen('(())'))#correct
print(nestParen('())'))#correct