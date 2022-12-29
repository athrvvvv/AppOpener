# Closing application via AppOpener
from AppOpener import close

def main():
    while True:
        inp = input("ENTER APP TO CLOSE: ")
        close(inp, output=False) # Output text will be not printed <output=False>

if __name__ == "__main__":
    main()
