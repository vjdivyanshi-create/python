l =[]
while(True):
    print("""
1. Add element 
          2. remove element
          3. Display first three elements
          4. display last three elements
          5. print all elements
          6. exit
          """)
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        e = input("Enter element to add: ")
        l.append(e)
    elif ch == 2: 
        e = input("Enter element to remove: ")
        if e in l:
            l.remove(e)
        else:
            print("Element not found")
    elif ch == 3: 
        print("First three elements: ", l[:3])
    elif ch == 4: 
        print("Last three elements: ", l[-3:])
    elif ch == 5: 
        print("All elements: ", l)
    elif ch == 6: 
        break
    else: 
        print("Invalid choice")