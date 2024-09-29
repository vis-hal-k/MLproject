import sys
import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    # exc_info is excecution info and it gives three important information:
    # The exc_tb give all the information on which file the exception has occurred on which line number exception has occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception): # Exception is a parent class of CustomException
# This Exception is python built-in class. 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        # This is all information in CustomException class so when I raise this class first error_message details will call and we get particular error_message 
    def __str__(self):
        return self.error_message
    

    # Complete details from chatGPT
    '''
    Code Breakdown:
1. error_message_detail Function:
  *This function captures the details about the    exception that occurs, such as:
     ** The file where the error occurred (co_filename).
     ** The line number where the error happened  (tb_lineno).
      ** The actual error message itself (str(error)).
   *It uses sys to capture exception information (exc_info), which holds details about the exception.

   *It returns a formatted error message with details of where and what error occurred.

2. CustomException Class:

    *This class inherits from Python's built-in Exception class.

    *The __init__ method initializes the exception with an error message and error details, which are passed to the error_message_detail function to create a detailed error message.

    *The __str__ method is overridden to return the detailed error message when the exception is converted to a string (e.g., when it is printed or logged).

3. super().__init__ Issue:


    '''

# Lets test the exception handling
'''
if __name__ == "__main__" :
    try:
        a = 1/0 
    except Exception as e:
        logging.info("Divide by Zero error")
        raise CustomException(e,sys) 
'''
