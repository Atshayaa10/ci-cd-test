def add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        raise TypeError("Both inputs must be numbers")

def main():
    result = add(5, 3)
    print("The sum of 5 and 3 is:", result)

if __name__ == "__main__":
    main()