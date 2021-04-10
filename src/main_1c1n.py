import json
import os
from afinn_reader import AfinnReader

def main():
    #Init classes
    afinn = AfinnReader(os.path.join(os.path.dirname(__file__), "AFINN.txt"))

    print(afinn.calcAFINNScore(["abanDoNs", "abandons.!?", "abandon abandon"]))


if __name__ == "__main__":
    main()
