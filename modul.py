from ism import ismi
from familiya import familiyasi
from ochistva import ochistvasi
import threading
import time






t1=threading.Thread(target=ismi)
t2=threading.Thread(target=familiyasi)
t3=threading.Thread(target=ochistvasi)

t1.start()
t2.start()
t3.start()