from gpiozero import LED
import time

a = LED(2)
b = LED(3)
c = LED(4)
d = LED(17)
e = LED(27)
f = LED(22)
g = LED(10)
dp = LED(9)

def diagnostic():
    j = "0"
    while j != "3":
        print("Which type of diagnostic test do you want?")
        j = input("1. Normal \n2. Snake \n3. Exit \n")
        if j == "1":
            a.on()
            time.sleep(0.5)
            a.off()
            time.sleep(0.5)
            b.on()
            time.sleep(0.5)
            b.off()
            time.sleep(0.5)
            c.on()
            time.sleep(0.5)
            c.off()
            time.sleep(0.5)
            d.on()
            time.sleep(0.5)
            d.off()
            time.sleep(0.5)
            e.on()
            time.sleep(0.5)
            e.off()
            time.sleep(0.5)
            f.on()
            time.sleep(0.5)
            f.off()
            time.sleep(0.5)
            g.on()
            time.sleep(0.5)
            g.off()
            time.sleep(0.5)
            dp.on()
            time.sleep(0.5)
            dp.off()
            time.sleep(0.5)
        if j == "2":
            a.on()
            time.sleep(0.5)
            b.on()
            time.sleep(0.5)
            c.on()
            time.sleep(0.5)
            d.on()
            time.sleep(0.5)
            e.on()
            time.sleep(0.5)
            f.on()
            time.sleep(0.5)
            g.on()
            time.sleep(0.5)
            dp.on()
            time.sleep(0.5)
            time.sleep(1)
            dp.off()
            time.sleep(0.5)
            g.off()
            time.sleep(0.5)
            f.off()
            time.sleep(0.5)
            e.off()
            time.sleep(0.5)
            d.off()
            time.sleep(0.5)
            c.off()
            time.sleep(0.5)
            b.off()
            time.sleep(0.5)
            a.off()
            time.sleep(0.5)
            time.sleep(1) 
    return
    
def hexadecimal():
    k = "0"
    while k != "3":
        print("Do you want ascending order or descending order?")
        k = input("1. Ascending \n2. Descending \n3. Exit \n")
        if k == "1":
            a.on()
            f.on()
            e.on()
            d.on()
            c.on()
            b.on()
            time.sleep(1)
            a.off()
            f.off()
            e.off()
            d.off()
            c.off()
            b.off()
           
            b.on()
            c.on()
            time.sleep(1)
            b.off()
            c.off()
      
            a.on()
            b.on()
            g.on()
            e.on()
            d.on()
            time.sleep(1)
            a.off()
            g.off()
            g.off()
            e.off()
            d.off()
        
            a.on()
            b.on()
            g.on()
            c.on()
            d.on()
            time.sleep(1)
            a.off()
            b.off()
            g.off()
            c.off()
            d.off()
     
            f.on()
            g.on()
            b.on()
            c.on()
            time.sleep(1)
            f.off()
            g.off()
            b.off()
            c.off()
     
            a.on()
            f.on()
            g.on()
            d.on()
            c.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            d.off()
            c.off()
     
            a.on()
            f.on()
            e.on()
            d.on()
            c.on()
            g.on()
            time.sleep(1)
            a.off()
            f.off()
            e.off()
            d.off()
            c.off()
            g.off()
       
            a.on()
            b.on()
            c.on()
            time.sleep(1)
            a.off()
            b.off()
            c.off()
      
            a.on()
            f.on()
            g.on()
            c.on()
            d.on()
            e.on()
            b.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            c.off()
            d.off()
            e.off()
            b.off()
        
            a.on()
            f.on()
            g.on()
            b.on()
            c.on()
            d.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            b.off()
            c.off()
            d.off()
            
            e.on()
            f.on()
            a.on()
            b.on()
            c.on()
            g.on()
            time.sleep(1)
            e.off()
            f.off()
            a.off()
            b.off()
            c.off()
            g.off()
            
            f.on()
            e.on()
            d.on()
            c.on()
            g.on()
            time.sleep(1)
            f.off()
            e.off()
            d.off()
            c.off()
            g.off()
      
            a.on()
            f.on()
            e.on()
            d.on()
            time.sleep(1)
            a.off()  
            f.off()
            e.off()
            d.off()
  
            b.on()
            c.on()
            d.on()
            e.on()
            g.on()
            time.sleep(1)
            b.off()
            c.off()
            d.off()
            e.off()
            g.off()
        
            a.on()
            f.on()
            g.on()
            e.on()
            d.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            e.off()
            d.off()
            
            a.on()
            f.on()
            g.on()
            e.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            e.off()
            
        if k == "2":
            a.on()
            f.on()
            g.on()
            e.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            e.off()
            
            a.on()
            f.on()
            g.on()
            e.on()
            d.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            e.off()
            d.off()
            
            b.on()
            c.on()
            d.on()
            e.on()
            g.on()
            time.sleep(1)
            b.off()
            c.off()
            d.off()
            e.off()
            g.off()
            
            a.on()
            f.on()
            e.on()
            d.on()
            time.sleep(1)
            a.off()  
            f.off()
            e.off()
            d.off()
  
            f.on()
            e.on()
            d.on()
            c.on()
            g.on()
            time.sleep(1)
            f.off()
            e.off()
            d.off()
            c.off()
            g.off()
        
            e.on()
            f.on()
            a.on()
            b.on()
            c.on()
            g.on()
            time.sleep(1)
            e.off()
            f.off()
            a.off()
            b.off()
            c.off()
            g.off()
            
            a.on()
            f.on()
            g.on()
            b.on()
            c.on()
            d.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            b.off()
            c.off()
            d.off()
            
            a.on()
            f.on()
            g.on()
            c.on()
            d.on()
            e.on()
            b.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            c.off()
            d.off()
            e.off()
            b.off()
            
            a.on()
            b.on()
            c.on()
            time.sleep(1)
            a.off()
            b.off()
            c.off()
            
            a.on()
            f.on()
            e.on()
            d.on()
            c.on()
            g.on()
            time.sleep(1)
            a.off()
            f.off()
            e.off()
            d.off()
            c.off()
            g.off()
            
            a.on()
            f.on()
            g.on()
            d.on()
            c.on()
            time.sleep(1)
            a.off()
            f.off()
            g.off()
            d.off()
            c.off()
            
            f.on()
            g.on()
            b.on()
            c.on()
            time.sleep(1)
            f.off()
            g.off()
            b.off()
            c.off()
            
            a.on()
            b.on()
            g.on()
            c.on()
            d.on()
            time.sleep(1)
            a.off()
            b.off()
            g.off()
            c.off()
            d.off()
            
            a.on()
            b.on()
            g.on()
            e.on()
            d.on()
            time.sleep(1)
            a.off()
            g.off()
            g.off()
            e.off()
            d.off()
            
            b.on()
            c.on()
            time.sleep(1)
            b.off()
            c.off()
      
            f.on()
            e.on()
            d.on()
            c.on()
            b.on()
            a.on()
            time.sleep(1)
            f.off()
            e.off()
            d.off()
            c.off()
            b.off()
            a.off()      
       
