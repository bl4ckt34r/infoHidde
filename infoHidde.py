# Dependence for move in the paths
import os
# Dependence for get the username
import getpass

# Tuples for the change of number and signs
change_numbers = ["O", "i", "z", "E", "A", "S", "G", "T", "0", "g"]
change_number_signs = ["-", "^", "+"]
# String with all the characters that be can use in the tool
letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.@!#%|:*^-+"
# Variables that save the paths
your_path = os.getcwd()
file_path = 0
# Variable that save the new data
data_changed = ""
# Variable that save the displace of the characters
displace_number = ""
# Variable that save the sign of the displace (pos, right; neg, left)
sign = ""
# Variable that save the name of the file
file_name = 0
# Variable that save the data in the selected file
file_data = ""
# Action selectioned by the user
user_selection = 0
# Variable used when with a relative path as an input
is_in_path = False

# Function with the tool is started
def initTool():
    # Print banner an options of the tool
    print("    _       ____      __  ___     __    __   ")
    print("   (_)___  / __/___  / / / (_)___/ /___/ /__ ")
    print("  / / __ \/ /_/ __ \/ /_/ / / __  / __  / _ \ ")
    print(" / / / / / __/ /_/ / __  / / /_/ / /_/ /  __/")
    print("/_/_/ /_/_/  \____/_/ /_/_/\__,_/\__,_/\___/ ")
    print("")
    print("=========== Created by: bl4ckt3ar ===========")
    print("")
    print("1-. Crypt\n2-. Decrypt\n0-. Exit")

    # Select the global variables that be use
    global user_selection
    user_selection = int(input("Enter your selection --> "))

    # Validate the user selection, 1 & 2 is valid, 0 exit, every other not valid
    if user_selection == 1 or user_selection == 2:
        # Check the input of the path and file
        checkPathAndFile()
    elif user_selection == 0:
        # End the execution of the tool
        print("Exiting of the tool...!")
        endTool()
    else:
        # Request the data agin
        print("Invalid selection, try again, or use 0 to exit")
        initTool()

# Function to show a message and end the execution
def endTool():
    print("Ending the execution of the tool infoHidde")

# Function to validate the filename and path
def checkPathAndFile():
    # Select the global variables
    global file_name
    global file_path
    global is_in_path

    # Request the file of the path to the user
    print("\nEnter the path of your file")
    file_path = input("(use txt files, can use relative paths . and ~) -->")
    # Split the path to get te filename
    paths = file_path.split("/")
    # Extract the filename of the path
    file_name = paths[-1]
    # Extract file type of the filename
    file_type = file_name.split(".")

    # Validate the file type, as type text
    if(file_type[-1] != "txt"):
        print("The file type is invalid, only works with txt files")
        # Restart the executiuon tool for a invalid file type
        initTool()

    # Return the string file path a empty string
    file_path = ""
    # Check if the user input the relative home directory in the input path
    home_directory = False
    # Check the username, to create a home directory
    username = getpass.getuser()

    # Loop to iterate for all the parts of the path
    for word in paths[0:-1]:
        # If use the relative path of ".", declare the file path in actual path
        if word == ".":
            file_path = os.getcwd()
            is_in_path = True
            # Stop the loop 
            break;

        # Create the file path, for obtain the file path in case of use a
        # relative path in the input path
        file_path = file_path + "/" + word

        # Check if using the relative path of "~"
        if word == "~":
            # Check the user is executing the tool to build the path
            if username == "root":
                file_path = "/root"
            else:
                file_path = "/home/" + username

    # Check if need to change the path, if this true change the path with os
    if not is_in_path:
        os.chdir(file_path)
        print("Changing path...")

    # Call the function to read the content of the file
    readFileData()

# Function to read the data of the file and change this data
def readFileData():
    # Select the global variables
    global user_selection
    global file_data

    # Open and read the lines of the selected file
    file = open(file_name, "r")
    file_data = file.readlines()

    # Iterate for all the lines of the file
    for line in file_data:
        # Call the option selected by the user (Crypo or decrypt)
        if user_selection == 1:
            cryptData(line)
        elif user_selection == 2:
            decryptData(line)

    # Close the file, for good practice
    file.close()
    # Call the function to write the data in the file
    writeFileData()

