from queue import Queue
import threading
import time

q = Queue(maxsize = 10)

def execute_thread():
    count = 0
    current_state = "first"
    
    while True:
        time.sleep(1)
        
        if current_state == "running":
                count += 1
                
                if count == 1:
                    print(format(count) + " second")
                    
                else:
                    print(format(count) + " seconds")
                
        if q.qsize() > 0:
            command = q.get()
            
            if command == "exit":
                print("Exiting execution thread...")
                break
            
            if current_state != "first":
                if command == "restart":
                    print("Restarted")
                    count = 0
                    current_state = "running"
                   
            if current_state != "running":
                if command == "start":
                    print("Started")
                    current_state = "running"
            
            if current_state == "running":
                if command == "pause":
                    print("Paused")
                    current_state = "paused"
                    
            if current_state == "paused":
                if command == "resume":
                    print("Resumed")
                    current_state = "running"
                    
            if current_state == "running":
                if command == "stop":
                    print("Stopped")
                    count = 0
                    current_state = "paused"

def in_thread(thread_object):
    while True:
        a = input("start / restart / pause / resume / stop / exit ?\n")
        q.put(a)
        
        if a == "exit":
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
