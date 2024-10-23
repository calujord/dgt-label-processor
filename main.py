import argparse

from src.machine_label import DgtMachine


def __main__(plate: str):
    label = DgtMachine(plate).process_label()
    print(label.url_image, label.value)


if __name__ == '__main__':
    # Example: python main.py 1234-ABC
    parser = argparse.ArgumentParser(description='Process a plate number to get the DGT label.')

    # Example: python main.py 1234-ABC
    parser.add_argument('plate', type=str, help='The plate number to process')
    args = parser.parse_args()
    __main__(plate=args.plate)
