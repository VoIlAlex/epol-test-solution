"""
    Test of implemented solution 
"""

from purchases_generator import PurchasesGenerator
from solution import PurchasesCounter


if __name__ == "__main__":
    # number of types
    # of purchases to
    # generate
    types_num = 100

    # generate random
    # report on purchases
    purchases_generator = PurchasesGenerator(
        types_num=types_num,
        purchases_day_mean=150,
        purchases_day_std=50
    )
    purchases_generator.generate(
        output_file=open('purchases.txt', 'w+'),
        months_number=8
    )

    # print count of
    # purchases represented
    # in each month
    purchases_counter = PurchasesCounter('purchases.txt')
    print(purchases_counter)
    print('Initial number of purchase types: {}'.format(types_num))