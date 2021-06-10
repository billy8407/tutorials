import multiprocessing as mp


def job(n):
    print(n * n)
    return n * n

if __name__ == '__main__':
    p1 = mp.Process(target=job, args=(2,))
    p1.start()
    p1.join()