#Name: Rohit Mukherjee
#Course: 5363 cryptography
#professor: Dr.Terry Griffin
#program: main where we pass arguments

import argparse
import program3 as A1
from fractions import Fraction

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a",type=float, help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b",type=float, help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1",type=float, help="")
    parser.add_argument("-y1",dest="y1",type=float, help="")
    parser.add_argument("-x2",dest="x2",type=float, help="")
    parser.add_argument("-y2",dest="y2",type=float, help="")

    args = parser.parse_args()

    # Example:
    # python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1
    A1.curve(args.x1,args.y1,args.x2,args.y2,args.a,args.b)
    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    

if __name__ == '__main__':
    main()