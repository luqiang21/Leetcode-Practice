from tools import timing

@timing
def dec_to_bin1(number):
    bins = []
    if number < 2:
        return str(number)
    bins.append(str(number%2))
    while number >= 2:
        number //= 2
        bins.append(str(number%2))

    return ''.join(reversed(bins))


@timing
def dec_to_bin2(number):
    if number < 2:
        return str(number)
    return dec_to_bin2(number/2) + dec_to_bin2(number%2)
num = 3
print(dec_to_bin1(num))
print(dec_to_bin2(num))

num = 10
print(dec_to_bin1(num))
print(dec_to_bin2(num))
