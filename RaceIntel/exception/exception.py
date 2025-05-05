import sys
from RaceIntel.logging import logger

class CustomException(Exception):
    def __init__(self, error_msg: Exception, error_detail: sys):
        self.error_msg = error_msg
        _, _, exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f"""
            Error occured in 
            python script name: [{self.file_name}]
            line number: [{self.lineno}] 
            error message: [{str(self.error_message)}]
            """


if __name__ == "__main__":
    try:
        logger.logging.info("enter try block")
        a = 1/0
    except Exception as e:
        logger.logging.error(CustomException(e, sys))
        raise CustomException(e, sys)