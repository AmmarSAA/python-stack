# -----------------------------
# Simple Stack Implementation
# -----------------------------

# Function to remove (pop) the top item from the stack
def pop():
    global top
    # Replace the top element with an empty string (acts as 'removing' it)
    stack[top] = emptyString
    # Move the top pointer down by 1
    top -= 1
    # Return the new top pointer
    return top


# Function to add (push) a new item onto the stack
def push(addItem):
    global top
    # Move the top pointer up by 1 to make space for the new item
    top += 1
    # Add the new item at the new top position
    stack[top] = addItem
    # Return the new top pointer
    return top


# Function to display all elements currently in the stack
def output():
    # Loop through all elements up to the current top index
    for index in range(top + 1):
        # Print each index and its corresponding value in the stack
        print(f"{index}, {stack[index]}")


# Function to initialize the stack with a given size
def initilize(size):
    global top, emptyString, nullPointer, stack
    # A null pointer value representing 'no elements'
    nullPointer = -1
    # Initialize top to nullPointer (i.e., empty stack)
    top = nullPointer
    # Define an empty string placeholder for stack slots
    emptyString = ""
    # Create the stack as a list with a fixed size, filled with empty strings
    stack = [emptyString] * size


# Main program function
def main():
    # Ask the user for the desired size of the stack
    size = int(input("Please enter the size of stack: "))
    # Initialize the stack
    initilize(size)

    # Ask how many values the user wants to push into the stack
    value = int(input("How many values would you like to enter: "))
    for i in range(value):
        # Take each value as input
        valueEnter = input("Please enter value " + str(i + 1) + ": ")
        # Push the entered value onto the stack
        push(valueEnter)

    # Display the stack after insertion
    print("\nStack after pushing values:")
    output()

    # Ask how many values to remove (pop) from the stack
    delete = int(input("\nPlease enter how many values would you like to delete: "))
    for i in range(delete):
        # Remove the top element from the stack
        pop()

    # Display the stack after deletion
    print("\nStack after popping values:")
    output()


# Run the main function
main()
