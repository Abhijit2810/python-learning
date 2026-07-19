# Learning Lists
1. A list is a built-in mutable data structure that stores an ordered collection of items. It is represented by [].<br>
2. Accessing elements in lists is done with indexing. Indexing starts with 0 not 1.<br>
3. To access last element we can use index -1, second last -2 and so on, this indexing acts based on a formula indexing = length of list + negative index.

# Learning Functions
## General Functions
1. Append function is used to insert objects in list, but at the last, while insert function has 2 inputs, first is index and second is the element to be inserted. If we keep index greater or equal to last index, it adds element to last but no error, not considered good practice.<br>
2. del keyword deletes the list element when index is given of that element like del names[0].<br>
3. pop() is used to remove last element of the list, it is important to know that pop does remove the last element but it can also store that when assigned a variable to it. If we a provide index inside pop() then that particular index will be removed, index cant be greater than last index, in that case we again get index error.<br>
4. Remove function is used to remove an element directly if we dont know that index, if the element is not in list, it throws value error saying that its not in the list.<br>
5. reverse() function reverses the order of the list.<br>
6. len() function gives the number of elements in the list.

## Sorting functions
1. Sort function arranges the function alphabetically or numerically, while sorting we cant have multiple Data type elements in list.<br>
2. We can do reverse sorting by keeping reverse=True inside sort function parameter.<br>
3. When sorting is applied, the changes are permanent.<br>
4. sorted() is used for producing sorted lists, while no changes are made to original list, it can also reverse the order of sorting.

# Learning Errors
1. Index Error: This error comes in lists when we entered an index which is out of range for a list, like for a list of 5 elements, any index greater than or equal to 5 is out of range.<br>
2. Value Error: This error comes when a particular element is not in a list when used remove function.
