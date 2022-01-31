# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:28:46 2022

@author: dcsem
"""

#   Map() Creates a new, empty map. It returns an empty map collection.
#   put(key,val) Adds a new key-value pair to the map. If the key is already in the
# map then replace the old value with the new value.
#   get(key) Given a key, returns the value stored in the map or None otherwise.
#   del Deletes the key-value pair from the map using a statement of the form del map[key].
#   len() Returns the number of key-value pairs stored in the map.
#   in Return True for a statement of the form key in map, if the given key is
# in the map, False otherwise.

class HashTable:
    
    """An implementation of Map ADT, using open addressing with linear probing,
        that takes constant time O(1) in the best case to find an item.
        The worst case depends on the average number of comparisons, but since
        the table is design to expand itself at load factor of 0.7, the average
        number of comparisons it needs to make to find an item is approximately 2.16."""        
    
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        
        load_check = self.laod_factor_calc()
        if load_check >= 0.7:
            new_size = next_prime(self.size)
            for new_slot in range(self.size,new_size):
                self.slots.append(None)
                self.data.append(None)
            self.size = new_size
            
        
        if type(key) == str:
            hashvalue = self.str_hashfunction(key,len(self.slots))
        else:
            hashvalue = self.hashfunction(key,len(self.slots))
    
        if self.slots[hashvalue] == None:
          self.slots[hashvalue] = key
          self.data[hashvalue] = data
        else:
          if self.slots[hashvalue] == key:
            self.data[hashvalue] = data  #replace
          else:
            nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
              nextslot = self.rehash(nextslot,len(self.slots))
    
            if self.slots[nextslot] == None:
              self.slots[nextslot]=key
              self.data[nextslot]=data
            else:
              self.data[nextslot] = data #replace
    
    def hashfunction(self,key,size):
         return key%size
     
    
    def laod_factor_calc(self):
        
        full = 0
        for i in self.slots:
            if i != None:
                full +=1
            
        return full/len(self.slots)
        
     
    def str_hashfunction(self, key,size):
        
        sum = 0
        count = 1
        for pos in range(len(key)):
            sum = sum + (ord(key[pos])*count)
            count +=1
        
        return sum%size
        
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def get(self,key):
        
      if type(key) == str:
          startslot = self.str_hashfunction(key,len(self.slots))
      else:
          startslot = self.hashfunction(key,len(self.slots))
    
      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
    
    def __delitem__(self,key):
        
        self.delete(key)
        
    def delete(self,key):
        if type(key) == str:
            org_hash_val = self.str_hashfunction(key, len(self.slots))
        else:
            org_hash_val = self.hashfunction(key, len(self.slots))
        
        if self.slots[org_hash_val] == key:
            self.slots[org_hash_val] = None
            self.data[org_hash_val] = None

            
        else:
            next_slot = self.rehash(org_hash_val, len(self.slots))
            stop = False
            while self.slots[next_slot] != key or self.slots[next_slot] != None \
                and not stop:
                next_slot = self.rehash(next_slot, len(self.slots))
                if next_slot == org_hash_val:
                    stop = True
            
            if self.slots[next_slot] == key:
                self.slots[next_slot] = None
                self.data[next_slot] = None

                
    def __len__(self):
        return self.size
    
    def __contains__(self, key):
        
        found = False
        for i in self.slots:
            if i == key:
                found = True
        return found
    
def is_prime(x):
    return all(x % i for i in range(2, x))

def next_prime(x):
    return min([a for a in range(x+1, 2*x) if is_prime(a)])







