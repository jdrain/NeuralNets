import numpy

def SimpleGuesser(desiredOuput, inputOne, inputTwo):
    sampler = numpy.random
    bestOutput = inputOne * inputTwo
    for i in range(0, 100000):
        sample = sampler.sample()
        newOutput = (inputOne + sample) * (inputTwo + sample)
        if abs(newOutput - desiredOuput) < abs(bestOutput - desiredOuput):
            bestOutput = newOutput
    print(bestOutput)

if __name__ == '__main__':
    SimpleGuesser(6, 1.9, 2.8)