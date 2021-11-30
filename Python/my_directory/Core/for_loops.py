def basic():
    print("Basic counting, 1 to 150")
    for i in range(1, 151):
        print(i)


def div_by(divisor):
    print("counting by multiples of 5")
    for i in range(1, 1001):
        if (i % divisor) == 0:
            print(i)


def div_by_dojo(divisor_a, divisor_b):
    print("it's like fizzbuzz but different")
    for i in range(1, 101):
        if (i % divisor_a) == 0:
            print("coding")
        if (i % divisor_b) == 0:
            print("dojo")
        else:
            print(i)


def big_add():
    print("printing sum of all the odd numbers between 1 and 500000")
    sum = 0
    for i in range(1, 500001):
        if (i % 2) != 0:
            sum = (sum + i)
    print(sum)


def countdown(start):
    print("countdown by 4 starting at 2018")
    while start > 0:
        print(start)
        start = (start - 4)


def flex_counter(low, high, multiple):
    print("printing number between defined high and low divisible by defined integer ")
    for i in range(low, (high + 1)):
        if i % multiple == 0:
            print(i)


def main():
    basic()
    div_by(5)
    div_by_dojo(5, 10)
    big_add()
    countdown(2018)
    flex_counter(1, 100, 10)


if __name__ == "__main__":
    main()
