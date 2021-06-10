# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import multiprocessing as mp


def job(q, max_range):
    res = 0
    
    for i in range(max_range):
        res += i + i ** 2 + i** 3
    
    q.put(res)

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q, 10))
    p2 = mp.Process(target=job, args=(q, 1000))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    # first value
    res1 = q.get() 

    # second value
    res2 = q.get()

    print(res1, res2)