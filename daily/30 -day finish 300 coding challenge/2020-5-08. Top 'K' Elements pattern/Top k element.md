# K element

* The questions about find the top/smallest frequent 'k' elements
*  This typical question is for stream data calculation

### usually the question tag will be like this: 
`find median`, `find the top K`, `find the N largest label`


### the data structure we will use is heap

* time complexity o(logN)
* space complexity o(N)

### the build-in method 

* heapq.heappush 
* heapq.heappop  --> pop the smallest
* heapq.heappushpop --> useful for the maintanence of a heap fixed length
* heapq.heapify o(N)
* heapq.heaprepalce
* heapq.merge  --> merge inputs into a single sorted output  --> return iterator
* heapq.nlargest(k, nums) --> return list
* heapq.nsmallest(k, nums) --> return list

### tips
* minheap the smallest one is alway at first !!  -- > search o(1)
* maxheap we need push into the negative maximum val and pop out the max value

### why we need to use heap?
* heap search o(logn) --> minheap or maxheap can be o(1) in some cases
* heap insert and pop o(logn)
* In the contrary, for sort algorithm normally will use o(nlogn).