def solution(denum1, num1, denum2, num2):
    maxDiv = 1
    numeRator = denum1 * num2 + denum2 * num1
    denoMinator = num1 * num2
    for i in range(2, min(numeRator, denoMinator)+1):
        if(numeRator % i == 0 and denoMinator % i == 0):
            maxDiv = i
    answer = [numeRator/maxDiv, denoMinator/maxDiv]
    return answer





import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]




from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]