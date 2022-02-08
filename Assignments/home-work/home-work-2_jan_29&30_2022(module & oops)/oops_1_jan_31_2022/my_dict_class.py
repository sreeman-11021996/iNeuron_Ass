import logging

logging.basicConfig(filename = "log_my_dict.log", level = logging.INFO, 
                   format = '%(asctime)s %(levelname)s %(message)s')

class dict_items:
    def __init__ (self,my_dict):
        dict_items = list()
        for key in my_dict:
            dict_items.append((key,my_dict[key]))
        self.dict_items =  dict_items
        logging.info("dict_items created")
        
    def __str__ (self):
        display_str = "dict_items("+str(self.dict_items)+")"
        return display_str

class dict_keys:
    def __init__ (self,my_dict):
        dict_keys = list()
        for key in my_dict:
            dict_keys.append(key)
        self.dict_keys = dict_keys
        logging.info("dict_keys created")

    
    def __str__ (self):
        display_str = "dict_keys("+str(self.dict_keys)+")"
        return display_str
    
class dict_values:
    def __init__ (self,my_dict):
        dict_values = list()
        for key in my_dict:
            dict_values.append(my_dict[key])
        self.dict_values = dict_values
        logging.info("dict_values created")
    
    def __str__ (self):
        display_str = "dict_values("+str(self.dict_values)+")"
        return display_str
    

class my_dict:
    def __init__ (self,my_dict):
        self.my_dict = my_dict
        logging.info("dictionary (my_dict) created")
        #self.keys = 
    
    def __str__ (self):
        return str(self.my_dict)
    
    def my_clear (self):
        self.my_dict = {}
        logging.info("Dictionary is cleared")
        
    def my_copy (self):
        # create a new object:
        new_obj = my_dict(self.my_dict)
        logging.info("Shallow copy performed")
        return new_obj
        
    # classmethod -
    def my_fromkeys (seq,value=None):
        new_dict = dict()
        for i in seq:
            new_dict[i] = value
        new_dict_obj = my_dict(new_dict)
        logging.info("Dictionary created using my_fromkeys")
        return new_dict_obj
    
    # if you want to use my_list object as value
    def display_my_list(self):
        str_ = ""
        for i in self.my_dict:
            str_ = str_ + str(i) + " : " + str(self.my_dict[i].my_list) + " , "
        str_ = str_[:-3]
        to_display = "{" + str_ + "}"
        return to_display
    
    def my_get (self, key, default = None):
        try:
            value = self.my_dict[key]
            return value
        except KeyError as ke:
            logging.error(ke," - Not present in dictionary")
            return default
        
    def my_items (self):
        my_items = dict_items(self.my_dict)
        logging.info("key-value tuples returned")
        return my_items
    
    def my_keys (self):
        logging.info("List of keys of dictionary returned")
        return dict_keys(self.my_dict)
    
    def key_error (self,key):
        try:
            value = self.my_dict[key]
            return None,value
        except Exception as e:
            return e,None
    
    def my_pop (self,key,default=None):
        # check if key exists inside dictionary
        exp,value = self.key_error(key)
        if exp:
            if default is None:
                logging.error(exp, " - Key not in dictionary")
                return 
            else:
                logging.info(exp, " - Key not in dictionary. ",default," value returned")
                return default
        # do pop
        new_dict = dict()
        for k in self.my_dict:
            if k is not key:
                new_dict[k] = self.my_dict[k]
        self.my_dict = new_dict
        logging.info(key," : ",value," - popped out of dictionary")
        return value
    
    def __is_empty (self):
        try:
            if not self.my_dict:
                raise Exception (self.my_dict, " - Dictionary is empty")
        except Exception as e:
            logging.error(e)
            return True
        
    # self.keys -> list
    # self.values -> list
    def my_popitem (self):
        # we can modify this step in class
        if self.__is_empty():
            return None

        last_key = list(self.my_dict)[-1]
        pop_value  = self.my_pop(last_key)
        popitem = (last_key,pop_value)
        logging.info(key," : ",value," - Last item popped out of dictionary")
        return popitem
    
    def my_setdefault(self,key,default=None):
        # check if key exists inside dictionary
        exp,value = self.key_error(key)
        if exp:
            value = default
            self.my_dict[key] = value
            logging.info("Dictionary updated with new key:value pair")
        return value
    
    # use either dictionary or iterables
    def my_update (self,up_dict=None,**kwargs):
        if up_dict:
            for key in up_dict:
                self.my_dict[key] = up_dict[key]
        else:
            for key,value in kwargs.items():
                self.my_dict[key] = value
        logging.info("Dictionary updated")
                
    def my_values (self):
        logging.info("Dictionary values returned")
        return dict_values(self.my_dict)
    
    
