import logging

logging.basicConfig(filename = "log_my_tuple.log", level = logging.INFO, 
                   format = '%(asctime)s %(levelname)s %(message)s')

class my_tuple:
    def __init__ (self,my_tuple):
        self.my_tuple = my_tuple
        logging.info("my_tuple object created and initialized")
        
    # index -> to get the first occurence index of the value in the tuple
    def my_index (self,val):
        flag = False
        # condition for empty tuple:
        if len(self.my_tuple) == 0:
            flag = True
            
        for i in range(len(self.my_tuple)):
            # check each velue
            if self.my_tuple[i] == val:
                index = i
                logging.info("Index of ",value, " in the tuple returned")
                break
            elif i == (len(self.my_tuple) - 1):
                flag = True
            
        # value not found Error
        if flag:
            try:
                raise Exception(val," - Value not found in Tuple")
            except Exception as e:
                logging.error(e)
                index = None
        
        return index
    
    # count -> it counts the number of occurences of a particular value in the list
    def my_count (self,val):
        # checks the first occurence of the value
        index = self.my_index(val)
        if not index:
            count = 0
        else:
            count = 1
            # run a for loop from the index position after the first occurence index
            for i in range(index+1,len(self.my_tuple)):
                if self.my_tuple[i] == val:
                    count+=1
            #logging.info("Count of ", value, " in the Tuple is returned")
        return count
    