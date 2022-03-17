from gettext import find
from itertools import count
from math import sqrt, comb, ceil, floor, isqrt
from re import I, S
import time
from typing import MutableMapping
from sympy import primerange, sieve
def sieve_factors(n):
    s = [0] * (n+1)
    s[1] = 1
    for i in range(2, n+1, 2):
        s[i] = 2
    for i in range(3, n+1, 2):
        if s[i] == 0:
            s[i] = i
            for j in range(i, n + 1, i):
                if s[j] == 0:
                    s[j] = i
    return s
tiempo = time.perf_counter()
Q = sieve_factors(2*(isqrt(2 * 3141592653589793) + 1))


def findfactors(n):
    global Q
    yield Q[n]
    last = Q[n]
    while n > 1:
        if Q[n] != last and Q[n] != 1:
            last = Q[n]
            yield Q[n]
        n //= Q[n]


def products_of(p_list, upto):
    for i, p in enumerate(p_list):
        if p > upto:
            break
        yield -p
        for q in products_of(p_list[i+1:], upto=upto // p):
            yield -p * q


def phi(n, upto=None):
    if upto is not None and upto < n:
        cnt = upto
        p_list = list(findfactors(n))
        for q in products_of(p_list, upto):
            cnt += upto // q if q > 0 else -(upto // -q)
        return cnt
    cnt = n
    for p in findfactors(n):
        cnt *= (1 - 1/p)
    return int(cnt)

def countprimtrips(n):
    cnt = 0
    for m in range(3, int(sqrt(2*n)) + 1, 2):
        xmax = int(sqrt(2*n - m**2))
        cnt += phi(2*m, upto=xmax) if xmax < m else phi(2*m) // 2
    return cnt

print(countprimtrips(3141592653589793))
print(time.perf_counter() - tiempo)


def square_free(n):
    if n % 2 == 0:
        n /= 2
    if n % 2 == 0:
        return False
    for r in range(3, int(sqrt(n)) + 1):
        if n % r == 0:
            n /= r
        if n % r == 0:
            return False
    return True


def euler_203(r):
    cnt = 0
    distict = []
    rows = []
    for row in range(r+1):
        l = []
        for item in range(row + 1):
            l.append(comb(row, item))
        rows.append(l)
    for q in rows:
        for i in q:
            check = square_free(i)
            if check and i not in distict:
                cnt += i
                distict.append(i)
    return cnt


def hamming_numbers(n, upto):
    sieve = [True] * n
    primelist = []
    q = 0
    start = time.time()
    for i in range(2, n):
        if sieve[i]:
            primelist.append(i)
            for p in range(i * i, n, i):
                sieve[p] = False

    for i in range(1, upto):
        factors = list(findfactors(i))
        if all(item in primelist for item in factors):
            q += 1
    end = time.time()
    return q, end - start

def take2(limit,n):
    start = time.time()
    cnt = 1
    h = 1
    _h = [h]
    sieve = [True] * n
    primelist = []
    for i in range(2, n):
        if sieve[i]:
            primelist.append(i)
            for p in range(i * i, n, i):
                sieve[p] = False
    multindex = [0 for i in primelist]
    multvalues = [x * _h[i] for x, i in zip(primelist, multindex)]
    while h < limit:
        h = min(multvalues)
        _h.append(h)
        for (n,(v, x, i)) in enumerate(zip(multvalues, primelist, multindex)):
            if v == h:
                i += 1
                multindex[n] = i
                multvalues[n] = x * _h[i]
        cnt += 1
    end = time.time()
    return cnt, end - start


# def search(prev, indexinlist):
#     result = 1
#     sieve = [True] * 100
#     primes = []
#     for i in range(2, 100):
#         if sieve[i]:
#             primes.append(i)
#             for p in range(i * i, 100, i):
#                 sieve[p] = False
#     for i in range(indexinlist, 25):
#         product = primes[i] * prev
#         if product > 1000000000:
#             break
#         result += search(product, i)
#     return result

# print(search(1,0))


# start of integer partitions
# generating functions


def totient_recursive(n):
    i = 1
    if n > 2:
        factors = findfactors(n)
        cnt = n
        for p in factors:
            cnt *= (1 - 1/p)
        i += totient_recursive(int(cnt))
    else:
        i += 1
        return i
    return i


def euler214(n):
    sieve = [True] * n
    primelist = []
    q = 0
    start = time.time()
    for i in range(2, n):
        if sieve[i]:
            if i != 2 or i != 3:
                primelist.append(i)
            for p in range(i * i, n, i):
                sieve[p] = False
    for item in primelist:
        if int(totient_recursive(item - 1) + 1) == 25:
            q += item
    end = time.time()
    return q, end - start 


def check_amt_primes(n1, n2, n):
    sieve = [True] * n2
    primelist = []
    q = 0
    endlist = []
    start = time.time()
    for i in range(2, n2):
        if sieve[i]:
            if i > n1:
                primelist.append(i)
            for p in range(i * i, n2, i):
                sieve[p] = False
    for prime in primelist:
        q = 0
        for i in str(prime):
            if int(i) == 1:
                q  += 1
        if q == 3:
            endlist.append(prime)
    return endlist


def check_amt_primes2(n1, n2, n):
    start = time.time()
    primelist = primerange(n1,n2)
    endlist = []
    for i in range(n1, n2):
        q = 0
        for l in str(i):
            if int(l) == 1:
                q  += 1
        if q ==3:
            endlist.append(i)
    end = time.time()
    return endlist, end - start

def find_multiple_factors(n):
    l = []
    for i in range(2, int(sqrt(n)) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt > 0:
            l.append((i, cnt))
    if n > 1:
        l.append((n, 1))
    return l
# 211 Problem


def sigma_2(n):
    factors = find_multiple_factors(n)
    if len(factors) == 1:
        return 1.5
    num = 1
    for prime in factors:
        num *= (prime[0]**(((prime[1] +1) * 2)) - 1)/((prime[0]**2)-1)
    return int(num)


def euler_211(n):
    start = time.time()
    sum = 0
    for i in range(42, n):
        j = sqrt(sigma_2(i))
        if ceil(j) == floor(j):
            sum += i
    end = time.time()
    return sum, end - start

def sieve_factors(n):
    prime = [False] * (n+1)
    s = [0] * (n+1)
    s[1] = 1
    l = []
    for i in range(2, n+1, 2):
        s[i] = 2
    for i in range(3, n+1, 2):
        if prime[i] == False:
            s[i] = i
            for j in range(i, int(n/i) + 1, i):
                if prime[i*j] == False:
                    prime[i*j] = True
                    s[i*j] = i
    return s


# @cache
# def power(p: int, e: int):
#     return (pow(p, 2 * e + 2) - 1) // (p * p - 1)


# def sigma2(n: int):
#     global P
#     s = 1
#     while P[n] > 1:
#         p, e = P[n], 0
#         while P[n] == p:
#             n, e = n // p, e + 1
#         s *= power(p, e)
#     return s




# total = 0
# for n in range(1, 64 * 10 ** 6):
#     s2 = sigma2(n)
#     if isqrt(s2)**2 == s2:
#         total += n
