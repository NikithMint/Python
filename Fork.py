import os
def parentchild():
   n = os.fork()
   if n > 0:
    print("Parent process : ", os.getpid())
   else:
    print("Child proces : ", os.getpid())
# Driver code
parentchild()
