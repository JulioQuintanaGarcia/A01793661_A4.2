# pylint: disable=C0103
"""
Este script convierte números a binario y hexadecimal,
imprime los resultados en pantalla y guarda en un archivo llamado ConvertResults.txt.
"""
import sys
import time

def convert_to_binary(decimal):
    """Convierte un número decimal a binario."""
    binary_result = ""
    while decimal > 0:
        binary_result = str(decimal % 2) + binary_result
        decimal = decimal // 2
    return binary_result

def convert_to_hexadecimal(decimal):
    """Convierte un número decimal a hexadecimal."""
    hex_result = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hex_result = str(remainder) + hex_result
        else:
            hex_result = chr(ord('A') + remainder - 10) + hex_result
        decimal = decimal // 16
    return hex_result

def process_file(file_path):
    """Procesa un archivo, convierte los números y guarda los resultados."""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open('ConvertResults.txt', 'w', encoding="utf-8") as output_file:
            for line in lines:
                try:
                    decimal_number = int(line.strip())
                    binary_result = convert_to_binary(decimal_number)
                    hex_result = convert_to_hexadecimal(decimal_number)

                    print(f"Decimal: {decimal_number},"
                          f"Binary: {binary_result},"
                          f"Hexadecimal: {hex_result}")
                    output_file.write(f"Decimal: {decimal_number},"
                                      f"Binary: {binary_result},"
                                      f"Hexadecimal: {hex_result}\n")
                except ValueError:
                    print(f"Error: Invalid data in file - {line.strip()}")
                    output_file.write(f"Error: Invalid data in file - {line.strip()}\n")
    except FileNotFoundError:
        print("Error: File not found.")
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        start_time = time.time()
        process_file(sys.argv[1])
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        with open('ConvertResults.txt', 'a', encoding="utf-8") as output_file:
            output_file.write(f"Execution time: {execution_time} seconds\n")
