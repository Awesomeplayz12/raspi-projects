from pynput import keyboard
import threading
from queue import Queue
q = Queue(maxsize = 10)

def on_press(key):
    print("Pressed " , key)
    
def on_release(key):
    print("Released " , key)
    
    if key == keyboard.Key.esc:
        q.put("1")
    
with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
    listener.join()
    
def execute_thread():
    while True:
        a = q.get()
        
        if a == "1":
            listener.join()
            
            break
    
if __name__ == "__main__":
    execution_thread = threading.Thread(target = execute_thread)
    
    execution_thread.start()
    
    execution_thread.join()
