# File Creation
def create_file():
    try:
        # Open file in write mode
        f = open("my_file.txt", "w")
        
        # Write content to file
        f.write("Hello World!\n")
        f.write(f"This year is {2024}\n")
        f.write("Python is awesome!")
        
        print("File created successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close the file
        if 'f' in locals() and not f.closed:
            f.close()

# File Reading and Display
def read_file():
    try:
        # Open file in read mode
        f = open("my_file.txt", "r")
        
        # Read file content
        content = f.read()
        
        print("\nFile contents:")
        print(content)
    
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the file
        if 'f' in locals() and not f.closed:
            f.close()

# File Appending
def append_to_file():
    try:
        # Open file in append mode
        f = open("my_file.txt", "a")
        
        # Append new content
        f.write("\n\nAdditional lines:\n")
        f.write("Line 1 appended.\n")
        f.write("Line 2 appended.\n")
        f.write("Line 3 appended.")
        
        print("\nContent appended successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the file
        if 'f' in locals() and not f.closed:
            f.close()

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Display updated content