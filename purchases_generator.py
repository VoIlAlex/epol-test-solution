import random
import string
import numpy as np
import argparse


class PurchasesGenerator:
    def __init__(self, types_num, purchases_day_mean, purchases_day_std):
        """
        Arguments:
            types_num {int} -- number of purchases types to generate
            purchases_day_mean {int} -- average number of purchases per day
            purchases_day_std {int} -- average deviation of purchases number per day
        """
        self.purchases_day_mean = purchases_day_mean
        self.purchases_day_std = purchases_day_std

        # generate purchases types
        self.purchase_types = []
        for i in range(types_num):
            purchase_type = ''

            # first letter
            purchase_type += random.choice(string.ascii_uppercase)

            # 3 random numbers
            for i in range(3):
                purchase_type += str(random.randint(0, 9))

            self.purchase_types.append(purchase_type)

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
                random_purchase = random.choice(self.purchase_types)
                purchases_today.append(random_purchase)

            month_purchases_message = month_id_name + \
                " = ['" + "', '".join(purchases_today) + "']"

            print(month_purchases_message, file=output_file)


if __name__ == "__main__":
    purchases_generator = PurchasesGenerator(
        types_num=100,
        purchases_day_mean=150,
        purchases_day_std=50
    )
    report_file = open('purchases.txt', 'w+')
    purchases_generator.generate(report_file)
