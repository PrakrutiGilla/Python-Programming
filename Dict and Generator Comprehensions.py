#Dictionary Comprehension

"""syntax: output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}"""

#Eg 1: output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values.

'''input_list = [1,2,3,4,5,6,7] 
  
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0} 
  
print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

O/P: Output Dictionary using dictionary comprehensions: {1: 1, 3: 27, 5: 125, 7: 343}'''

#Eg 2
'''state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 
  
print({key:value for (key, value) in zip(state, capital)})

O/P: {'Gujarat': 'Gandhinagar', 'Maharashtra': 'Mumbai', 'Rajasthan': 'Jaipur'} '''

#Generator Comprehension

#Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator comprehensions
#use circular brackets.The major difference between them is that generators don’t allocate memory for the whole list.
#Instead, they generate each value one by one which is why they are memory efficient. 

"""input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7] 
  
output_gen = (var for var in input_list if var % 2 == 0) 
  
print("Output values using generator comprehensions:", end = ' ') 
  
for var in output_gen: 
    print(var, end = ' ')

    
Output:

Output values using generator comprehensions: 2 4 4 6 """
