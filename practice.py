# # #x=19
# # #print(bytes(x))
# # #import sys
# # #x="karthik"
# # #print(type(x))
# # #print(sys.getsizeof(x))
# # #x=19
# # #print(type(x))
# # #print(sys.getsizeof(x))
# # #x=3.0
# # #print(type(x))
# # #x=10
# # #if(True):
# #  #   print(x)
# #   #  print(x)
# #    # def add():
# #     #    print(x)
# #      #   add()
# # #x=10
# # #y=20
# # #add=x+y
# # #sub =x-y
# # #mul = x*y
# # #div = x/y
# # #flordiv = x//y
# # #pow=x**y
# # #mod =x%y
# # #print(add)
# # #print(sub)
# # #print(mul)
# # #print(div)
# # #print(flordiv)
# # #print(pow)
# # #print(mod)
# # #x=20
# # #y=30
# # #x=x+y
# # #y=x-y
# # #x=x-y
# # #print(x," ",y)
# # print("welcome to srijaaa resturent")
# # print("menu")
# # print("1.non veg,\n2.veg")
# # menu=int(input("enter the menu option:"))
# # match(menu):
# #      case 1:
# #           print("you choose non veg")
# #           print("a. chicken biryani")
# #           print("b.mutton biryani")
# #           print("c.mughaly biryani")
# #           item=input("enter items:")
# #           if item=="a":
# #                print("you selectd chicken biryani")
# #                print("thank you for order")
# #           elif item=="b":
# #                print("you selectd mutton biryani")
# #                print("thank you for order")
# #           elif item=="c":
# #                print("you selectd mughaly biryan")
# #                print("thank you for order")
# #           else:
# #                print("only the menu of non veg")
# #      case 2:
# #           print("you choose veg")
# #           print("a. veg biryani")
# #           print("b.mushrom biryani")
# #           print("c.vanaky biryani")
# #           item=input("enter items:")
# #           if item=="a":
# #                print("you selectd veg biryani")
# #                print("thank you for order")
# #           elif item=="b":
# #                print("you selectd mushrom biryani")
# #                print("thank you for order")
# #           elif item=="c":
# #                print("you selectd vankay biryani")
# #                print("thank you for order")
# #           else:
# #                print("only the menu of veg")
# #                print("thank you for visiting")
# #                print("thank you")
               
# import sys
# # a=20
# # b=3.0
# # c="karthik"
# # d=3+4j
# # e=True
# # print(sys.getsizeof(a))
# # print(sys.getsizeof(b))

# # print(sys.getsizeof(c))

# # print(sys.getsizeof(d))

# # print(sys.getsizeof(e))



# import sys  
# l=[]
# t=()
# s={}
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))
# print(sys.getsizeof(s))
#a=10
# b=a
# c=a
# # d=b
# # c=20
# # d =c
#n=int(input("enter a number"))
# if(n%2==0):
#     print("even number")
# else:
#     print("odd numer")
# n=int(input("enter a number"))
# if(n>0):
#     print( n,"is postive number")
# elif(n==0):
#     print("zero")
# # else:
# #     print(n,"is negative number")
# data=eval(input("enter data:"))
# if type(data) in[int,float,bool,complex]:
#     print("SVDT",data)
# elif type(data) in [str,tuple,list,set,dict]:
# #     print("MVDT",data)
# data=eval(input ("enter a data"))
# if type(data)==str:
#     l=[]
#     l.append(data)
#     print(l)
# data=eval(input("enter a number"))
# if type(data)==int:
#     t=data,
# #     print(t)

# i=1
# while (i<=10):
#     print(i)
#     i=i+1
#i=1
# sum=0
# prod=1
# while(i<=10):
#     sum+=i
#     prod*=i
#     i+=1
# print(sum)
# print(prod)

# n=int(input("enter a number"))
# sum=0
# pro=1
# while n>0:
#     d=n%10
#     sum+=d
#     pro*=d
#     n//=10
# if sum==pro:
#     print("spy number")
# else:
#     print(" not a spy number")
# ch=input("enter a character:")
# if 'a'<=ch<='z':
#     print( "lowercase" ,ch)
# else:
# #     print("not lowercase",ch)
# ch=input("enter a digit:")
# if '0'<=ch<='9':
#     print( "digit" ,ch)
# else:
#     print("not digit",ch)
# ch=input("enter a character:")
# if 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9': b  b  bbbb bb   
# ch=input("enter a character:")
# if  '0'<=ch<='9':
#     print(ord(ch),ch)
# ch=input("enter a character:")
# if  'A'<=ch<='Z':
#     print(ord(ch),ch)

# ch=input("enter a character:")
# if  'a'<=ch<='z' or 'A'<=ch<='Z':
# #     print(ord(ch),ch)
# ch=input("enter a character:")
# if  '0'<=ch<='9':
#     print(ord(ch),ch)
# elif 'a'<=ch<='z' or 'A'<=ch<='Z':
#     print(ord(ch),ch)
# else:
#     l=[]
#     l.append(ch)
#     print(l)
# ch=input("enter a character:")
# if 'a'<=ch<='z':
#     print(chr(ord(ch)-32))
# else:
#     print(chr(ord(ch)+32))
# ch=input("enter a character:")
# if 'A'<=ch<='Z':
#     print(chr(ord(ch)+32))
# # elif 'a'<=ch<='z':
# #     print(chr(ord(ch)-32))
# import random
# secret=35
# guess=34
# print("welcome to number guessing game")
# while guess!=secret:
#     guess=int(input("guess a number:"))
#     if guess==secret:
#         print("hurry!! you won the game")
#         break
# #     elif guess<secret:
# #         print("to0 low")
# #     else:
# #         print("too high")
# password="karthik"
# user_password="karthik@123"
# while user_password!=password:
#     user_password=input("enter your password:")
#     if user_password==password:
#         print("login succesful")