def specific():
    i = "0"
    while i != "16":
        print("What hexadecimal number do you want displayed?")
        i = input("0. 0 \n1. 1 \n2. 2 \n3. 3 \n4. 4 \n5. 5 \n6. 6 \n7. 7 \n8. 8 \n9. 9\n10. A \n11. B \n12. C \n13. D \n14. E \n15. F \n16. Exit \n")
        if i == "0":
            print("0")
            f.on()
            e.on()
            d.on()
            c.on()
            b.on()
            a.on()
            time.sleep(2.5)
            f.off()
            e.off()
            d.off()
            c.off()
            b.off()
            a.off()
        if i == "1":
            print("1")
            b.on()
            c.on()
            time.sleep(2.5)
            b.off()
            c.off()
        if i == "2":
            print("2")
            a.on()
            b.on()
            g.on()
            e.on()
            d.on()
            time.sleep(2.5)
            a.off()
            g.off()
            g.off()
            e.off()
            d.off()
        if i == "3":
            print("3")
            a.on()
            b.on()
            g.on()
            c.on()
            d.on()
            time.sleep(2.5)
            a.off()
            b.off()
            g.off()
            c.off()
            d.off()
        if i == "4":
            print("4")
            f.on()
            g.on()
            b.on()
            c.on()
            time.sleep(2.5)
            f.off()
            g.off()
            b.off()
            c.off()
        if i == "5":
            print("5")
            a.on()
            f.on()
            g.on()
            d.on()
            c.on()
            time.sleep(2.5)
            a.off()
            f.off()
            g.off()
            d.off()
            c.off()
        if i == "6":
            print("6")
            a.on()
            f.on()
            e.on()
            d.on()
            c.on()
            g.on()
            time.sleep(2.5)
            a.off()
            f.off()
            e.off()
            d.off()
            c.off()
            g.off()
        if i == "7":
            print("7")
            a.on()
            b.on()
            c.on()
            time.sleep(2.5)
            a.off()
            b.off()
            c.off()
        if i == "8":
            print("8")
            a.on()
            f.on()
            g.on()
            c.on()
            d.on()
            e.on()
            b.on()
            time.sleep(2.5)
            a.off()
            f.off()
            g.off()
            c.off()
            d.off()
            e.off()
            b.off()
        if i == "9":
            print("9")
            a.on()
            f.on()
            g.on()
            b.on()
            c.on()
            d.on()
            time.sleep(2.5)
            a.off()
            f.off()
            g.off()
            b.off()
            c.off()
            d.off()
        if i == "10":
            print("A")
            e.on()
            f.on()
            a.on()
            b.on()
            c.on()
            g.on()
            time.sleep(2.5)
            e.off()
            f.off()
            a.off()
            b.off()
            c.off()
            g.off()
        if i == "11":
            print("b")
            f.on()
            e.on()
            d.on()
            c.on()
            g.on()
            time.sleep(2.5)
            f.off()
            e.off()
            d.off()
            c.off()
            g.off()
        if i == "12":
            print("C")
            a.on()
            f.on()
            e.on()
            d.on()
            time.sleep(2.5)
            a.off()    
            f.off()
            e.off()
            d.off()
        if i == "13":
            print("d")
            b.on()
            c.on()
            d.on()
            e.on()
            g.on()
            time.sleep(2.5)
            b.off()
            c.off()
            d.off()
            e.off()
            g.off()
        if i == "14":
            print("E")
            a.on()
            f.on()
            g.on()
            e.on()
            d.on()
            time.sleep(2.5)
            a.off()
            f.off()
            g.off()
            e.off()
            d.off()
        if i == "15":
            print("F")
            a.on()
            f.on()
            g.on()
            e.on()
            time.sleep(2.5)
            a.off()
            f.off()
            g.off()
            e.off()  

h = "0"
while h != "4":
    print("Which one do you want?")
    h = input("1. Diagnostic Test \n2. Display all hexadecimals \n3. Display a specific number \n4. Exit \n")
    if h == "1":
        diagnostic()

    if h == "2":
        hexadecimal()
        
    if h == "3":
        specific()
