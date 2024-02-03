# pylint: disable=C0103
"""
Word Count Program
"""

import sys
import time

def word_count(file_path):
    """
    Count the frequency of each word in the given file.

    Args:
        file_path (str): The path of the file to process.

    Returns:
        dict: A dictionary containing word frequencies.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    word_freq = {}
    for word in words:
        word = word.lower()  # Convertir a minúsculas para considerar palabras iguales
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

def write_results(results, output_file):
    """
    Write the word frequencies to the specified output file.

    Args:
        results (dict): A dictionary containing word frequencies.
        output_file (str): The path of the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, freq in results.items():
            file.write(f"{word}: {freq}\n")

def print_results(results):
    """
    Print the word frequencies on the screen.

    Args:
        results (dict): A dictionary containing word frequencies.
    """
    for word, freq in results.items():
        print(f"{word}: {freq}")

def main():
    """
    Main function to execute the word count program.
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py WordCountResults.txt")
        return

    word_count_file = sys.argv[1]
    start_time = time.time()

    word_freq = word_count(word_count_file)

    if word_freq is not None:
        # Process TC files
        test_cases = ["TC1.txt", "TC2.txt", "TC3.txt", "TC4.txt"]
        combined_word_freq = {}

        for test_case in test_cases:
            tc_word_freq = word_count(test_case)
            if tc_word_freq is not None:
                for word, freq in tc_word_freq.items():
                    combined_word_freq[word] = combined_word_freq.get(word, 0) + freq

        print_results(combined_word_freq)
        write_results(combined_word_freq, "WordCountResults.txt")

        elapsed_time = time.time() - start_time
        print(f"Execution time: {elapsed_time:.4f} seconds")
        print("Results written to WordCountResults.txt")

if __name__ == "__main__":
    main()
