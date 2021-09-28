import random

def main():

    numbers = []
    addresses = []
    snum = random.randint(1, 100)
    adr = 0

    for f in range(999):
        numbers.append(random.randint(1, 100))
    
    for adr in range(len(numbers)):
        x = numbers[adr] - snum
        if x == 0:
            addresses.append(adr)

    print(f'number {snum} is located on the following addresses: {addresses} in the list "numbers"')

if __name__ == "__main__":
    main()
