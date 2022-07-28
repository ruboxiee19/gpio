import threading
import time
from tkinter import * 
from tkinter.ttk import *
from time import strftime
from datetime import datetime
import urllib.request


#import RPi.GPIO as GPIO
#import MFRC522
import signal
import time
 


Name_Disp = "NAME NAME NAME"
Inn_Disp = "150"
In_Out = "OUT"

Remaing = 0;



file1 = open("inpeople.txt", "a")  # append mode
file1.close()
def allgui():


    root = Tk()
    root1 = Tk()
    root.wm_attributes('-transparentcolor', '#ab23ff')
    root.title('RFID')
    root.attributes('-fullscreen',True)
    root1.attributes('-fullscreen',True)

    bg = PhotoImage(file = "IMAGE.png")
   
    bg1 = PhotoImage(file = "IMAGE.png")

    label1 = Label( root, image = bg)
    label1.place(x = 0,y = 0,relwidth=1, relheight=1)

    
    # label2 = Label( root1, image = bg1)
    # label2.place(x = 0,y = 0,relwidth=1, relheight=1)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    def time():
        string = strftime('%H:%M:%S %p')
        TIme.config(text = string)
        TIme.after(1000, time)
        print("aftettr")
        NAme.config(text = Name_Disp)
        INn.config(text = In_Out)
        NOp.config(text = Inn_Disp)

    TIme = Label(root, font = ('calibri', 40, 'bold'),
                foreground = 'BLACK',background="#ab23ff")
    
    NAme = Label(root, text="NAME", font = ('calibri', 40, 'bold'),foreground = 'BLACK',background="#ab23ff")
    NOp = Label(root, text="", font = ('calibri', 20, 'bold'),foreground = 'BLACK',background="#ab23ff")
    INn = Label(root, text="INN", font = ('calibri', 30, 'bold'),foreground = 'BLACK',background="#ab23ff")
    
   # TIme.pack()
    TIme.place(bordermode=INSIDE, x =0, y = 0)
   
    #NAme.pack()
    NAme.place(bordermode=INSIDE, x =(screen_width/2), y = (screen_height/2),anchor = N)
   
    #INn.pack()
    INn.place(bordermode=INSIDE, x =(screen_width/2), y = (screen_height/1.5),anchor = N)
   
    #NOp.pack()
    NOp.place(bordermode=INSIDE, x =(screen_width/1.03), y = (screen_height/1.03),anchor = SW)



   # TIme.grid(column=0, row=0,sticky =SE)
  #  NAme.grid(column=1, row=0)
 #   INn.grid(column=1, row=1,sticky =SE)
#    NOp.grid(column=2, row=2,sticky =SE)

    time()
    mainloop()


#def ifnetwork():







def ifnonetwork():
    while True:
        print('Loop 3')
        time.sleep(1)




thread1 = threading.Thread(target=allgui)
thread1.start()

#thread2 = threading.Thread(target=ifnetwork)
#thread2.start()


thread3 = threading.Thread(target=ifnonetwork)
thread3.start()

while True:
 #   print("hii")



    continue_reading = True
 
    def end_read(signal,frame):
        global continue_reading
        print ("Ctrl+C captured, ending read.")
        continue_reading = False
        GPIO.cleanup()
        
    signal.signal(signal.SIGINT, end_read)
    MIFAREReader = MFRC522.MFRC522()
    while continue_reading:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if status == MIFAREReader.MI_OK:
            print ("Card detected")
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
            
            print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+','+str(uid[4]))  
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            
            MIFAREReader.MFRC522_SelectTag(uid)
            Uid=str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+','+str(uid[4])
            print(Uid);
            
            string1 = Uid
            file1 = open("inpeople.txt", "r")
            flag = 0
            index = 0
            for line in file1:  
                index += 1 
                if string1 in line:
                  flag = 1
                  break 
            file1.close()

            if flag == 0: 
               print('String', string1 , 'Not Found')
               In_Out = "IN"
               file1 = open("inpeople.txt", "a")  # append mode
               file1.write(Uid + "\n")
               file1.close()
               

            else:
               with open('inpeople.txt', 'r') as file:
                   text = file.read()
               print('String', string1, 'Found In Line', index)
               with open('inpeople.txt', 'w') as file:
                   new_text = text.replace((Uid + "\n"), '')
                   file.write(new_text)
                   In_Out = "OUT"
               
            string = strftime('%H:%M:%S %p')

            def connect(host='http://google.com'):
                try:
                    urllib.request.urlopen(host) #Python 3.x
                    return True
                except:
                    return False
            if connect():
                print("internet")
                


                
            else:
                print("nointrer")