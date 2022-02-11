import logging 

class log:
    def __init__ (self,file_name = "sql.log",level = "info",format = '%(asctime)s %(levelname)s %(message)s'):
        self.__file_name = file_name
        self.__level = level
        self.__format = format
        self.__basic()
        
    def __basic(self):
        try:
            if self.__level == "info":
                logging.basicConfig(filename = self.__file_name,level = logging.INFO,
                                    format = self.__format)
        except Exception as e:
            print(e)
    
    def __check_msg (self,message):
        if not isinstance(message,str):
            raise Exception("Please enter a string message")
    
    def error (self,message):
        # check the message 
        self.__check_msg(message)
        logging.error(message)
    
    def warning (self,message):
        # check the message 
        self.__check_msg(message)
        logging.warning(message)
    
    def info (self,message):
        # check the message 
        self.__check_msg(message)
        logging.info(message)