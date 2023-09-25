class VectorDivisionError(Exception):
    pass

def divide_vectors(vector1, vector2):
    try:
        if len(vector1) != len(vector2):
            raise VectorDivisionError("Vector dimensions do not match")
        
        result_vector = [v1 / v2 for v1, v2 in zip(vector1, vector2)]
        return result_vector
    except ZeroDivisionError:
        raise VectorDivisionError("Division by zero error")

def get_vector_input(prompt):
    try:
        vector_str = input(prompt)
        vector = [float(val) for val in vector_str.split()]
        return vector
    except ValueError:
        raise VectorDivisionError("Invalid input. Please enter numeric values separated by spaces")

if __name__ == "__main__":
    try:
        print("Enter the first vector values separated by spaces:")
        vector1 = get_vector_input("Vector 1: ")
        
        print("Enter the second vector values separated by spaces:")
        vector2 = get_vector_input("Vector 2: ")
        
        result_vector = divide_vectors(vector1, vector2)
        print(f"The result vector is: {result_vector}")
    except VectorDivisionError as e:
        print(f"Vector Division Error: {e}")