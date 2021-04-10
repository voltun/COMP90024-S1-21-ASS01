import json
import os

def main():
    #
    afinn_f = open(os.path.join(os.path.dirname(__file__), "AFINN.txt"))
    afinn = afinn_f.read()


    print(afinn)


if __name__ == "__main__":
    main()
