import math

#class Interpreter:
#    def __init__(self):
#        pass
#
#    def Convert(self, expression):
#        slope = FindSlope(expression)

def FindSlope(exp):
    slopeChar = ''
    for index, char in enumerate(exp):
        if index == 1 and char == 'x':
            slopeChar == '1'
        else: 
            if char == 'x' and index != 1:
                for i in range(index):
                    slopeChar += exp[i]

    return slopeChar

print(FindSlope('x'))