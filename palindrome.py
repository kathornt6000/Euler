from time import perf_counter

from sympy import N, per, sieve
from numba import njit
from functools import cache
import numpy as np
from math import isqrt

from pytorch_tutorial import sigma_2

# prime numbers up to limit
def sieve_factors(n):
    s = [0] * (n+1)
    s[1] = 1
    for i in range(2, n+1, 2):
        s[i] = 2
    for i in range(3, n+1, 2):
        if s[i] == 0:
            s[i] = i
            for j in range(i, n + 1, i):
                s[j] = i
    return s

@njit
def primesieve(limit=64 * 10 ** 6):
    sieve = np.full(limit + 1, 0, dtype=np.uint64)
    sieve[1] = 1
    sieve[2::2] = 2
    for i in range(3, limit + 1, 2):
        if not sieve[i]:
            sieve[i::i] = i
    return sieve


@cache
def power(p: int, e: int):
    return (pow(p, 2 * e + 2) - 1) // (p * p - 1)


def sigma2(n: int):
    global S
    s = 1
    while S[n] > 1:
        p, e = S[n], 0
        while S[n] == p:
            n, e = n // p, e + 1
        s *= power(p, e)
    return s


# time = perf_counter()
# S = sieve_factors(64000000)
# total = 0
# for n in range(1, 64 * 10 ** 6):
#     s2 = sigma2(n)
#     if isqrt(s2)**2 == s2:
#         total += n
# total = 0
# for n in range(1, 64 * 10 ** 6):
#     s2 = sigma2(n)
#     if isqrt(s2)**2 == s2:
#         total += n

print(16/(16**2))