
"""

Project:        Basic Truth Table Generator
Programmer:     Paul Xiong
Date:           November 24, 2024

Description: 
The Basic Truth Table Generator simplifies the process of creating truth tables for logical operations 
involving binary variables. With this tool, the user can specify the number of variables (from 2 to 5), 
select a logical operation (such as AND, OR, XOR, NAND, etc.), and choose the display format (binary or 
boolean) for the results. The program computes all possible combinations of the input variables and 
applies the selected operation to each combination, providing the corresponding results. The generated 
truth table is displayed in the console for immediate reference, and the ability to save the results 
to a file is provided for future use or analysis. This tool offers a quick and accurate way to generate 
basic truth tables, eliminating manual errors and simplifying the process of logic design.

"""


# function to compute the result of the logical operation
def compute_operation(variables, operation):
    if operation == "AND":
        return all(variables) # returns True if all are True
    elif operation == "OR":
        return any(variables) # returns True if any is True
    elif operation == "NAND":
        return not all(variables) # negation of AND
    elif operation == "NOR":
        return not any(variables) # negation of OR
    elif operation == "XOR":
        return sum(variables) % 2 == 1 # returns True if an odd number of variables are True
    else:
        return None  # should never reach here if input is validated

# function to generate and save the truth table
def generate_truth_table(num_variables, operation, display_format):
    
    # initalize some constants
    TEXT_FILE = "truth_table.txt"
    COLUMN_WIDTH = 6

    # create table title for specific operation
    title = f"Truth table for {operation}:"
    
    # generate the variable names based on the number of variables from ASCII (A, B, C, D, E, ...)
    variable_names = [chr(65 + i) for i in range(num_variables)]
    
    # create header string with variables and result column
    header = "".join([name.ljust(COLUMN_WIDTH) for name in variable_names + ["Result"]])

    # add separator line between header and body (based on header length)
    separator = "-" * len(header)
    
    # declare table list
    table_lines = []

    # iterate over all possible combinations of variable values which is 2^n
    for i in range(2 ** num_variables):
        # create a list of 0 and 1 representing the current combination of variable values
        binary_values = [int(x) for x in f"{i:0{num_variables}b}"] # binary representation
        
        # compute the result of the operation for the current combination
        result = compute_operation(binary_values, operation)
        
        # convert binary values to True/False if necessary
        if display_format == 1:
            binary_values = ["True" if x == 1 else "False" for x in binary_values]
        else:
            result = 1 if result == True else 0
        
        # format the row for the table with proper alignment/column width
        row = "".join([str(val).ljust(COLUMN_WIDTH) for val in binary_values + [result]])
        table_lines.append(row)

    # save and overwrite to file
    with open(TEXT_FILE, "w") as file:
        file.write(f"{title}\n{header}\n{separator}\n") # write title, header, and separator
        file.writelines(line + "\n" for line in table_lines) # write each data row with newlines
    
    # display result
    print(f"{title}\n{header}\n{separator}") # print title, header, and separator
    print("".join(line + "\n" for line in table_lines)) # join the lines with newlines between them

    # notify user of file location
    print(f"Truth table saved to {TEXT_FILE}.")



# function to ask user how they want to display the truth table (binary or true/false)
def get_display_format():
    # initalize choice
    choice = -1
    
    # repeta until valid choice of 0 or 1
    while choice < 0:
        # prompt user for 0 or 1
        choice = int(input("Display information in binary (0) or true/false (1): "))
        
        # validate choice
        if choice == 0:
            # confirm user selected binary display
            print("Values will be displayed in binary.")
        elif choice == 1:
            # confirm user selected boolean display
            print("Values will be displayed as true/false.")
        else:
            # invalid message
            print("Invalid choice. Enter '0' for binary or '1' for true/false.")
        
        # new line
        print("")

    # return choice
    return choice


# function to get the logical operation choice from the user
def get_operation_choice():
    # initalize list of valid operations in string format
    valid_operations = ["AND", "OR", "NAND", "NOR", "XOR"]
    
    # declare operation
    operation = ""
    
    # repeat until a valid operation is found wihtin the list
    while operation not in valid_operations:
        # prompt for operation given list of options
        operation = input(f"Enter the logical operation ({', '.join(valid_operations)}): ").strip().upper()
        
        # validate user input for operation
        if operation in valid_operations:
            # confirm user's choice
            print(f"Successfully chose operation {operation}")
        else:
            # display improper input/operation
            print("Invalid operation. Try again.")
            
        # new line
        print("")
        
    # return valid operation
    return operation

# function to get the number of comparable variables from the user
def get_number_of_variables():
    # initalize number
    num = 0
    
    # repeat until a valid number is chosen (between 2 and 5)
    while num <= 0:
        # prompt user for input
        selected_num = int(input("Select a number of variables to compare (between 2-5): "))
    
        # check if the input is within the valid range (2 to 6 inclusive)
        if 2 <= selected_num <= 5:
        # assign the valid input to 'num' and confirm success
            num = selected_num
            print(f"Successfully chosen {num} variables.")
        else:
            # display error message if the number is out of range
            print("Number not in range 2-5. Try again.")
    
        # new line
        print("")
    
    # return valid num of variables
    return num


# function to introduce the system to the user
def introduce_system():
    print("Basic Truth Table Generator")
    print("---------------------------")
    print("")

# main program logic
def main():
    
    # display program title
    introduce_system()
    
    # get user input for number of variables, operation, and display format
    num = get_number_of_variables()
    operation = get_operation_choice()
    display_format = get_display_format()

    # generate and display the truth table based on input
    generate_truth_table(num, operation, display_format)

# execute the program
if __name__ == "__main__":
    main()
