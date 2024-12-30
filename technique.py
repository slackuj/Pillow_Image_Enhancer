import sys
def options(n):
    """returns the chosen Image Enhancement Technique"""
    count = 0
    while True:
        try:
            prompt = input(f"Select any one Image Enhancement Technique [1-{n}]: ")
            option = int(prompt)
        except ValueError:
            count = count + 1
            if (prompt.lower() == "quit"):
                sys.exit("Exiting with quit...")
            if (count > 10):
                sys.exit("Exiting for inapprpriate response...")
        else:
            if (1 <= option <= n): return option 
            else: 
                count = count + 1
            if (3 < count <= 10):
                print("\nYou can enter 'quit' to exit\n")
            if (count > 10):
                sys.exit("Exiting for inapprpriate response...")
