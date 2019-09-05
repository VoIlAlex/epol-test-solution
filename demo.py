"""
    Test of implemented solution 
"""

from purchases_generator import PurchasesGenerator
from purchases_counter import PurchasesCounter


if __name__ == "__main__":
    # number of ids
    # of purchases to
    # generate
    ids_num = 100

    # generate random
    # report on purchases
    purchases_generator = PurchasesGenerator(
        ids_num=ids_num,
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
    ids_num_counted = len(purchases_counter.purchases)
    print('Initial number of purchase ids: {}'.format(ids_num))
    print('Final Number of purchase ids: {}'.format(ids_num_counted))
