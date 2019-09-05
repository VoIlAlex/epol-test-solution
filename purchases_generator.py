import random
import string
import numpy as np
import argparse


class PurchasesGenerator:
    """
        Generates random report 
        about purchases by months
    """

    def __init__(self, ids_num, purchases_day_mean, purchases_day_std):
        """
        Arguments:
            ids_num {int} -- number of purchases ids to generate
            purchases_day_mean {int} -- average number of purchases per day
            purchases_day_std {int} -- average deviation of purchases number per day
        """
        self.purchases_day_mean = purchases_day_mean
        self.purchases_day_std = purchases_day_std

        # generate purchases ids
        self.purchase_ids = []
        for i in range(ids_num):
            purchase_id = ''

            # first letter
            purchase_id += random.choice(string.ascii_uppercase)

            # 3 random numbers
            for i in range(3):
                purchase_id += str(random.randint(0, 9))

            self.purchase_ids.append(purchase_id)

    def generate(self, output_file, months_number=12):
        """
        Generates purchases report 
        in the specified file in format:

        m<n> = ['<name>', ...]
        ...

        where <n> is month number, <name> is name of 
        purchase.

        Arguments:
            output_file {"writable"} -- writable object ot place report
            months_number {int} -- number of months to fill
        """
        assert months_number > 0 and months_number < 13

        for i in range(months_number):

            month_id_name = 'm' + str(i+1)

            # generate random number
            # as number of purchases
            # in this day
            purchases_number = np.random.normal(
                loc=self.purchases_day_mean,
                scale=self.purchases_day_std
            )
            purchases_number = int(purchases_number)
            purchases_number = max(1, purchases_number)

            purchases_today = []
            for i in range(purchases_number):
                random_purchase = random.choice(self.purchase_ids)
                purchases_today.append(random_purchase)

            month_purchases_message = month_id_name + \
                " = ['" + "', '".join(purchases_today) + "']"

            print(month_purchases_message, file=output_file)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generates random purchases report'
    )
    parser.add_argument(
        '-tn', '--types-number',
        help='number of purchases types',
        type=int,
        default=100
    )
    parser.add_argument(
        '-m', '--mean',
        help='mean of purchases number per day',
        type=int,
        default=150
    )
    parser.add_argument(
        '-s', '--std',
        help='standard deviation of purchases number per day',
        type=int,
        default=50
    )
    parser.add_argument(
        '-mn', '--months-number',
        help='number of months go generate',
        type=int,
        default=12
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    purchases_generator = PurchasesGenerator(
        ids_num=args.ids_number,
        purchases_day_mean=args.mean,
        purchases_day_std=args.std
    )
    report_file = open('purchases.txt', 'w+')
    purchases_generator.generate(
        output_file=report_file,
        months_number=args.months_number
    )
    print('[INFO] Purchases are generated.')
