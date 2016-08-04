import numpy

#add gate
def AddGate(a, b):
    return a + b

#multiply gate
def MultGate(a, b):
    return a * b

#overall circuit
def Circuit(x, y, z):
    t = AddGate(x, y)
    u = MultGate(t, z)
    return u

if __name__ == '__main__':
    #test this stuff out
    a = 3
    b = -4
    c = 9

    #derivatives of the overall circuit modeled by the function (a+b)*c
    dCircuitWRTa = c
    dCircuitWRTb = c
    dCircuitWRTc = a + b

    #step size
    step = .5

    #initial output
    initial = Circuit(a,b,c)
    print("initially: " + str(initial))

    #iterate and increase
    for i in range(0,10):
        a = a + step * dCircuitWRTa
        b = b + step * dCircuitWRTb
        c = c + step * dCircuitWRTc
        print("step " + str(i) + " " + str(Circuit(a,b,c)))