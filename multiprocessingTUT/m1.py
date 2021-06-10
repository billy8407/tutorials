from multiprocessing import Pool    
def f(x):
    return x^2

def f2():
    p = Pool(5)
    return p.map(f, [1,2,3,4,5])