# Function to write te changed data in the selected file
def writeFileData():
    # Select the global variable
    global data_changed

    # Open the file in write mode, write the new data in the file,
    # close the file for good practice, and call the function to end the tool
    file = open(file_name, "w")
    file.write(data_changed)
    file.close()
    endTool()

# Function to encrypt the data
def cryptData(data):
    # Select the global variables to be use
    global displace_number
    global file_data
    global sign
    global data_changed

    # Request to the user the displace number for the chararcters
    displace_number = int(input("Enter displace number --> "))
    # Get the side of the move, with the sign (pos -> right, neg -> left)
    getSign()

    # Iterate all the characters of the data to move at the new position
    for data_letters in data:
        # Select the actual position, calculate the final position
        # and save the changed character in a string
        list_position = letters.find(data_letters)
        final_position = getFinalPositionCrypt(displace_number, list_position, len(letters))
        data_changed = data_changed + letters[final_position]

    # Data used to calculate the changed sign
    abs_value = abs(displace_number)
    current_pos = change_number_signs.index(sign)
    odds = len(change_number_signs)
    # Calculate the chanfed sign, and add to the data changed
    data_changed = data_changed + change_number_signs[getFinalPositionCrypt(abs_value, current_pos, odds)]

    # Encrypt the displace of the characters
    for nums in str(displace_number):
        # Check if the current character is a number
        if nums.isdigit():
            # If a number add the changed date to the, data changed string
            data_changed = data_changed + change_numbers[int(nums)]

    # Add a line break for end with current line and work with the next
    data_changed = data_changed + "\n"

# Function to decrypt the data, encrypted by the encrypt function
def decryptData(data_in):
    # Select the global variables
    global sign
    global sign_position
    global displace_number
    global data_changed

    # Save the signs positions, to get the sign with the encryption
    sign_position_list = []

    # Loop to obtain the signs position
    for signs in change_number_signs:
        if data_in.rfind(signs) != -1:
            sign_position = data_in.rfind(signs)
            sign_position_list.append(sign_position)

    # Get the final position of the sign
    sign_position = max(sign_position_list)
    # Get the sign of the current data
    sign = data_in[sign_position]
    crypt_split = data_in.split(sign)
    num_split = crypt_split[-1].split("\n")

    # Loop to get the displace number used in the encryption
    for data in num_split[0]:
        displace_number = str(displace_number) + str(change_numbers.index(data))

    # Calculate the original sign used before the encryption
    abs_value = abs(int(displace_number))
    current_pos = change_number_signs.index(sign)
    odds = len(change_number_signs)
    sign = change_number_signs[getFinalPositionDecrypt(abs_value, current_pos, odds)]

    # Apply the obtained sign, in displace_number
    if sign == "-":
        displace_number = int(displace_number) * -1
    else:
        displace_number = int(displace_number)

    # Set the end of the current line, without the displace number 
    limit = len(data_in) - sign_position + 1

    # Iterate in all the characters of the line, to decrypt this
    for data_letters in data_in[0:-limit]:
        list_position = letters.find(data_letters)
        data_changed = data_changed + letters[getFinalPositionDecrypt(displace_number, list_position, len(letters))]

    # Return to empty string the displace number
    displace_number = ""
    # Add a line break to the line, and pass to the next line
    data_changed = data_changed + "\n"

# Function to get the sign of the displace number before the encryption
def getSign():
    # Get the global variables
    global sign
    global displace_number

    # Set the current sign
    if displace_number > 0:
        sign = "+"
    elif displace_number < 0:
        sign = "-"
    else:
        sign = "^"

# Function to calculate the final position based on the displace, current
# position of original data, and the lenght of the base string
def getFinalPositionCrypt(m_displace, m_position, m_letters):
    module = m_displace % m_letters

    if module + m_position >= m_letters:
        final_position = module - (m_letters - m_position)
    else:
        final_position =  m_position + module

    return final_position

# Function to calculate the original position based on the disoplace, current
# position of encrypted data, and the lenght of the base string
def getFinalPositionDecrypt(m_displace, m_position, m_letters):
    module = m_displace % m_letters

    if module >= m_letters - m_position:
        original_position = m_position - module + m_letters
    else:
        original_position = m_position - module

    if original_position >= m_letters:
        original_position = original_position - m_letters

    return original_position

# Call the start tool, at the moment of call in the terminal
if __name__ == '__main__':
    initTool()
