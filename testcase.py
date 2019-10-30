#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = 10#float(input())

    tip_percent = 3.0 #jint(input())

    tax_percent = 8.0#hint(input())
    tip_percent = meal_cost *(round(tip_percent,2)/100)
    tax_percent = meal_cost *(round(tax_percent,2)/100)
    total = meal_cost + round(tax_percent,2) + round(tip_percent,2)
    print(round(total))

#if __name__ == '__main__':
    solve(meal_cost, tip_percent, tax_percent)
