#!usr/bin/python
import threading
from queue import Queue
import time
import sys
import socket
from datetime import datetime
from colorama import init, Fore

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW

print(f"{GRAY} - -- - - - - - - - - - - - Developed By rizad- - - - - - - - - - - - - --")
print(f"{GREEN} ######                       #####")                                               
print(f"{GREEN} #     #  ####  #####  ##### #     #  ####    ##   #    # #    # ###### #####")     
print(f"{GREEN} #     # #    # #    #   #   #       #    #  #  #  ##   # ##   # #      #    #")    
print(f"{GREEN} ######  #    # #    #   #    #####  #      #    # # #  # # #  # #####  #    #")    
print(f"{GREEN} #       #    # #####    #         # #      ###### #  # # #  # # #      #####")  
print(f"{GREEN} #       #    # #   #    #   #     # #    # #    # #   ## #   ## #      #   #")
print(f"{GREEN} #        ####  #    #   #    #####   ####  #    # #    # #    # ###### #    #")
print(f"{RED}- - - - - - - - - - - - - - - - - PortScanner V1.0- - - - - - - - - - - - - - -  ")                                                                                                             
                                                                                                             
                                                                                                                                                              

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.

print_lock = threading.Lock()



target = input('Enter a remote host to scan :')
t1 = datetime.now()
ip = socket.gethostbyname(target)
print(ip)
print(f"{YELLOW}-" * 60)
print("Please Wait Scanning Remote Host", ip) 
print(f"{YELLOW}-" * 60)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print(f'{GREEN}[+]Port',port, "is open")
        con.close()
    except:
        pass
        
    
    
    


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()
        

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()

# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(30):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()


start = time.time()

# 1080 jobs assigned.
for worker in range(1080):
    q.put(worker)

# wait until the thread terminates.
q.join()
t2 = datetime.now()
total = t2 - t1
print('Scanning Completed in:',total)
