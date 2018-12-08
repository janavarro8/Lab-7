"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Lab 7
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 12/7/18
Purpose: Implement Edit Distance Algorithm
"""

def main():
    str1 = "miners"
    str2 = "money"
    
    print('\nFirst word is "', str1, '"')    
    print('Second word is "', str2, '"')
    
    editList = edit_distance(str1, str2)
    
    print("\nThe edit distance for the two words is: ", editList[len(str2)][len(str1)])
    
    print("\nThe full edit distance list:\n")
    
    print_list(editList, str1, str2)
    
#Creates the edit distance list
def edit_distance(str1, str2):
    str1 = " " + str1 #add space to evaluate no string
    str2 = " " + str2 
    len1 = len(str1) #holds length of the words
    len2 = len(str2)
    
    editList = [[0]*len1 for i in range(len2)] #creates list of appropriate size
    
    for i in range(len1):
        editList[0][i] = i #fills 0 - length1 in array at [0]
    for i in range(len2):
        editList[i][0] = i #fills 0 - length2 in array at [][0]
        
    for i in range(1, len2):
        for j in range(1, len1):
            if(str1[j] == str2[i]): #if letters at i are equal
                editList[i][j] = editList[i - 1][j - 1] #sets index to diagonal left index
            else:
                #sets index to the minimum of surrounding indexes
                editList[i][j] = min(editList[i - 1][j], editList[i - 1][j - 1], editList[i][j - 1]) + 1
    
    return editList

#prints the edit distance list with 
#the words on their appropriate lines
def print_list(editList, str1, str2):
    str1 = '"' + str1
    str2 = '"' + str2
    
    print("   ", end='') #helps line up str1 to list
    for i in range(len(str1)): #prints str1
        print(str1[i], " ", end='')
    print()
    
    for i in range(len(str2)):
        print(str2[i], " ", end='') #prints str2
        for j in range(len(str1)):
            print(editList[i][j], " ", end='') #prints each index in list
        print() 
    
main()