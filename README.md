# Testing of simple book library CLI

![Library](https://img.shields.io/badge/Library-Management-blue)

## Description

Book Library CLI is a simple command-line application to manage a library of books. It supports adding, deleting, listing, and finding books in the library. The data is stored in a JSON file for persistence.

## Features

- Add a book with title and author
- Delete a book by title
- List all books in the library
- Find a book by title

## Usage

### Interact with the CLI

To start the application, navigate to the directory containing the project files and run:

```bash
python library.py
```

You will see the following menu:

```
Welcome to the Book Library CLI!
1. Add a book
2. Delete a book
3. List all books
4. Find a book
5. Exit
Enter your choice:
```

You can choose an option by entering the corresponding number. Follow the prompts to add, delete, list, or find books in the library.


## Testing
This project uses the `unittest` module for testing.  

### Running Tests

To run the tests included with the Book Library, follow these steps:

1. **Open your terminal**: Make sure you are in the root directory of the project where the test files are located.

2. **Execute the Test Command**: Run the tests using the Python unittest module which is a standard testing library in Python. Here's how you can run all tests from the terminal:

```bash
 python -m unittest test_library.py
```

### The tests for the Book Library CLI cover the following key functionalities:

- Adding a book
- Deleting a book
- Listing all books
- Finding a book

### Example Test Output

    ```bash
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s
    OK
    ```

