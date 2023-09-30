from variable_base_factoradic import convert
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")


def main():
    inp = "1010"
    res = convert(inp)
    if isinstance(res, int):
        print(f"Converting {inp} from factoradic: {res}")
    else:
        print(f"Converting {inp} to factoradic: {res}")


if __name__ == "__main__":
    main()
