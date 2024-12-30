
def options(n):
    """returns the interpolation factor"""
    count = 0
    while True:
        try:
            prompt = input("Enter the factor by which you would like to interpolate the image [ int or float ] :")
            option = float(prompt)
        except ValueError:
            count = count + 1
            if (prompt.lower() == "quit"):
                sys.exit("Exiting with quit...")
            if (count > 10):
                print("\nYou can enter 'quit' to exit\n")
        else:
            return option 
            
