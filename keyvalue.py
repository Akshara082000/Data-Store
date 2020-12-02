import json
import os
import sys
import time
import threading

class Storage:

    dict={}

    """
    If location mentioned,after checking that path exits the file will be loaded to perform operations.If not mentioned a new file will be created or previous file in default
    path will be loaded. 
      
    """
    def __init__(self,location=""):

        self.lock=threading.Lock()
        if location=="":

           self.name="datastore.json"
           self.location = os.path.expanduser('~')
           self.location = os.path.join(self.location,"Documents",self.name)
           self.file=open(self.location,"a+")
           load_check=os.stat(self.location)
           if load_check.st_size!=0:
              with open(self.location,'r+') as f:
                    self.dict=json.load(f)
                    
            
        else:
           self.location = os.path.expanduser(location)

           if os.path.exists(self.location):
              load_check=os.stat(self.location)
              if load_check.st_size!=0:
                  with open(self.location,'r+') as f:
                      self.dict=json.loads(f)
                     
           else:

             print("Path doesn't exists")
             exit()

    """
    
    Syntax add(key,value,lifetime)

            1.Key should not exits,should be less than 32 chars.
            2.Value should be less than 6kb
            3.Adding this key/value should not make a file exceed 1GB.
            4.All conditions are checked,if satisfied key will be added to the file.

            To calculate lifetime a key created time will also be stored.
            Adding key-value will be stored as JSON. 

    """
    def add(self,key,value,lifetime=0):

        if len(key)>32:

           print("Error:Key Size exceeded.Maxmimum size allowed is only upto 32 characters")
           return

        else:

            if sys.getsizeof(value)> 16000:

               print("Error:Value Size exceeded.Maxmimum size allowed is only upto 16kb")
               return
       
            if bool(self.dict):

                if self.dict.__contains__(key):
                   
                    print(key+" already exits in the file.")
                    return 

                else:

                     temp_dict={}
                     temp_list=[]
                     livetime={}
                     livetime["created_time"]=time.time()
                     livetime["lifetime"]=lifetime
                     value.update(livetime)
                     temp_list.append(value)
                     temp_dict[str(key)]=value
                     file_size=os.stat(self.location)
                     file_size=file_size.st_size
                     dict_size=sys.getsizeof(temp_dict)

                     if  (dict_size+file_size) > (1024*1024*1024):

                          print("Save Failed.Memory limilt will be exceeded above 1GB.")
                          return

                     else:

                         
                         self.lock.acquire(blocking=True)
                         with open(self.location) as f:
                             data=json.load(f)
                             data[key]=temp_list  

                         with open(self.location,"w+") as f:
                             f.write(json.dumps(data))
                             self.dict.update(temp_dict)
                         self.lock.release()
                            

            else:

                     temp_dict={}
                     temp_list=[]
                     livetime={}
                     livetime["created_time"]=time.time()
                     livetime["lifetime"]=lifetime
                     value.update(livetime)
                     temp_list.append(value)
                     temp_dict[str(key)]=temp_list
                     self.lock.acquire(blocking=True)
                     with open(self.location,'a+') as f:
                        f.write(json.dumps(temp_dict))
                        self.dict.update(temp_dict)
                     self.lock.release()


    """
      Read will display value for the given key,if key exists and live time is not over.
    """

    def read(self,key):
        
        if self.dict.__contains__(key):

            if self.dict[key][0]["lifetime"]==0 or (time.time() - self.dict[key][0]["created_time"]) < self.dict[key][0]["lifetime"]:
               print(self.dict[key])
               return self.dict[key]
 
            else:
 
               print("Live Time is over for this key")
               return 
        else:

            print("Key doesn't exists")
            return

       """
        delete will remove key and value for the given key,if key exists and live time is not over.
   
       """


    def delete(self,key):


        if self.dict.__contains__(key):

            data=self.dict[key]

            if data[0]["lifetime"]==0 or (time.time() - data[0]["created_time"]) < data[0]["lifetime"]:

               self.dict.pop(key)
               self.lock.acquire()
               with open(self.location,'w+') as f:
                   f.write(json.dumps(self.dict))
               self.lock.release()
            else:
 
               print("Live Time is over for this key")
               return 
        else:

            print("Key doesn't exists")
            return        

              
    def display(self):

        print(self.dict)       




