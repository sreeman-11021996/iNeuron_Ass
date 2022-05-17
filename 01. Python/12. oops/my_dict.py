class dict_parser:
    
    def __init__ (self,test_dict):
        try:
            if type(test_dict) == dict:
                self.dict = test_dict
            else:
                raise Exception(test_dict," - Not a dictionary")
        except Exception as e:
            print("Error! -> ",e)
    
    def get_keys (self):
        return self.dict.keys()
    
    def get_values (self):
        return self.dict.values()
    
    def insert_dict (self,key,value):
        self.dict[key] = value
    
    def display (self):
        print(self.dict)
    
    def user_input (self):
        self.dict = eval(input())
        print(type(self.dict))
        print(self.get_keys())
        print(self.get_values())