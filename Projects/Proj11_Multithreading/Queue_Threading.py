from queue import Queue
import threading
import time

q = Queue(maxsize = 10)

def execute_thread():
    count = 0
    
    while True:
        time.sleep(0.001)
        count += 1
        
        if q.qsize() > 0:
            command = q.get()
            print(command)
            
            if command == "stop":
                print("Exiting execution thread...")
                break
                
            if command == "print":
                print(format(count) + "\n")
                
            if command == "cringe":
                print("that is nanna \n")
        
def in_thread(thread_object):
    while True:
        a = input("\n")
        q.put(a)
        
        if a == "stop":
            thread_object.join()
            print("Exiting input thread...")
            break
        
if __name__ == "__main__":
    execution_thread = threading.Thread(target = execute_thread)
    input_thread = threading.Thread(target = in_thread, args = (execution_thread,))
    
    execution_thread.start()
    input_thread.start()
    
    execution_thread.join()
    input_thread.join()
