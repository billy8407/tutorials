# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import multiprocessing as mp
from multiprocessing import pool


def job(x):
    return x*x


def multicore():
    pool = mp.Pool()
    result = pool.map(job, range(10))
    print(result)

    # can't use iterable
    # result = pool.apply_async(job, range(10))
    result = [pool.apply_async(job , (i,)) for i in range(10)]
    result_value = [res.get() for res in result]
    print(result_value)

if __name__ == '__main__':
    multicore()


