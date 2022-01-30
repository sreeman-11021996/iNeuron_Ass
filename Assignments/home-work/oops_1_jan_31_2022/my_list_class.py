import logging

logging.basicConfig(filename = "log_my_list.log", level = logging.INFO, 
                   format = '%(asctime)s %(levelname)s %(message)s')

class my_list:
    
    def __init__ (self,my_list):
        self.my_list = my_list
        logging.info("my_list object created and initialized")
        
    def __str__ (self):
        return str(self.my_list)
    
    def my_append (self,val):
        new_list = [None]*(len(self.my_list)+1)
        # populate the new list
        new_list[:-1] = self.my_list
        new_list[-1] = val
        
        # copy it to class var.
        self.my_list = new_list
        logging.info(val, " appended to the list ")
    
    def my_clear (self):
        self.my_list = []
        logging.info("List is cleared")
        
    # 3. copy -> it returns a new copy of the list which can be modified without making changes 
    # in the original list
    def my_copy (self):
        # create a new object:
        new_obj = my_list(self.my_list)
        logging.info("Shallow copy performed")
        return new_obj
    
    # index -> to get the first occurence index of the value in the list
    def my_index (self,val):
        flag = False
        # condition for empty list:
        if len(self.my_list) == 0:
            flag = True
            
        for i in range(len(self.my_list)):
            # check each velue
            if self.my_list[i] == val:
                index = i
                logging.info("Index of ",value, " in the list returned")
                break
            elif i == (len(self.my_list) - 1):
                flag = True
            
        # value not found Error
        if flag:
            try:
                raise Exception(val," - Value not found in List")
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
            for i in range(index+1,len(self.my_list)):
                if self.my_list[i] == val:
                    count+=1
            logging.info("Count of ", value, " in the list is returned")
        return count
        
    # 5. extend -> to add the given list with another list and replace it with the first list
    def my_extend (self,ext_list):

        newlen = len(self.my_list) + len(ext_list)
        new_list = [None]*newlen

        new_list[:len(self.my_list)] = self.my_list
        new_list[len(self.my_list):] = ext_list

        self.my_list = new_list
        logging.info("List extended")
        
    def __out_of_range (self,index):
        try:
            if index >= len(self.my_list):
                raise Exception(index," -> Out of Bounds of the list")
            else: 
                return False
        except Exception as e:
            logging.error(e)
            return True
        
    # 7. insert -> syntax (list.insert(index,value))
    def my_insert (self,index,value):
        # check out of bounds error
        if (len(self.my_list))>0:
            if self.__out_of_range(index):
                return 
        else:
            index = 0

        new_list = [None]*(len(self.my_list)+1)

        new_list[:index] = self.my_list[:index]
        new_list[index] = value
        new_list[index+1:] = self.my_list[index:]

        self.my_list = new_list
        logging.info(value, " inserted into list at index ", index)
        
    # empty list Error:
    def __is_empty (self):
        try:
            if not self.my_list:
                raise Exception(self.my_list," -> List is Empty")
        except Exception as e:
            logging.error(e)
            return True
    
    # 8. pop -> syntax (list.pop(index)) -> it returns the element at the index & removes it 
    # from the list
    def my_pop(self,index = -1): 
        # index = -1 to pop last value

        # Error 1 -> check out of bounds error
        if self.__out_of_range(index):
            return None
        # Error 2 -> check if list is empty
        if self.__is_empty():
            return None

        pop_val = self.my_list[index]
        new_list = [None]*(len(self.my_list)-1)

        # filling the new list
        if index == -1:
            new_list = self.my_list[:index]
            logging.info("Popped the last element in list")
        else:
            new_list[:index] = self.my_list[:index]
            new_list[index:] = self.my_list[index+1:]
            logging.info("Popped the element at index ",index," in list")
            
        self.my_list = new_list
        return pop_val
    
    # 9. remove by value -(first occurance only)
    def my_remove (self,value):
        # find index and pop but don't return the value
        index = self.my_index(value)
        if index is not None:
            pop = self.my_pop(index)
            logging.info("Removed ",value," from the list")
    
    # 10. reverse -> reverses the list (in_place)
    def my_reverse (self):
        for i in range(round(len(self.my_list)/2)):
            self.my_list[i],self.my_list[(len(self.my_list)-1)-i] = self.my_list
            [(len(self.my_list)-1)-i],self.my_list[i]
            logging.info("Reverses the list")