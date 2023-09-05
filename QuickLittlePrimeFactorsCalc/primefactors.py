import numpy as np
import time 
from tabulate import tabulate
from primenumgen import primeNumberGenerator


''' 
FINDING THE PRIME FACTORS OF A NUMBER
Finds all of the prime numbers that go into the number and then divides by the largest divisor as
many times as results in an integer before going onto the next lowest factor
'''
def primefactors(number=None):
    expectedTime = 8.978461048568194e-08*number**2
    print('Expected Time:',expectedTime,'s')
    startTime = time.time()
    primeFactorsnumber = number #keeps record of number being factorised for later check
    primeNumbers = primeNumberGenerator(number)
    possiblePrimes = []
    if number == primeNumbers[len(primeNumbers)-1]:
        primeFactors = [number]
        powers = [1]
    else:
        for i in range(len(primeNumbers)):
            if primeNumbers[i] <= (number/2): #prime factors can only be a half or less a half of the number
                possiblePrimes.append(primeNumbers[i]) #adds all primes small enough to be factors
            else:
                break
        primeFactors = []
        for i in range(len(possiblePrimes)):
            if (number/possiblePrimes[i]).is_integer() is True: # if divisible the possible prime is found to be a prime factor
                    
                    primeFactors.append(possiblePrimes[i])


        powers = []

        for i in range(len(primeFactors)):
            power = 0
            val = 0 # val is the factor to the next highest power
            factor = primeFactors[len(primeFactors)-i-1] #searches factors highest to lowest as they are in ascending order in the array
            while val <= number: #checks val is small enough to be a factor
                
                val = factor**power
                
                x = number/val
                ''' 
                if the next highest power of the factor is not divisible the while loop ends
                '''
                if (x).is_integer() == True:
                    power+=1
                    
                else:
                    power-=1 #the power that is found to not be a divisor is one too high
                    break
            powers.append(power)
            number = number/(factor**power)
        
        
    powers.reverse() # the highest factors power is appended first and so the array needs to be reversed for the factor and its power to align

    facts = ['Factors','Power'] # adding table headers

    ''' 
    solution checking ensures that all the factors to their powers multiply
    to make the original number
    '''

    solutionChecking = [] 
    for i in range(len(powers)):
        facts.append(primeFactors[i])
        facts.append(powers[i])
        solutionChecking.append(primeFactors[i]**powers[i])
    total = 1
    for i in range(len(solutionChecking)):
        total = total*solutionChecking[i]

    factsTable = np.reshape(facts,(len(powers)+1,2))

    ''' 
    prints table if the total from the solution checking process 
    equals the intial input number value
    '''
    if total == primeFactorsnumber:
        print(tabulate(factsTable, headers='firstrow', tablefmt='fancy_grid'))
        

    else:
        print('unsuccessful')

    endTime = time.time()
    totalTime = endTime-startTime
    print(totalTime)
    #times.append(totalTime)
    #print(primeFactorsnumber)
    #numbers.append(primeFactorsnumber)
    return [totalTime,primeFactorsnumber]




