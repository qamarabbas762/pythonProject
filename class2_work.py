import time

"""1) Question - Dictionary Manipulation: Write a Python function swap_keys_values that takes a dictionary as input and returns a new dictionary with keys and values swapped. Provide sample input and expected output.
Sample input = {'a': 1, 'b': 2, 'c': 3}
Sample output = {1: 'a', 2: 'b', 3: 'c'}
"""

# def dict_manu(d):
#     d1 ={}
#     for key,value in d.items():
#         d1[value] =key
#     return d1
#
#
# print(dict_manu({'a': 1, 'b': 2, 'c': 3}))


"""2)  Question - Removing Duplicates from a List: Write a Python function remove_duplicates that takes a list as input and removes duplicates while preserving the original order of elements.
sample input = [1, 2, 3, 2, 4, 3, 5]
sample output =  [1, 2, 3, 4, 5]
"""

# def remove_dup(li):
#     list1 = []
#     for i in li:
#         if i not in list1:
#             list1.append(i)
#         else:
#             pass
#     return list1
#
# print(remove_dup([1, 2, 3, 2, 4, 3, 5]))


"""Function to Merge Two Sorted Lists -> final list should be also Sorted(merge them in such a way that the final list is automatically sorted)
sample input = list1= [1,3,5,7] , list2 =[2,4,6,8]
sample output==[1,2,3,4,5,6,7,8]
"""

# def merge_list(l1,l2):
#     l3 = l1+l2
#     return sorted(l3)
#
# list1 = [1,3,5,7]
# list2 = [2,4,6,8]
# print(merge_list(list1,list2))

"""Correction for the above question """

def merge_list(l1,l2):
    i,j=0,0
    merged_list = []

    while i< len(l1) and j< len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i+=1
        else:
            merged_list.append(l2[j])
            j+=1

    merged_list.extend(l1[i:])
    merged_list.extend(l2[j:])

    return merged_list

list1 = [1,3,5,7]
list2 = [2,4,6,8]
print(merge_list(list1,list2))



"""Function to Count Vowels and Consonants
sample input= "Hello World"
sample output= {'vowels':3,'consonants':7}
"""

# def count_words(word):
#     d = {'vowels':0,'consonents':0}
#     for i in word:
#         if i in 'aeiou':
#             d['vowels'] +=1
#         elif i == ' ':
#             pass
#         else:
#             d['consonents'] +=1
#
#     return d
#
# print(count_words('Hello World'))

"""Correction for the above question"""

# def count_words(word):
#     d = {'vowels':0,'consonents':0}
#     for i in word:
#         if i in 'aeiouAEIOU':
#             d['vowels'] +=1
#         elif i == ' ' or i in '123456789':
#             pass
#         else:
#             d['consonents'] +=1
#
#     return d
#
# print(count_words('Hello World 123'))

"""Function to Find Longest Consecutive Sequence
Write a Python function longest_consecutive_sequence that finds the length of the longest consecutive elements sequence from an unsorted list of integers.
# Sample input
input_nums = [100, 4, 200, 1, 3, 2]
 # Expected output
Output=4 (Longest consecutive sequence is [1, 2, 3, 4])
"""

# def longest_consecutive_sequence(nums):
#     num_set = set(nums)
#     num_list = []
#     max_length = 0
#
#
#     for num in num_set:
#         if num-1 not in num_set:
#             current_num = num
#             current_length =1
#
#         else:
#             current_length +=1
#         if current_length > max_length:
#             max_length =current_length
#             num_list = list(range(current_num,current_num+current_length))
#
#     return num_list
#
# # Expected output
# input_nums = [100, 4, 200, 1, 3, 2]
# output = longest_consecutive_sequence(input_nums)
# print(output)  # Output: 4



# def longest_consecutive_sequence(nums):
#     num_set = set(nums)
#     num_list = []
#     max_length = 0
#
#     for num in num_set:
#         if num-1 not in num_set:
#             length = 0
#         while num+length in num_set:
#             length+=1
#         max_length = max(length,max_length)
#
#     return max_length
#
# # Expected output
#
# input_nums = [100, 4, 200, 1, 3, 2]
# start_time = time.time()
# output = longest_consecutive_sequence(input_nums)
# print(output)
#
# print(f"execution time is  {time.time()-start_time}")
