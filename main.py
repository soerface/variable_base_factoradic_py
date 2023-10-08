from variable_base_factoradic import to_factoradic
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")


def main():
    inp = 101
    res = to_factoradic(inp)
    print(f"Converting {inp} to factoradic: {res}")


if __name__ == "__main__":
    main()
