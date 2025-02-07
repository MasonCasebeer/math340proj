import pickle
with open("./data.pkl","rb") as file:
    L=pickle.load(file)
    S=pickle.load(file)
    D=pickle.load(file)
    C=pickle.load(file)
    F=pickle.load(file)
    M=pickle.load(file)


#3 ----- Lists -----
##3.1  How many elements are in the list L?
print(len(L)) 
##3.2  What is the type of the third element in the list L?
print(type(L[2])) 
##3.3  What is the value of the last element of the list?
print((L[5]))
##3.4  What is the 5th character in the string S?
print(S[4])
##3.5  At what index can 5 be found in the list L?
print(L.index(5))
#4 ----- Sets -----
print("Enter set area")
##4.1  How many elements are in the set C?
print(len(C))
##4.2  After adding the four class colors, how many elements are in the set C?
C.update(["red","blue","yellow","red"])
print(len(C))
##4.3  Which of the following are equal to the provided frozenset F?
print(frozenset([1,2]) == F)
print(frozenset([2,1]) == F)
print (set([1,2]) == F)
print ([2,1] == F )


#5----- Dictionaries -----
print("Enter dictionaries")
##5.1  In the dictionary D, what is the value associated with the key 'b'?
print(D.get('b'))
##5.2  Pull the keys from the dictionary D and print them using the print() function.
print(D.keys())
##5.3  In the dictionary D, at what key can we find the value 'apple'?
LD = D.items()
print(LD)
#5----- For Loops -----
##6.1  The list M contains a hidden message stored as individual characters.
##     Use a for loop to print out the message. 

for char in M:
    print(char + "\n")