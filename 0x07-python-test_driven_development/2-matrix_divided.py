#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a number.

    Args:
        matrix (list): The input matrix (2D list of numbers).
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: The new matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix is not a matrix (2D list of numbers).
        TypeError: If the div is not a number (integer or float).
        ZeroDivisionError: If the div is 0.
    """
    # Check the types of matrix and div
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (2D list of numbers)")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("Al elements of the matrix must be numbers")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check the value of div
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with all elements divided by div
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
