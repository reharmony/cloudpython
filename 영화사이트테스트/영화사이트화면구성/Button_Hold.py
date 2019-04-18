'''
Created on 2019. 4. 18.

@author: user
'''
class mywidget(Button):
   def __init__(self, master):
    .... 
        self.bind('<KeyPress-b>', do_bleah)
        self.bind('<KeyRelease-b>',reset_bleah)
        self.reset_bleah() # must initialize the flag!
   def print_bleah(self, event=None):
        if self.bleahOK:
             self.bleahOK = False
             self.set_up_bleah()
             # do other bleah-y stuff if needed
       else:
             self.continue_bleahing() 
   def reset_bleah(self, event=None):
       self.bleahOK = True