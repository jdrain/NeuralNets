import SimpleNeuralNet
import matplotlib.pyplot as plt

"""
To test my simple neural net and gather some data about it
"""

#function to run some tests
def runTests(initialWeight, step, iterations):
    x=[] #iterations
    y=[] #error
    #iterate through
    for i in range(0, iterations):
        x.append(i)
        y.append(2 - SimpleNeuralNet.testFunction(step, i, initialWeight))
    #generate some plots
    plt.plot(x, y, "bo")
    plt.ylabel("Error")
    plt.xlabel("Iteration")
    plt.suptitle(str(iterations) + " Iteration Simple Neural Net With Initial Weighting " + str(initialWeight) + " And Step Size " + str(step))
    return plt

if __name__ == '__main__':
    #iterations
    for i in range(1, 4):
        #step
        for j in range(1, 4):
            #initial weightings
            for k in range(1, 4):
                test = runTests(k, 10**-j, 10**i)
                test.savefig('plots/plot_'+str(i)+str(j)+str(k)+'.png', bbox_inches='tight')
                test.show()