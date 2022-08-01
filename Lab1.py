# CSC 122
# Traingle Area Calculator
# By <Your Name>

# Correct all of the errors in this code

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""

#import math library

def main():
    print(f"Triangle Calculator') # print standard header

    # Inputs(s): Collection of user data from keyboard for length of sides of triangle
    s1=input("Enter the length of side 1 in inches: ")
    s2=input("Enter the length of side 2 in inches: ")
    S3=input("Enter the length of side 3 in inches: ")

    # Processes: Calculation of result using math module sqrt function
    s=s1+s2+s3/2 # semi-perimeter calculation
    area=math.sqrt(s(s-s1)(s-s2)(s-s3)) # Hero's formula calculation

    # Output(s): Output of result to console screen
    print(f"\n\n The area of the triangle is {area:.2f} square inches.\n\n")

if __name__ == "__main__":
    main()
