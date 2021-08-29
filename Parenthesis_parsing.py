from collections import deque
import random

class Parser():
    open = ['(','[','{']
    close = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    #Checks if a given string formed of '[]()' has proper formatting
    def parse(parenthesis):
        stack = deque()#append and pop
        
        for i in parenthesis:

            if(i in Parser.open):
                stack.append(i)
            elif(not stack):
                return False
            elif(not stack.pop() == Parser.close[i]):
                return False
        if(stack):
            return False
        return True
    def generate_random(N=10):
        chars = Parser.open.copy()
        chars.extend(list(Parser.close.keys()))
        return ''.join(random.choices(chars, k=N))


len=10
tests = 100000
iterations = 50
valid = [0]*iterations

for r in range(iterations):
    for i in range(tests):
        gen = Parser.generate_random(len)
        if(Parser.parse(gen)):
            valid[r] += 1
            #print(gen)

mean = sum(valid)/iterations
variance = sum([((x - mean) ** 2) for x in valid]) / (iterations-1) #Bessel's corection for sample data
stddev = variance ** 0.5

print("mean = {0:0.1f}".format(mean))
print("variance = {0:0.1f}".format(variance))
print("std = {0:0.1f}".format(stddev))