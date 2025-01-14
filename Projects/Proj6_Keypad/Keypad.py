import RPi.GPIO as GPIO
import time

class keypad():
    KEYPAD = [
        [1,2,3,"A"],
        [4,5,6,"B"],
        [7,8,9,"C"],
        ["*",0,"#","D"],
        ]
    
    ROW = [2,3,4,14]
    COLUMN = [15,18,17,27]
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
    
    def getKey(self):
        
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
            
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
            
        rowVal = -1
        for i in range(len(self.ROW[i])):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                
        if rowVal < 0 or rowVal > 3:
            self.exit()
            return
        
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
            
        GPIO.setup(self.ROW[rowVal], GPIO.out)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
        
        colVal = -1
        for j in range(len(self.COLUMN[j])):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                colVal = j
                
        if colVal < 0 or colVal > 3:
            self.exit()
            return
        
        self.exit()
        return self.KEYPAD[rowVal][colVal]
    
    def exit(self):
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down = GPIO.PUD_UP)
            
if __name__ == '__main__':
    kp = keypad()
    while True:
        digit = None
        while digit == None:
            digit = kp.getKey()
        print(digit)
        time.sleep(0.5)
