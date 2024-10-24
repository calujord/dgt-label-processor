import argparse

from exceptions.request_exception import RequestException
from src.machine_label import DgtMachine


def __main__(plate: str):
    try:
        # Process the plate number
        label = DgtMachine(plate).process_label()
        print("Label image", label.url_image)
        print("Label value", label.value)
    except RequestException as e:
        print(f"Response error: {e}")


if __name__ == '__main__':
    # Example: python main.py 1234-ABC
    parser = argparse.ArgumentParser(description='Process a plate number to get the DGT label.')

    # Example: python main.py 1234-ABC
    parser.add_argument('plate', type=str, help='The plate number to process')
    args = parser.parse_args()
    __main__(plate=args.plate)
