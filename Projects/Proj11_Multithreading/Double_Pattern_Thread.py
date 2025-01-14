import threading
import time

def thread_one(name, delay):
    count1 = 5
    
    for x in range(0,999):
        print("\n" +name + " " + format(count1))
        time.sleep(delay)
        count1 += 10
    
def thread_two(name, delay):
    count2 = 0
    
    for x in range(0,999):
        print("\n" + name + " " + format(count2))
        time.sleep(delay)
        count2 += 10
    
if __name__ == "__main__":
    t1 = threading.Thread(target = thread_one, args = ("Thread-1", 0.001))
    t2 = threading.Thread(target = thread_two, args = ("Thread-2", 0.001))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Over")
