
#rate=float(input("Enter your rating:"))
#if(rate>5 or rate<0):
#    print("Invalid rating! Please enter a rating between 0 and 5.")
#else:
#    if(4<rate<=5):
#        print("Excellent")
 #   elif(3<rate<=4):
  #      print("Good")
   # elif(2<rate<=3):
    #    print("Average")
    #elif(1<rate<=2):
    #    print("Poor")
    #else:
    #    print("Very Poor")
print("Welcome to our restaurant!")
print("available options:")
print("1. Veg")
print("2. Non-Veg")
print("3. Chinese")
print("4. Italian")
choice=int(input("Enter your choice:"))
if(choice==1):
    print("You have selected Veg menu")
    print("Items:")
    print("1. dal makhani")
    print("2. dal tadka")
    print("3. paneer butter masala")
elif(choice==2):
    print("You have selected Non-Veg menu")
    print("Items:")
    print("1. chicken curry")
    print("2. mutton korma")
    print("3. fish fry")
elif(choice==3):
    print("You have selected Chinese menu")
    print("Items:")
    print("1. chicken dim sum")
    print("2. alioli noodles")
    print("3. vegetable spring rolls")
elif (choice==4):
    print("You have selected Italian menu")
    print("Items:")
    print("1. margherita pizza")
    print("2. pasta")
    print("3. tiramisu")

else:
    print("Invalid choice")
    print("Thanks for visiting our restaurant!")