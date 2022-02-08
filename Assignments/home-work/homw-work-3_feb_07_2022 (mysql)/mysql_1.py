import mysql.connector as conn
class Database:
    __COLUMNS_REQ = 7
    def __init__ (self):
        try:
            self.__mydb = conn.connect(host = "localhost", user = "root", password = "mysql")
            self.__cursor = self.__mydb.cursor()
        except:
            print("Server could not connect! Some error occured")
        else:
            print("Server Connected")
            
    def create_db (self,db_name = "cardataset"):
        self.__cursor.execute("create database if not exists {db}".format(db = db_name))
    
    def show_db (self):
        self.__cursor.execute("show databases")
        return self.__cursor.fetchall()
    
    def drop_db (self,db_name):
        self.__cursor.execute("drop database if exists {db_var}".format(db_var = db_name))
        self.__mydb.commit()
    
    def __check_db (self,db_name):
        try:
            # check if db exists & use it
            self.__cursor.execute("use {db_val}".format(db_val = db_name))
        except Exception as e:
            print("DataBase not found!",e)
            return True
        else:
            print("DataBase present")
            return False
            
    def __check_table(self,table_name):
        try:
            self.__cursor.execute("select * from {table} where 1".format(table = table_name))
            self.__cursor.fetchall()
        except Exception as e:
            print("New Table",e)
            return True
        else:
            print("Table {table} already exists".format(table=table_name))
            return False

    def create_table(self,table_name,columns = (),db_name = "cardataset"):
        
        # ERROR_1 -> check if database is present
        if self.__check_db(db_name):
            return
        # create the table
        # ERROR_2 -> check if table exists:
        if self.__check_table(table_name):
            if len(columns) == self.__COLUMNS_REQ:
                try:
                    self.__cursor.execute("create table {table_}({col1},{col2},{col3},{col4},{col5},"
                                        "{col6},{col7})".format(table_=table_name,col1=columns[0],
                                                         col2=columns[1],col3=columns[2],
                                                         col4=columns[3],col5=columns[4],
                                                         col6=columns[5],col7=columns[6]))
                except Exception as e:
                    print("Could not create the table!",e)
                else:
                    print("Table created successfully")
    
    def show_table(self,db_name):
        # Error_1 -> check db_name
        if self.__check_db(db_name):
            return
        self.__cursor.execute("use {db_}".format(db_ = db_name))
        self.__cursor.execute("show tables")
        return self.__cursor.fetchall()
    
    def describe_table (self,db_name,table_name):
        # Error_1 -> check db_name
        if self.__check_db(db_name) or self.__check_table(table_name):
            return
        self.__cursor.execute("use {db_}".format(db_ = db_name))
        self.__cursor.execute("describe {table}".format(table = table_name))
        return self.__cursor.fetchall()
    
    def drop_table (self,table_name,db_name):
        self.__cursor.execute("drop table if exists {db_}.{table}".format(db_ = db_name,table = table_name))
        self.__mydb.commit()
    
    def __check_val_str(self,insert_str):
        delimiter = ","
        val_lst = insert_str.split(delimiter)
        if (len(val_lst) == self.__COLUMNS_REQ):
            return True
        else:
            print("Insufficient values for columns")
            return False
        
    def __single_insert (table_name,single_insert):
        if not self.__check_val_str(single_insert):
            return
        self.__cursor.execute("INSERT INTO {table} VALUES ({val})".format(table=table_name,
                                                                      val = single_insert))
        self.__mydb.commit()
    
    def __file_insert (table_name,file_insert):
        import csv
        try:
            with open(file_insert,"r") as fhand:
                data = csv.reader(fhand, delimiter = "\n")
                for i in data:
                    var_lst = (i[0].split(","))
                    str_val = ""
                    # convert the list of values to sql query string
                    for val in var_lst:
                        str_val = str_val + "'" + val + "'" + ", "
                    str_val = str_val[:-2]
                    # insert the query into table
                    self.__cursor.execute("insert into {table} VALUES ({val})".format(
                            table=table_name, val = str_val))
                self.__mydb.commit()
        except Exception as e:
            print(e)
    
    def insert (self,db_name,table_name,single_insert = None,file_insert = None):
        # Error_1 -> check db_name and ERROR_2 -> check if table exists:
        if self.__check_db(db_name) or self.__check_table(table_name):
            return
        
        if (single_insert is not None) and (type(single_insert)==str):
            self.__single_insert(table_name,single_insert)
        
        elif (file_insert is not None):
            self.__file_insert(table_name,file_insert)
                    
    def select (self,db_name="cardataset",table_name="car",cols = "*"):
        # ERROR_1 -> check if database is present
        exp_db = self.__check_db(db_name)
        if exp_db:
            return 
        self.__cursor.execute("select {col_val} from {table_val}".format(col_val = cols,
                                                            table_val = table_name))
        return self.__cursor.fetchall()
    
    def count_records (self,db_name = "cardataset",table_name = "car",cols="*",
                      nest_query=False):
        # Error_1 -> check db_name and ERROR_2 -> check if table exists:
        if self.__check_db(db_name) or self.__check_table(table_name):
            return
        self.__cursor.execute("select count({cols_var}) from {table}".format(cols_var = cols,
                                                            table = table_name))
        return self.__cursor.fetchall()
            
            
    def group_by (self,db_name = "cardataset",table_name="car",gp_col = "buying"):
        # Error_1 -> check db_name and ERROR_2 -> check if table exists:
        if self.__check_db(db_name) or self.__check_table(table_name):
            return
        # group_by col 
        self.__cursor.execute("select {gp_col_var},count(*) as count_records from {table} "
                    "group by {gp_col_var}".format(table = table_name,gp_col_var = gp_col))
        return self.__cursor.fetchall()
    
    def filter_rec (self,filter_val,db_name = "cardataset", table_name = "car",
                    filter_col = "doors",cols = "*"):
        # Error_1 -> check db_name and ERROR_2 -> check if table exists:
        if self.__check_db(db_name) or self.__check_table(table_name):
            return
        self.__cursor.execute("select {cols_var} from {table} where {filt_col} = {filt_val}".
                              format(cols_var = cols,table=table_name,filt_col=filter_col,
                              filt_val = filter_val))
        return self.__cursor.fetchall()
    
    def update (self,db_name = "cardataset", table_name = "car",update_col = "doors",
                prev_val = "2", upd_val = "8"):
        # Error_1 -> check db_name and ERROR_2 -> check if table exists:
        if self.__check_db(db_name) or self.__check_table(table_name):
            return
        self.__cursor.execute("update {table} set {upd_col} = {upd_val_var} where {upd_col} like "
                              "{prev_val_var}".format(table=table_name,upd_col=update_col,
                                upd_val_var = upd_val,prev_val_var = prev_val))
        self.__mydb.commit()