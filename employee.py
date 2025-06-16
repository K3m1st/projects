'''Create Employee Login
You have been contracted to create an employee portal for the company's new timecard system. Start by creating an Employee class with the following attibutes:

 - First Name
 - Last Name
 - Username
 - Password
 - Time Worked
 
**Requirements:**
 - prompt the user to enter the employee's first and last name
 - the init method should create an employee object with a users first and last name
 - the init method will generate the employee's username and password
 - the employee username is automatically created using the first letter of first name + '_' + first 3 letters of last name
 - the password is randomly generated, has a length of 8 - 16 characters and contains the following: at least 1 uppercase letter, 1 lowercase letter, 1 number between [0-9] (i.e. running the program multiple times should produce passwords with no repeatable patterns)
 - the timecard will start at 0 minutes worked for all days of the week ''''

class Employee:
    def __init__(self):
        self.fname = input('Enter your first name: ') # ask for first name
        self.lname = input('Enter your last name: ') # ask for last name
        self.username = (self.fname[0] + '_' + self.lname[0:3]) # First letter of first name + '_' + first 3 letters of last name
        self.password = self._generate_password() # grab and assign returned value from generate_password function
        self.hours = [] # Time worked
        self.minutes = [] # Track minutes worked each day in a list
        self.rate = 12 # Hourly rate.. damn.

    def _generate_password(self):
        # 1) Decide on a random length (8–16)
        import random
        length = random.randint (8,16)
        # 2) Pick one lowercase, one uppercase, one digit
        from string import ascii_lowercase, ascii_uppercase,digits, ascii_letters
        all = ascii_letters + digits # String of all chars and digits
        first_upper = random.choice(ascii_uppercase) # Choose one Uppercase char
        first_lower = random.choice(ascii_lowercase) # Choose one Lowercase char
        first_digit = random.choice(digits) # Choose one digit
        # 3) Pick the rest from the combined pool
        remaining = length - 3 # Subtract the three required characters from the length of the random number (8-16)
        extra = random.choices(all, k=remaining)
        chars = [first_upper, first_lower, first_digit] + extra # Combine three required characters with the remaining number of characters needed
        # 4) Shuffle the list of chars
        random.shuffle(chars)
        # 5) Join into a string and return it
        return ''.join(chars)

    def update_name(self): # Function to update name
        new_fname = input('Enter new first name: ') # Ask for new first name
        new_lname = input('Enter new last name: ') # Ask for new last name
        self.fname = new_fname # Reassign
        self.lname = new_lname # Reassign
        print(f'{self.fname}!, Your new username is below.') # Print new fname
        self.__update_username() # update username

    def __update_username(self): # function to update username
        self.username = self.fname[0] + '_' + self.lname[0:3]  # splicing to create user, same as in init function
        print(f'New username: {self.username}') # Print new username

    def update_password(self): # Update password
        self.__check_password() ## call check password func

    def __check_password(self): # Verify users old password & generate new one
        v = input('Please enter your current password: ') # ask user for current password
        if v != self.password: # if input does not equal current password
            print('Passwords don\'t match! Try again!') # Prompt to try again
            self.__check_password()# Rerun

        else: # verification confirmed
            self.password = self._generate_password()  # Reassign
            print(f'{self.fname}, your password has been updated!') # Tell user pass has been updated
            print(f'Username: {self.username}') # print new username
            print(f'New password: {self.password}') # print new password

    def update_timecard(self):
        tw = input('Please enter the time worked (in minutes) for each day of the week (Su,M,T,W,Th,F,Sa: ') # Ask for time worked this week
        parts = tw.split(',') # Want to turn user input into a list... splitting the commas in the input to assign each day to an index in the list
        self.minutes = [int(p) for p in parts] # Create a list of minutes worked each day based off of user input
        self.hours = [ # Convert mins into hours, backend prep for printing paystub func
        "No hours reported" if m == 0 # No work? No hours reported
        else f"{m//60} hrs {m%60} min" # Else format to hours and minutes
        for m in self.minutes] # for each day of the week
        print(f'{self.fname}, Your timecard has been updated.') # Notify user that their timecard has been updated

    def print_paystub(self):
        print("-" * 80) # we love horizontal lines
        print(f'{self.lname}, {self.fname}')
        print(f'Username: {self.username}')
        print('-' * 40)
        print('HOURS WORKED')
        if not self.minutes: print('No hours reported! Get to work!') # if user chooses print pay stub without entering minutes, tell them no hours are reported
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] # List of days
        pair = zip(days, self.hours) # Join days and hours into a list
        for day, hours in pair: # Print out day and hours worked
            print(f'{day}:{hours}')
        print('-' * 40)
        # Add up for total pay
        tm = sum(self.minutes)  # Sum total minutes for the week
        th = tm / 60 # total hours worked
        pay = th * self.rate # Calculate pay
        print(f'TOTAL PAY: {pay:.2f}') # Print out amount earned including cents
        # Clear timecard
        self.minutes = []
        self.hours = []
        print('Your timecard has been reset.')

#Main function that handles the program flow
def main():
    emp = Employee() # Assign class to a variable
    print(f'Welcome {emp.fname}!, Your login info is below.') # Greet user by first name
    print(f'Employee name: {emp.username}') # Display created username
    print(f'Employee password: {emp.password}') #Display password

    while True: # Run until user exits , print interface
        print('\nChoose from the following:')
        print('1) Update name (username will be updated automatically)')
        print('2) Update Password')
        print('3) Add Hours')
        print('4) Print Paystub')
        print('5) Exit')

        s = input('Choose an option:')
        if s == '1': # Execute update name function
            emp.update_name()
        elif s == '2': # Execute update password
            emp.update_password()
        elif s == '3': # Execute update timecard
            emp.update_timecard()
        elif s =='4': # Execute print paystub
            emp.print_paystub()
        elif s =='5': break # Exit program
        else: # User did not enter a valid num
            print('Please enter a valid option!') # User did not enter val

if __name__ == "__main__":
    main()
