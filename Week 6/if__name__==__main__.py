#  if __name__ == __main__:   (This script can be imported OR run standalone)
#                              Functions and classes in this module can be reused
#                              without the main block of code executing

#  Ex. library = Import library for functionality
#                         When running library directly, display a help page
def main():
    print("Hello world!")
    # your program goes here

if __name__ == "__main__":    # This Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
    main()
                    # protecting users from executing the code if they simply want to import the functionality.

