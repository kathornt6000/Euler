import time
from math import log, sqrt, gcd
from tkinter import PhotoImage
import numpy as np

from pytorch_tutorial import totient_recursive

#  class board:
#     def __init__(self) -> None:
#         self.moves = []
#         self.flipped = False
#         self.whitesTurn = True
#         self.squares = []
#         for r in range(8):
#             for c in range(8):
#                 self.squares.append(square(r,c))
#         self.standard()

#     def standard(self):
#         return None
# class square:
#     def __init__(self, row, col) -> None:
#         self.row = row
#         self.col = col
#         self.lDiag = self.setDiag(row, col, 1)
#         self.rDiag = self.setDiag(row, col, 2)

#     def setDiag(self, row, col, axis):
#         return None

#     def setPiece(self, piece):
#         self.piece = piece

#     def emptySquare(self):
#         self.piece = None

# Euler Project 1 ||Correct||
# sum = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i


# # Euler Project 2 ||Correct||
# fib1 = 1
# fib2 = 1
# sum = 0
# result = 0
# while result < 4000000:
#     if result%2 == 0:
#         sum += result
#     fib1  = fib2
#     fib2 = result
#     result = fib1 + fib2



# Euler Project 3 ||Correct||
def findFactors(n):
    max = 0
    while n % 2 == 0: # if 2 can go continuously into it
        max = 2 
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2): # for all numbers above, stopping at sqrt(n) skipping evens+
        while n % i == 0:
            max = i
            n //= i
    return n if n > 2 else max


# Euler Project 4 ||Complete||
# Naive Solution with strings
def largestPal():
    maxPal = 0
    for x in range(100, 1000):
        for y in range(100,1000):
            num = x * y
            test = str(num)
            reversal = test[::-1]
            if len(test) % 2 ==0: 
                if test[:len(test)//2] == reversal[:len(test)//2] and num > maxPal:
                    maxPal = num
            else:
                if test[:len(test)//2] == reversal[:len(test)//2 + 1] and num > maxPal:
                    maxPal = num
    return maxPal


# Euler Project 5 ||Complete||
# used prime factorization


# Euler Project 6 ||Complete||
def euler6():
    sumSquares = 0
    squaresSum = 0
    for i in range(1,101):
        sumSquares += i**2
        squaresSum += i
    end = squaresSum ** 2
    return end-sumSquares

# sieve

def find_prime(n):
    sieve = [True] * n
    primeList = []
    for i in range(2, n):
        if sieve[i]:
            primeList.append(i)
            for p in range(i*i,n,i):
                sieve[p] = False
    return primeList

def find_prime_sum(n):
    summed, sieve = 0, [True] * n
    for i in range(2, n):
        if sieve[i]:
            summed += i
            for p in range(i*i,n,i):
                sieve[p] = False
    return summed
# Euler Project 7 ||In Progress||


# Euler project 11 ||In Progresss||
def grid():
    ways = [[0,1], [1,0], [-1,1], [1,-1], [-1, 0], [0, -1]]




# Euler project 347 ||Complete||
def euler347(n):
    s = 0
    primes = find_prime(n//2 + 1)
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            max = 0
            q = primes[i]
            l = primes[j]
            x = q*l
            if x <= n:
                for a in range(1, int(log(n/l, q)+1)+1):
                    for b in range(1, int(log(n/q, l)+1)):
                        if n >= (q**a)*(l**b) > max:
                            max = (q**a)*(l**b)
                s += max
            else:
                continue
    return s


# STOLEN CODE TEST TO SEE
# LIMIT = 10000000

# primes = euler.primesTo(LIMIT+1)

# def best(p,q):
#     a = 1
#     maximum = 0
#     while p**a * q <= LIMIT:
#         b = 1
#         while p**a * q**b <= LIMIT:
#             maximum = max(maximum, p**a * q**b)
#             b += 1
#         a += 1
#     return maximum

# total=0
# for i in xrange(len(primes)):
#     for j in xrange(i+1, len(primes)):
#         if primes[i]*primes[j] > LIMIT: break
#         total += best(primes[i], primes[j])
            
# print total


def prime_factors(n):
    l = []
    while n % 2 == 0:
        if 2 in l:
            n /= 2
        else:
            l.append(2)
            n /= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in l:
                n /= i
            else:
                l.append(int(i))
                n /= i
    if n > 2 and n not in l:
        l.append(n)
    return l

# new function to check the lengths of phi(n) and n perm check doesn't workf
def totient_function_q(number):
    l = []
    p = prime_factors(number)
    phi = 1
    for i in p:
        q = 1 - 1 / i
        phi *= q
    phi *= number
    if len(str(phi))-2 == len(str(number)) and all(a in str(phi) for a in str(number)) is True:
        return number/phi, number
    else:
        return None

def eras_sieve(m, n):
    sieve = [True] * n
    primeList = []
    for i in range(2, sqrt(n)):
        if sieve[i]:
            primeList.append(i)
            for p in range(i*i,n,i):
                sieve[p] = False
    return primeList


def is_perm(a, b):
    return sorted([d for d in str(a)]) == sorted([d for d in str(b)])



def euler70(n):
    answer = 0
    best = 200
    primes = find_prime(10000)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            l,p = primes[i], primes[j]
            q = l * p
            if q < n:
                phi = (l-1) * (p-1)
                ratio = q/phi
                if is_perm(phi, q) and best > ratio:
                    best = q/phi
                    answer = q
                    factors = primes[i], primes[j], phi
            
    return answer, best, factors

def totient_function_q(number):
    l = []
    p = prime_factors(number)
    phi = 1
    for i in p:
        q = 1 - 1 / i
        phi *= q
    phi *= number
    return number/phi

# tracking to see if i can calculate pythag triples
def pythag_triples(n):
    i = 0
    start = time.time()
    t = int(sqrt(2 * n))
    for x in range(1, t +1, 2):
        for m in range(x+2, int(sqrt(2*n - x**2)) + 1, 2):
            if gcd(x, m) == 1:
                # q = x*m
                # l = (m**2 - x**2)/2
                # c = (m**2 + x**2)/2
                # trips.append((q,l,c))
                # if c < n:
                i += 1
    end = time.time()
    return i, end-start



def mergeSort(arr):
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def totient_function(number):
    l = []
    p = prime_factors(number)
    phi = 1
    for i in p:
        q = 1 - 1 / i
        phi *= q
    phi *= number
    return phi


def primesieve(limit=64 * 10 ** 6):
    start = time.time()
    sieve = [0] * (limit + 1)
    sieve[1] = 1
    sieve[2::2] = 2
    for i in range(3, limit + 1, 2):
        if not sieve[i]:
            sieve[i::i] = i
    end = time.time()
    return end - start

