# This program developed by Maged Baheig.
# Thanks a lot UDACITY for this great Nanodegree.

# Import required packages for developing the program:
    # time package: for perform required time calc.
    # pandas package: to deal with datasets as df and perform required statistics.
    # sys module: to manipulate different parts of the Python Runtime Environment.
import time
import pandas as pd
import sys


# Create CITY_DATA dictionary contains 'city names' as KEYS,
# and corresponding csv data files' names as VALUES.
CITY_DATA =     {
                'Chicago': 'chicago.csv',
                'Newyork': 'new_york_city.csv',
                'Washington': 'washington.csv'
                }

# Define get_filters() function.
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Create a list for each filter type.
    # Each list contains the accepted user input to proceed.
    city_list = ["C", "N", "W"]
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "All"]
    day_list = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "All"]
    
    # Print a welcome message to user.    
    print('''
                  ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
                  ☺                                             ☺
                  ☺\t✦ Hello! ...                               ☺
                  ☺\t  It gives us pleasure to help you          ☺
                  ☺\t  exploring some US bikeshare data!         ☺
                  ☺                                             ☺
                  ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
    ''')
    
    # Print text demonstrates available data limitations to user.
    print('''
    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    ↓                                                                         \t↓
    ↓\t■ US bikeshare data are avaialble ...                                  \t↓
    ↓\t\t✦ For 3 Cities! ("Chicago", "Newyork", and "Washington").        \t↓
    ↓\t\t✦ During the first six months of 2017 [from Jan-2017 to Jun-2017].\t↓ 
    ↓                                                                         \t↓
    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    ''')
  
    # Print text instructs user how to deal with the program and the required inputs.
    print('''
    ⛊ For the BEST experience,
     Please RUN the program in FULL SCREEN.
          
    ⛊ To abort program at any avaialble interact time,
     Please type (exit) or (e) then press (ENTER).
    
    ⚑ IMPORTANT NOTE: For all required inputs,
     Type your answer WITHOUT parentheses () then press (ENTER).
         ''')



    # Get user input for city (chicago, newyork, or washington). 
    # Use a while loop to handle invalid inputs.
        
    while True: 
        # Repeat below code continously. STOP Only in case of 2 conditions:
            # Condition#1: if exit condition is True.
            # Condition#2: if break condition is True.
        
        # Use 'Try-Except-else' block to handle user input errors.
        try:
            # Guide user with input options & store the input in city variable (will be created below).
            #.title() method used to ensure string case as elements in the created list.
            city = input( 
        """\n\n⛊ To view the available bikeshare data, please type:\n
         The letter (c) for "Chicago" city.
         The letter (n) for "Newyork" city.
         The letter (w) for "Washington" city.\n      
        
        ➤ Your answer for the CITY is:\t """).title() 
        
            # Below is the 1st condition to exit this while loop and exit the whole program
            if city == 'Exit' or city == 'E':
                # Break while loop & exit the whole program if city input == 'Exit' or 'E'.
                # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                print("Loading" , end="")
                for i in range(3, 0, -1):
                    print(".", end="")
                    time.sleep(1)
                    if i == 1:
                        print('')
                # Print text thanks user for his/her time and tells 'program closed'.
                print('''
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                      ↓                                                            ↓
                      ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                      ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                      ↓                                                            ↓
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
          ''')
                # Break while loop & exit the whole program as city input == 'Exit' or 'E'.
                sys.exit()
            # Below is the 2nd condition to break this while loop and continue with next code line.
            elif city in city_list:
                # Break & exit while loop as user city input exist in city_list.
                break            
                
        # Handle [Ctrl + c] keyboard interrupt action.
        # While loop will be restarted at this point.
        except KeyboardInterrupt:
            print('\n\n             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
            print('                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
    
        # Inform user with any other wrong inputs.
        # While loop will be restarted at this point.
        else: 
            print('\n             🠋🠋🠋 Invalid CITY choice!! 🠋🠋🠋')
       
   
    # get user input for month (jan, feb, mar, ... , jun, all)
    # Use a while loop to handle invalid inputs.
        
    while True: 
        # Repeat below code continously. STOP Only in case of 2 conditions:
            # Condition#1: if exit condition is True.
            # Condition#2: if break condition is True.
        
        # Use 'Try-Except-else' block to handle user input errors.
        try:
            # Guide user with input options & store the input in month variable (will be created below).
            #.title() method used to ensure string case as elements in the created list.
            month = input(
        """\n\n⛊ Please detrmine which MONTH do you want to explore, type:\n
         (jan) for "January" month.
         (feb) for "February" month.
         (mar) for "March" month.
         (apr) for "April" month.
         (may) for "May" month.
         (jun) for "June" month.
         (all) for the All "6" months.\n

        ➤ Your answer for the MONTH is:\t """).title()
        
            # Below is the 1st condition to exit this while loop and exit the whole program
            if month == 'Exit' or month == 'E':
                # Break while loop & exit the whole program if month input == 'Exit' or 'E'.
                # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                print("Loading" , end="")
                for i in range(3, 0, -1):
                    print(".", end="")
                    time.sleep(1)
                    if i == 1:
                        print('')
                # Print text thanks user for his/her time and tells 'program closed'.
                print('''
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                      ↓                                                            ↓
                      ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                      ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                      ↓                                                            ↓
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
          ''')
                # Break while loop & exit the whole program as month input == 'Exit' or 'E'.
                sys.exit()
            # Below is the 2nd condition to break this while loop and continue with next code line.
            elif month in month_list:
                # Break & exit while loop as user month input exist in month_list.
                break            
                
        # Handle [Ctrl + c] keyboard interrupt action.
        # While loop will be restarted at this point.
        except KeyboardInterrupt:
            print('\n\n             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
            print('                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
    
        # Inform user with any other wrong inputs.
        # While loop will be restarted at this point.
        else: 
            print('\n             🠋🠋🠋 Invalid MONTH choice!! 🠋🠋🠋')
            
           
    # get user input for day of week (all, monday, tuesday, ... sunday)
    # Use a while loop to handle invalid inputs.
        
    while True: 
        # Repeat below code continously. STOP Only in case of 2 conditions:
            # Condition#1: if exit condition is True.
            # Condition#2: if break condition is True.
        
        # Use 'Try-Except-else' block to handle user input errors.
        try:
            # Guide user with input options & store the input in day variable (will be created below).
            #.title() method used to ensure string case as elements in the created list.
            day = input(
        """\n\n⛊ Please detrmine which DAY do you want to explore, type:\n
         (sun) for "Sunday" day.
         (mon) for "Monday" day.
         (tue) for "Tuesday" day.
         (wed) for "Wednsday" day.
         (thu) for "Thursday" day.
         (fri) for "Friday" day.
         (sat) for "Saturday" day.
         (all) for the All "7" week days.\n

        ➤ Your answer for the DAY is: \t""").title()
        
            # Below is the 1st condition to exit this while loop and exit the whole program
            if day == 'Exit' or day == 'E':
                # Break while loop & exit the whole program if day input == 'Exit' or 'E'.
                # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                print("Loading" , end="")
                for i in range(3, 0, -1):
                    print(".", end="")
                    time.sleep(1)
                    if i == 1:
                        print('')
                # Print text thanks user for his/her time and tells 'program closed'.
                print('''
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                      ↓                                                            ↓
                      ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                      ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                      ↓                                                            ↓
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
          ''')
                # Break while loop & exit the whole program as day input == 'Exit' or 'E'.
                sys.exit()
            # Below is the 2nd condition to break this while loop and continue with next code line.
            elif day in day_list:
                # Break & exit while loop as user day input exist in day_list.
                break            
                
        # Handle [Ctrl + c] keyboard interrupt action.
        # While loop will be restarted at this point.
        except KeyboardInterrupt:
            print('\n\n             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
            print('                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
    
        # Inform user with any other wrong inputs.
        # While loop will be restarted at this point.
        else: 
            print('\n             🠋🠋🠋 Invalid DAY choice!! 🠋🠋🠋')
            
   
    ### CONFIRM USER INPUT STEP ###
        
    # Create an Main if statement displays the 'applied filters' based on user inputs.
    # Get user confirmation input ('yes' or 'no') and store it in confirm variable.
    
    # Confirm variable will be Handled  via 2 BLOCKS as below:

        # BLOCK #1: As long as confirm variable != 'Yes' or 'No',
            # it will be handled in while True block
        
        # BLOCK #2: Once confirm variable == 'Yes' or 'No',
            # it will be handled via if statement block
           
 
    # Main if statement displays the 'applied filters' based on user inputs for city variable.
    # This step added to transform city value from 'city 1st letter' to 'city full name'.
    if city == "C":
        print("\n\n")
        print("%" * 95)
        print("%%", '\t'* 23, "%%")
        print("%%\t\t■  You have chosen to explore US bikeshare data with below applied filters     \t\t %%")
        print('%%\t\t  ', "-" * 72, '\t\t %%')
        print('%%\t\t⛛ Applied Filters:', '\t'*17, '%%')
        print('%%\t\t\t\t\t\t\t✦ City:    ', 'Chicago', '\t'*11, '%%')
        print('%%\t\t\t\t\t\t\t✦ Month(s):', month, '\t'*12, '%%')
        print('%%\t\t\t\t\t\t\t✦ Day(s):  ', day, '\t'*12, '%%')
        print("%%", '\t'* 23, "%%")
        print("%" * 95)
        print("\n\n")
        
        
        # Handle user input in a while True block.
        # Ask user to confirm the 'applied filters'.            
        while True: 
            # Repeat below code continously. STOP Only in case of 2 conditions:
                # Condition#1: if exit condition is True.
                # Condition#2: if break condition is True.
        
            # Use 'Try-Except-else' block to handle user input errors.
            try:
                # Guide user with input options & store the input in confirm variable (will be created below).
                #.title() method used to ensure program string handling consistencey.
                confirm = input('''
                                ⛊ To CONFIRM with above filters,  please type 'yes'.
                                ⛊ To CHANGE filters,              please type 'no'.
                
                                ➤ Your answer is: \t''').title()
                print('')
    
                # Below is the 1st condition to exit this while loop and exit the whole program
                if confirm == 'Exit' or confirm == 'E':
                    # Break while loop & exit the whole program if confirm input == 'Exit' or 'E'.
                    # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                    print("Loading" , end="")
                    for i in range(3, 0, -1):
                        print(".", end="")
                        time.sleep(1)
                        if i == 1:
                            print('')
                    # Print text thanks user for his/her time and tells 'program closed'.
                    print('''
                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                          ↓                                                            ↓
                          ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                          ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                          ↓                                                            ↓
                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
              ''')
                    # Break while loop & exit the whole program as confirm input == 'Exit' or 'E'.
                    sys.exit()
                    
                # Below is the 2nd condition to break this while loop and continue with next code line.
                elif confirm == 'Yes' or confirm == 'No':
                    # Break & exit while loop as user confirm input 'Yes' or 'No'.
                    break            
            
            # Handle [Ctrl + c] keyboard interrupt action.
            # While loop will be restarted at this point.
            except KeyboardInterrupt:
                print('\n\n\t\t\t\t             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
                print('\t\t\t\t                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
        
            # Inform user with any other wrong inputs.
            # While loop will be restarted at this point.
            else: 
                print('\n\t\t\t\t               🠋🠋🠋 Invalid Input!! 🠋🠋🠋')
            
        # Below code will be excuted ONLY if confirm variable == 'No'.
        # Once confirm == 'No', re-call get_filters() function again.
        if confirm == 'No':
            print("\n\n")
            get_filters()
        
        # Below code will be excuted ONLY if confirm variable == 'Yes'.
        # Once confirm == 'Yes', exit this nested-if and return city, month, day.            
        elif confirm == 'Yes':
            print('\n\n► Filters CONFIRMED.')
            # Print 'Please Wait ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
            print("Please Wait" , end="")
            for i in range(4, 0, -1):
                print(".", end="")
                time.sleep(1)
                if i == 1:
                    print('')
            
                         
        city = 'Chicago'
        return city, month, day              
             
        
    
    
    elif city == "N":        
        print("\n\n")
        print("%" * 95)
        print("%%", '\t'* 23, "%%")
        print("%%\t\t■  You have chosen to explore US bikeshare data with below applied filters     \t\t %%")
        print('%%\t\t  ', "-" * 72, '\t\t %%')
        print('%%\t\t⛛ Applied Filters:', '\t'*17, '%%')
        print('%%\t\t\t\t\t\t\t✦ City:    ', 'Newyork', '\t'*11, '%%')
        print('%%\t\t\t\t\t\t\t✦ Month(s):', month, '\t'*12, '%%')
        print('%%\t\t\t\t\t\t\t✦ Day(s):  ', day, '\t'*12, '%%')
        print("%%", '\t'* 23, "%%")
        print("%" * 95)
        print("\n\n")        
       
        
        # Handle user input in a while True block.
        # Ask user to confirm the 'applied filters'.            
        while True: 
            # Repeat below code continously. STOP Only in case of 2 conditions:
                # Condition#1: if exit condition is True.
                # Condition#2: if break condition is True.
        
            # Use 'Try-Except-else' block to handle user input errors.
            try:
                # Guide user with input options & store the input in confirm variable (will be created below).
                #.title() method used to ensure program string handling consistencey.
                confirm = input('''
                                ⛊ To CONFIRM with above filters,  please type 'yes'.
                                ⛊ To CHANGE filters,              please type 'no'.
                
                                ➤ Your answer is: \t''').title()
                print('')
    
                # Below is the 1st condition to exit this while loop and exit the whole program
                if confirm == 'Exit' or confirm == 'E':
                    # Break while loop & exit the whole program if confirm input == 'Exit' or 'E'.
                    # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                    print("Loading" , end="")
                    for i in range(3, 0, -1):
                        print(".", end="")
                        time.sleep(1)
                        if i == 1:
                            print('')
                    # Print text thanks user for his/her time and tells 'program closed'.
                    print('''
                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                          ↓                                                            ↓
                          ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                          ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                          ↓                                                            ↓
                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
              ''')
                    # Break while loop & exit the whole program as confirm input == 'Exit' or 'E'.
                    sys.exit()
                    
                # Below is the 2nd condition to break this while loop and continue with next code line.
                elif confirm == 'Yes' or confirm == 'No':
                    # Break & exit while loop as user confirm input 'Yes' or 'No'.
                    break            
            
            # Handle [Ctrl + c] keyboard interrupt action.
            # While loop will be restarted at this point.
            except KeyboardInterrupt:
                print('\n\n\t\t\t\t             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
                print('\t\t\t\t                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
        
            # Inform user with any other wrong inputs.
            # While loop will be restarted at this point.
            else: 
                print('\n\t\t\t\t               🠋🠋🠋 Invalid Input!! 🠋🠋🠋')
            
        # Below code will be excuted ONLY if confirm variable == 'No'.
        # Once confirm == 'No', re-call get_filters() function again.
        if confirm == 'No':
            print("\n\n")
            get_filters()
        
        # Below code will be excuted ONLY if confirm variable == 'Yes'.
        # Once confirm == 'Yes', exit this nested-if and return city, month, day.            
        elif confirm == 'Yes':
            print('\n\n► Filters CONFIRMED.')
            # Print 'Please Wait ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
            print("Please Wait" , end="")
            for i in range(4, 0, -1):
                print(".", end="")
                time.sleep(1)
                if i == 1:
                    print('')
            
                                
        city = 'Newyork'
        return city, month, day
    
    
    elif city == "W":
        print("\n\n")
        print("%" * 95)
        print("%%", '\t'* 23, "%%")
        print("%%\t\t■  You have chosen to explore US bikeshare data with below applied filters     \t\t %%")
        print('%%\t\t  ', "-" * 72, '\t\t %%')
        print('%%\t\t⛛ Applied Filters:', '\t'*17, '%%')
        print('%%\t\t\t\t\t\t\t✦ City:    ', 'Washington', '\t'*11, '%%')
        print('%%\t\t\t\t\t\t\t✦ Month(s):', month, '\t'*12, '%%')
        print('%%\t\t\t\t\t\t\t✦ Day(s):  ', day, '\t'*12, '%%')
        print("%%", '\t'* 23, "%%")
        print("%" * 95)
        print("\n\n")   
       
        
        # Handle user input in a while True block.
        # Ask user to confirm the 'applied filters'.            
        while True: 
            # Repeat below code continously. STOP Only in case of 2 conditions:
                # Condition#1: if exit condition is True.
                # Condition#2: if break condition is True.
        
            # Use 'Try-Except-else' block to handle user input errors.
            try:
                # Guide user with input options & store the input in confirm variable (will be created below).
                #.title() method used to ensure program string handling consistencey.
                confirm = input('''
                                ⛊ To CONFIRM with above filters,  please type 'yes'.
                                ⛊ To CHANGE filters,              please type 'no'.
                
                                ➤ Your answer is: \t''').title()
                print('')
    
                # Below is the 1st condition to exit this while loop and exit the whole program
                if confirm == 'Exit' or confirm == 'E':
                    # Break while loop & exit the whole program if confirm input == 'Exit' or 'E'.
                    # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                    print("Loading" , end="")
                    for i in range(3, 0, -1):
                        print(".", end="")
                        time.sleep(1)
                        if i == 1:
                            print('')
                    # Print text thanks user for his/her time and tells 'program closed'.
                    print('''
                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                          ↓                                                            ↓
                          ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                          ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                          ↓                                                            ↓
                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
              ''')
                    # Break while loop & exit the whole program as confirm input == 'Exit' or 'E'.
                    sys.exit()
                    
                # Below is the 2nd condition to break this while loop and continue with next code line.
                elif confirm == 'Yes' or confirm == 'No':
                    # Break & exit while loop as user confirm input 'Yes' or 'No'.
                    break            
            
            # Handle [Ctrl + c] keyboard interrupt action.
            # While loop will be restarted at this point.
            except KeyboardInterrupt:
                print('\n\n\t\t\t\t             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
                print('\t\t\t\t                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
        
            # Inform user with any other wrong inputs.
            # While loop will be restarted at this point.
            else: 
                print('\n\t\t\t\t               🠋🠋🠋 Invalid Input!! 🠋🠋🠋')
            
        # Below code will be excuted ONLY if confirm variable == 'No'.
        # Once confirm == 'No', re-call get_filters() function again.
        if confirm == 'No':
            print("\n\n")
            get_filters()
        
        # Below code will be excuted ONLY if confirm variable == 'Yes'.
        # Once confirm == 'Yes', exit this nested-if and return city, month, day.            
        elif confirm == 'Yes':
            print('\n\n► Filters CONFIRMED.')
            # Print 'Please Wait ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
            print("Please Wait" , end="")
            for i in range(4, 0, -1):
                print(".", end="")
                time.sleep(1)
                if i == 1:
                    print('')
            
                         
        city = 'Washington'
        return city, month, day
    
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe based on user input for the city
    df = pd.read_csv(CITY_DATA[city])
    
   
    # convert the 'Start Time' and 'End Time' columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month from 'Start Time' and 'End Time' columns to create new columns
    df['Start Month'] = df['Start Time'].dt.strftime("%b")
    df['End Month'] = df['End Time'].dt.strftime("%b")
      
    # extract day of week from 'Start Time' and 'End Time' columns to create new columns
    df['Start Day'] = df['Start Time'].dt.strftime("%a")
    df['End Day'] = df['End Time'].dt.strftime("%a")
    
    # extract Hour from 'Start Time' and 'End Time' columns to create new columns
    df['Start Hour'] = df['Start Time'].dt.hour
    df['End Hour'] = df['Start Time'].dt.hour
    
    # creating "Trip" column using "Start Station" and "End Station"
    df['Trip'] = df['Start Station'] + "   -TO->   " + df['End Station'] 
    
    
    # Apply filters based on user input for month and day 
    if month != 'All':
        #df[(df.Start Month == month) & (df.Start Day == day)]
        df = df[df['Start Month'] == month]
        
    if  day != 'All':
        df = df[df['Start Day'] == day]

    #TEMP STEP:  
    # Save filterd df into csv file locally to 
    # check filtered data at month and day to validate filter functions
    #df.to_csv('filtered_month.csv', index = False, header=True)
    # HINT: Uncomment above line of code to activate it.
   
    return df
        


# At all below functions, we will create a start_time variable to track the time taken for excyting each function.



def summary_stats(df):
    """Displays a summary statistics for selected data."""

    start_time = time.time()

    print('\n\n')
    print('''
                  
                                                                                  
    Section #1             The main statistics for the selected data           
                                                                                  
                  
            
            ''')      
                  
    print('Calculating summary statistics for selected data ...\n')
    
    print('\n- The numbers of (Rows, Columns) at the selected data are {}.'.format(df.shape))
    print('\n- Selected data has {} values.'.format(df.size))
    print('\n- column labels in the selected data are:')
    for i, v in enumerate(df.columns): #    # print the column labels in the dataframe
        print("\t", i, v)
    print('\n- Selected data has {} NULL values.'.format(df.isnull().sum().sum()))
    print('\n- The Main Descriptive Statistics for the seleceted data are as below:\n')
    print(round(df.describe()))
    print("\n🕘 This statistics Calc took %s seconds.\n\n" % round((time.time() - start_time), 2))



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    start_time = time.time()
    
    print('\n\n')
    print('''
                  
                                                                                  
    Section #2          Statistics on the most frequent times of travel        
                                                                                  
                  
            
            ''')      

    print('Calculating The Most Frequent Times of Travel...\n')

    # display the most common month of travel
    most_common_month = df['Start Month'].mode().values[0]
    print('\n')
    print('Most Popular month:')
    print(most_common_month)

    # display the most common day of week of travel
    most_common_day = df['Start Day'].mode().values[0]
    print('\n')   
    print('Most Popular day:')
    print(most_common_day)
    
    # display the most common start hour of travel
    most_common_hour = df['Start Hour'].mode().values[0]
    print('\n')
    # Use if statement to handle most_common_hour, 
    # to convert time from 24H system to 12H system
    
    if most_common_hour > 12:
        print('Most Popular Start Hour:')
        print(most_common_hour - 12, "PM")
    
    elif most_common_hour == 12:
        print('Most Popular Start Hour:')
        print("12 PM")
              
    elif most_common_hour == 0:
        print('Most Popular Start Hour:')
        print("12 AM")
    else:
        print('Most Popular Start Hour:')
        print(most_common_hour, "AM")
    print("\n🕘 This statistics Calc took %s seconds.\n\n" % round((time.time() - start_time), 2))




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    start_time = time.time()
    
    print('\n\n')
    print('''
                  
                                                                                  
    Section #3           Statistics on the most popular stations and trip      
                                                                                  
                  
            
            ''')     

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # Display most commonly used start station
    most_common_start_station = df['Start Station'].mode().values[0]
    print('\n')
    print('Most Popular start station:')
    print(most_common_start_station)

    # Display most commonly used end station
    most_common_end_station = df['End Station'].mode().values[0]
    print('\n')
    print('Most Popular end station:')
    print(most_common_end_station)

    # Display most frequent combination of start and end station trip
    most_common_trip = df['Trip'].mode().values[0]
    print('\n')
    print('Most Popular trip:')
    print(most_common_trip)
    print("\n🕘 This statistics Calc took %s seconds.\n\n" % round((time.time() - start_time), 2))




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    start_time = time.time()
    
    print('\n\n')
    print('''
                  
                                                                                  
    Section #4          Statistics on the total and average trip duration      
                                                                                  
                  
            
            ''')  

    print('\nCalculating Trip Duration...\n')
    

    # Display total travel time in Seconds
    total_travel_time = int(round(df['Trip Duration'].sum(), 0))
    print('\n')
    print('Total travel time (in Seconds):')
    print(total_travel_time, 'Seconds')
    
    # Display total travel time in Minutes
    total_travel_time = df['Trip Duration'].sum()
    print('\n')
    print('Total travel time (in Minutes):')
    print(int(total_travel_time/60), 'Minutes')
    
    # Display total travel time in Hours
    total_travel_time = df['Trip Duration'].sum()
    print('\n')
    print('Total travel time (in Hours):')
    print(int(total_travel_time/60/60), 'Hours')

    # Display mean travel time in seconds
    avg_travel_time = int(round(df['Trip Duration'].mean(), 0))
    print('\n')
    print('Average travel time (in Seconds):')
    print(avg_travel_time, 'Seconds')

    # Display mean travel time in Minutes
    avg_travel_time = df['Trip Duration'].mean()
    print('\n')
    print('Average travel time (in Minutes):')
    print(int(avg_travel_time/60), 'Minutes')
    print("\n🕘 This statistics Calc took %s seconds.\n\n" % round((time.time() - start_time), 2))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    start_time = time.time()
    
    print('\n\n')
    print('''
                  
                                                                                  
    Section #5                   Statistics on bikeshare users                 
                                                                                  
                  
            
            ''')      

    print('\nCalculating User Stats...\n')


    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('\n')
    print('User Type counts:')
    print(user_type_count)



    # Display counts of gender
    # Use if statement to handle Washington missing Gender data
    if 'Gender' in df.columns:
        gendere_count = df['Gender'].value_counts()
        print('\n')
        print('Gender counts:')
        print(gendere_count)
    else:
        print('\n')
        print('No "Gender data" available for "Washington" City')
        

        
    # Display earliest, most recent, and most common year of birth
    # Use if statement to handle Washington missing Gender Birth Year data
    if 'Birth Year' in df.columns:
        print('\n')
        print('Earliest Birth Year: ', int(round(df['Birth Year'].min(), 0)))
        print('Most Recent Birth Year: ', int(round(df['Birth Year'].max(), 0)))
        print('Most Common Birth Year: ', int(round(df['Birth Year'].mode(), 3).values[0]))
    else:
        print('\n')
        print('No "Birth Year" data available for "Washington" City')
    print("\n🕘 This statistics Calc took %s seconds.\n\n" % round((time.time() - start_time), 2))




def display_rawdata(city):
    """Displays a sample of explored data upon user request."""
    

    # Print a text tells the user that row data is available to check.
    print('\n\n')
    
    print('''
                  ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
                  ☺                                               ☺
                  ☺   Raw data is available to check   ☺
                  ☺                                               ☺
                  ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
    ''')
    
    # As long as this function will take user input more than 1 time with different text Formula,
    # it will be excuted using more than 1 while True block.
    
    # While True BLOCK#1
    # Handle user_request input in a while True block.
    # Ask user if would like to have a look on a sample data of chosen city.            
    while True: 
        # Repeat below code continously. STOP Only in case of 2 conditions:
            # Condition#1: if exit condition is True.
            # Condition#2: if break condition is True.
   
        # Use 'Try-Except-else' block to handle user input errors.
        try:
            # Guide user with input options & store the input in user_request variable (will be created below).
            #.title() method used to ensure program string handling consistencey.
            user_request = input('''
            ⛊ Would you like to view a sample data of chosen city? 
             Please type (yes) or (no).
            
            ➤ Your answer is:\t ''').title()
            print('')

            # Below is the 1st condition to exit this 1st while loop block and exit the whole program
            if user_request == 'Exit' or user_request == 'E':
                # Break 1st while loop & exit the whole program if user_request == 'Exit' or 'E'.
                # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                print("Loading" , end="")
                for i in range(3, 0, -1):
                    print(".", end="")
                    time.sleep(1)
                    if i == 1:
                        print('')
                # Print text thanks user for his/her time and tells 'program closed'.
                print('''
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                      ↓                                                            ↓
                      ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                      ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                      ↓                                                            ↓
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
          ''')
                # Break 1st while loop & exit the whole program as user_request == 'Exit' or 'E'.
                sys.exit()
                
            # Below is the 2nd condition to break this 1st while loop and continue with next code line.
            elif user_request == 'Yes' or user_request == 'No':
                # Break & exit the 1st while loop as user user_input 'Yes' or 'No'.
                break            
        
        # Handle [Ctrl + c] keyboard interrupt action.
        # 1st While loop will be restarted at this point.
        except KeyboardInterrupt:
            print('\n\n\t\t\t\t             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
            print('\t\t\t\t                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
    
        # Inform user with any other wrong inputs.
        # 1st While loop will be restarted at this point.
        else: 
            print('\n\t\t\t\t               🠋🠋🠋 Invalid Input!! 🠋🠋🠋')
    
    
    # Below code will be excuted ONLY if user_request variable == 'No'.
    # Once user_request == 'No', call restart() function to continue with next line code.        
    if user_request == 'No':
        print('\n  You\'r welcome  ☺ ')
        restart()


    # Below code will be excuted ONLY if user_request variable == 'Yes'.
    # Once user_request == 'Yes', it will be handled via another while True block (2nd While loop BLOCK).        
    # (For loop) will be used (inside 2nd while loop) to view a sample of rowdata on chunks.
        
    elif user_request == 'Yes':
        while True:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                start_time = time.time()
                print('\n A Sample of 5 rows from chosen data ...\n')
                print(chunk)
                print("\n🕘 data loading took %s seconds.\n\n" % round((time.time() - start_time)))
                
                # Handle user_request input in another while True block (3rd While loop BLOCK).
                # Ask user if would like to have a look on a sample data of chosen city.
                
                while True: 
                    # Repeat below code continously. STOP Only in case of 2 conditions:
                        # Condition#1: if exit condition is True.
                        # Condition#2: if break condition is True.
                    
                    # Use 'Try-Except-else' block to handle user input errors.
                    # Guide user with input options & store the input in user_request variable (will be created below).
                        #.title() method used to ensure program string handling consistencey.\
                        try:
                            user_request = input(
                            '''
                    ⛊ May you want to look at more data? 
                     Please type (yes) or (no).
            
                    ➤ Your answer is:\t ''').title()
                            print('')
                            # Below is the 1st condition to exit this 3rd while loop block and exit the whole program
                            if user_request == 'Exit' or user_request == 'E':
                                # Break 3rd while loop & exit the whole program if user_request == 'Exit' or 'E'.
                                # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                                    print("Loading" , end="")
                                    for i in range(3, 0, -1):
                                        print(".", end="")
                                        time.sleep(1)
                                        if i == 1:
                                            print('')
                                    # Print text thanks user for his/her time and tells 'program closed'.
                                    print('''
                                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                                          ↓                                                            ↓
                                          ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                                          ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                                          ↓                                                            ↓
                                          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                                          ''')
                                    # Break 3rd while loop & exit the whole program as user_request == 'Exit' or 'E'.
                                    sys.exit()
                                    
                            # Below code will be excuted ONLY if user_request variable == 'No' in for loop.
                            # Once user_request == 'No', call restart() function to continue with next line code.        
                            elif user_request == 'No':
                                # Break & exit while loop as user user_input 'Yes' or 'No'.
                                print('\n  You\'r welcome  ☺ ')
                                restart()
                            
                            # Below code will be excuted ONLY if user_request variable == 'Yes',
                            # in (for loop) which (inside 2nd while loop).
                            # Once user_request == 'Yes', break 3rd while loop, 
                            # and back to (for loop) which (inside 2nd while loop).         
                            elif user_request == 'Yes':
                                break
                        
                        # Handle [Ctrl + c] keyboard interrupt action.
                        # 3rd While loop will be restarted at this point.
                        except KeyboardInterrupt:
                            print('\n\n\t\t\t\t             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
                            print('\t\t\t\t                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
                    
                        # Inform user with any other wrong inputs.
                        # 3rd While loop will be restarted at this point.
                        else: 
                            print('\n\t\t\t\t               🠋🠋🠋 Invalid Input!! 🠋🠋🠋')
                        




def restart():
    """
    Asks user if would like to re-explore the data again or not.

    Returns:
        (function) sys.exit() - abort the program
        (function) main() - restart the program from the begining
    """
    
    # Handle user_input in a while True block.
    # Ask user if would like to re-explore the data again or not.            
    while True: 
        # Repeat below code continously. STOP Only in case of 2 conditions:
            # Condition#1: if exit condition is True.
            # Condition#2: if break condition is True.
    
        # Use 'Try-Except-else' block to handle user input errors.
        try:
            # Guide user with input options & store the input in user_input variable (will be created below).
            #.title() method used to ensure program string handling consistencey.
            user_input = input('''
            ⛊ Would you like to re-explore the data? 
             Please type (yes) or (no).
            
            ➤ Your answer is:\t ''').title()
            print('')

            # Below is the 1st condition to exit this while loop and exit the whole program
            if user_input == 'Exit' or user_input == 'E':
                # Break while loop & exit the whole program if user_input == 'Exit' or 'E'.
                # Print 'Loading ... ' in a for loop with 1sec delay, to add dynamic appearence to the program.
                print("Loading" , end="")
                for i in range(3, 0, -1):
                    print(".", end="")
                    time.sleep(1)
                    if i == 1:
                        print('')
                # Print text thanks user for his/her time and tells 'program closed'.
                print('''
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
                      ↓                                                            ↓
                      ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
                      ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
                      ↓                                                            ↓
                      ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
          ''')
                # Break while loop & exit the whole program as user_input == 'Exit' or 'E'.
                sys.exit()
                
            # Below is the 2nd condition to break this while loop and continue with next code line.
            elif user_input == 'Yes' or user_input == 'No':
                # Break & exit while loop as user user_input 'Yes' or 'No'.
                break            
        
        # Handle [Ctrl + c] keyboard interrupt action.
        # While loop will be restarted at this point.
        except KeyboardInterrupt:
            print('\n\n\t\t\t\t             🠋🠋🠋 NO Input Taken!!! 🠋🠋🠋')
            print('\t\t\t\t                ⚑ To abort program please type (exit) or (e) then press (ENTER)')
    
        # Inform user with any other wrong inputs.
        # While loop will be restarted at this point.
        else: 
            print('\n\t\t\t\t               🠋🠋🠋 Invalid Input!! 🠋🠋🠋')
        
    # Below code will be excuted ONLY if user_input variable == 'No'.
    # Once user_input == 'No', call sys.exit() function to exit the whole program.
    if user_input == 'No':
        print("\n\n")
        print("Loading" , end="")
        for i in range(3, 0, -1):
           print(".", end="")
           time.sleep(1)
           if i == 1:
               print('')
               # Print text thanks user for his/her time and tells 'program closed'.
        print('''
            ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            ↓                                                            ↓
            ↓ --- --- --- ---    Thanks for your time    --- --- --- --- ↓
            ↓ --- --- --- --- ---   Program closed   --- --- --- --- --- ↓
            ↓                                                            ↓
            ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            ''')
        # Exit the whole program as user_input == 'No'.
        sys.exit()
        
        
    # Once user_input == 'Yes', call main() function to restart the program.
    elif user_input == 'Yes':
        main()
        

# List all defined function under the main function 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        summary_stats(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rawdata(city)
        restart()

        
        


if __name__ == "__main__":
	main()
