primes = []
not_primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for num in range(2,number):
        if number % num == 0:
            is_prime = False
            break
    if is_prime:
            primes.append(number)
    else:
            not_primes.append(number)
print('Primes:', primes)
print('Not Primes:', not_primes)
        


