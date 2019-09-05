from collections import Counter


class PurchasesCounter:
    def __init__(self, file_path):
        self.purchases = Counter()

        # parse purchases
        with open(file_path) as f:
            for line in f:
                month_name, _, month_purchases = line.rstrip().split(' ', 2)

                # remove brackets from purchases
                month_purchases = month_purchases.replace('[', '')
                month_purchases = month_purchases.replace(']', '')

                # split purchases
                month_purchases = month_purchases.split(', ')

                # remove quotes
                month_purchases = [
                    purchase.replace('\'', '') for purchase in month_purchases
                ]

                # initialize purchases counter
                # with values of the first month
                if len(self.purchases) == 0:
                    self.purchases.update(month_purchases)

                # increase purchases count
                # in purchase is presented
                else:
                    for purchase in month_purchases:
                        if purchase in self.purchases.elements():
                            self.purchases.update([purchase])

    def __repr__(self):
        """
            Format: <purchase> ---> <count>
        """
        repr_str = ''
        for purchase, count in self.purchases.most_common(len(self.purchases)):
            repr_str += purchase
            repr_str += ' ---> '
            repr_str += str(count)
            repr_str += '\n'
        repr_str += 'Number of purchase types: {}'.format(len(self.purchases))
        return repr_str


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--purchases',
        help='file with purchases',
        default='purchases.txt'
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    purchases = PurchasesCounter(args.purchases)
    print(purchases)
