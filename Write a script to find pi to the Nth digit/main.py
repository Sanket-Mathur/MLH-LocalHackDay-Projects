import math

def sqrt(n, digit):
    """
    Calculate the square root of a long integer n.
    """
    precision = 10 ** 16
    num = float((n * precision) // digit) / precision
    
    guess = (int(precision * math.sqrt(num)) * digit) // precision
    n_digit = n * digit

    while True:
        prev_guess = guess
        guess = (guess + n_digit // guess) // 2
        if guess == prev_guess:
            break
    
    return guess

def power(n):
    if n == 0:
        return 1
    
    r = power(n // 2)
    if n % 2 == 0:
        return r * r
    
    return r * r * 10

def pi():
    """
    Calculating pi upto digit digits.
    """
    m = power(10000)
    k = 1
    a_k = m
    a_sum = m
    b_sum = 0

    const = 640320 ** 3 // 24

    while a_k != 0:
        a_k *= -(6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k //= k * k * k * const
        a_sum += a_k

        b_sum += k * a_k

        k += 1
    
    total = 13591409 * a_sum + 545140134 * b_sum
    pi = (426880 * sqrt(10005 * m, m) * m) // total
    
    return pi

if __name__ == '__main__':
    n = int(input("Enter the number of digits: "))
    pi_value = str(pi())
    print(pi_value[n - 1])