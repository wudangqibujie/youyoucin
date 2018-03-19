from multiprocessing import Process
import redis
import time
r = redis.Redis(host="localhost",port = "6379")
def A():
    r.lpush("FFTT","bmw")
    for i in range(100):
        time.sleep(1)
        r.lpush("FFTT",str(i))

def B():
    for i in range(10):
        time.sleep(1)
        print(i)

if __name__ == '__main__':
    B()
    A()

