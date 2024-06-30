from package.input_string import get_string
from package.calculate_string  import calculate_string
def main():
    s = get_string()
    length = calculate_string(s)

    print(f"the length of string is :{length}")


if __name__ ==  "__main__":
    main()

