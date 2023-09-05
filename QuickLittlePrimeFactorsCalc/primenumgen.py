import numpy as np
from tabulate import tabulate

'''
PRIME NUMBER GENERATOR
This prime number generator works by dividing integers from 2 to an upper limit by prime numbers
that have already been found. If the number returns non-integer values for all the primes it is
divided by it is determined to be prime

'''

def primeNumberGenerator(upperLimit = None):
        primeNumbers = [2] #the lowest prime is hard coded
        num = 3 #working upwards from the lowest prime

        while num <= upperLimit:
            decimals =[] #all of the non-integer values from the divisions will be appended here
            x =0
            ''' 
            The subsequent for loop looks through every value in the primeNumbers array and detrmines if the number
            is divisible by it. This enables the for loop to update each time a new prime number is found

            '''
            for i in range(len(primeNumbers)): 
                
                if (num/primeNumbers[i]).is_integer() is False: # if a decimal is returned
                    
                    decimals.append(num)
                
            '''
            The following if statement checks to see if all of the divisions returnded decimals as the length of the decimals
            would be equal to the length of the primeNumbers array
            '''         
            if len(decimals) == len(primeNumbers):
                primeNumbers.append(num)
                
            num +=1
        #print('all of the prime numbers under',upperLimit,':',primeNumbers)
        return primeNumbers


primeNumberGenerator(233)


