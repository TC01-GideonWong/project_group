#importing all the other python files
from overheads import*
from cash_on_hand import*
from profit_loss import*

def main_program():
  '''
  This function has no parameters and will run all the other functions from the imported python files
  '''
  overheads_highest()
  coh_difference()
  pl_difference()
  
#running main program
(main_program())
