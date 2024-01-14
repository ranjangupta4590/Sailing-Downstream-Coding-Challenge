def check_list(input_list):
    # Check if the length is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("Error: List length must be a multiple of 10.")

    # Remove items at positions which are a multiple of 2 or 3
    required_list = [x for i, x in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

    return required_list

try:
    # Accept a list of integers from the user
    user_input = input("Enter a list of integers separated by space: ")
    input_list = list(map(int, user_input.split()))

    # Call the function to process the list
    result = check_list(input_list)

    # Print the input and processed lists
    print("Input List:", input_list)
    print("Processed List:", result)

except ValueError as e:
    print(e)
except Exception as e:
    print("An unexpected error occurred:", e)
