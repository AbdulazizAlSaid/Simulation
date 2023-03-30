import argparse
import random

def main():
    parser = argparse.ArgumentParser(description="Monty Hall Simulation")
    parser.add_argument('--num-doors', dest='N', required=False)
    args = parser.parse_args()
    global numDoors
    if args.N: 
        numDoors = int(args.N)
    else: 
        numDoors = 3
    print(numDoors)
    doors = [0]* numDoors
    print(doors)

    prizeIdx = random.randint(0, numDoors-1)
    doors[prizeIdx] = 1
    print(doors)
if __name__ == "__main__":
    main()