while True:
    print('Please select one of the following:-\n1. Press 1 for read.\n2. Press 2 for write.\n3. Press 3 for delete.\n4. Press q to quit.')
    choice = input('Enter your choice here:- ').lower()
        
    if choice == '1':
        with open("file.txt", 'r') as f: 
            data = f.read()
            print(data)

    elif choice == '2':
        name = input('Enter the name of person:-') 
        age = int(input(f'Etner the age of the {name}:- '))
        degree = input(f'Enter the qualification of the {name}:- ')
        university =  input(f'Enter the unversity/college of {name}:- ')

        details={'Name' : name, 
            'Age' : age, 
            'Degree' : degree, 
            'University' : university} 

        with open("file.txt", 'a') as f: 
            for key, value in details.items(): 
                f.write('%s:%s\n' % (key, value))

    elif choice == '3':
        with open("file.txt", 'r+') as f: 
            f.truncate()
    
    elif choice == 'q':
        break
        
    else:
        print('\nPlease enter a valid choice.\n')