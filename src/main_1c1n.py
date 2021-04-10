import json
import os
from afinn_reader import AfinnReader

def main():
    parent_dir = os.path.dirname(os.path.dirname(__file__))

    #Init classes
    afinn = AfinnReader(os.path.join(parent_dir, "AFINN.txt"))

    print(afinn.calcAFINNScore(["abanDoNs", "abandons.!?", "abandon abandon"]))


if __name__ == "__main__":
    main()
