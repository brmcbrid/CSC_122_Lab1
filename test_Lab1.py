# Tests for Lab1
# Triangle Area Calculator

import os.path
import sys
from Lab1 import main
from tud_tests import *

def test_Lab1():

    try:
        exists = os.path.exists("Lab1.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input([4.125,3.25,2.5])
    main()
    output = get_display_output()

    assert output == [
        "Triangle Calculator\n",
        "Enter the length of side 1 in inches: ",
        "Enter the length of side 2 in inches: ",
        "Enter the length of side 3 in inches: ",
        "\nThe area of the triangle is 4.06 square inches."
       ]

    # Test 2
    set_keyboard_input([12.45,6.78,8.875])
    main()
    output = get_display_output()

    assert output == [
        "Triangle Calculator\n",
        "Enter the length of side 1 in inches: ",
        "Enter the length of side 2 in inches: ",
        "Enter the length of side 3 in inches: ",
        "\nThe area of the triangle is 29.12 square inches."
       ]