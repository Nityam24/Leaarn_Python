# Write a program to read n integers from the keyboard and store them into a file
# total.txtfile, separate odd and even numbers and store them in odd.txt and even.txt file.
# Display the content of all three files.


def reciprocal_list_elements(input_list):
    result = []
    for item in input_list:
        try:
            if isinstance(item, (int, float)):
                reciprocal = 1 / item
                result.append(reciprocal)
            else:
                raise ValueError(f"Invalid input: {item}")
        except ZeroDivisionError:
            print(f"Error: Division by zero for element {item}")
            result.append(None)
        except ValueError as ve:
            print(f"Error: {ve}")
            result.append(None)
    return result

input_list = [12, 0, 'a', 20, 'hi']
reciprocal_values = reciprocal_list_elements(input_list)
print(reciprocal_values)