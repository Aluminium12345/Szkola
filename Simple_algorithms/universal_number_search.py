'''
ENG:
The script first randomizes a list of 1000 numbers and then look for "snum" in this list. This is thought of as a compatibility algorithm and because of that
it is probably not as efficient as it could be. The compatibility i am talking about is with assembly's "jump if equals zero" command.

PL:
Ten skrypt najpierw losuje liste 1000 liczb. Pozniej w tej liscie jest szukana liczba "snum". Ten skrypt zostal stworzony z mysla o kompatybilnosci z jezykiem
asemblera i jego insterukcja "skocz jesli rowna sie zero".
'''
import random

def main():

    numbers = []
    addresses = []
    snum = random.randint(1, 100)
    adr = 0

    for f in range(1000):
        numbers.append(random.randint(1, 100))
    
    for adr in range(len(numbers)):
        x = numbers[adr] - snum
        if x == 0:
            addresses.append(adr)

    print(f'number {snum} is located on the following addresses: {addresses} in the list "numbers"')

if __name__ == "__main__":
    main()
