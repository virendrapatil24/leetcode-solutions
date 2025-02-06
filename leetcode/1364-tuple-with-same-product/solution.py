class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_map[product] = product_map.get(product, 0) + 1

        tuples = 0
        for k, v in product_map.items():
            if v > 1:
                tuples += (8 * v * (v - 1) // 2)
        return tuples

'''
# Intuition
Make a count of unique pairs with same product. Every 2 pairs of same product will have 8 combinations (just to make sure pairs are unique). Lastly get how many combinations of 2 can be made with the pairs having same product and multiply it by 8.

# Approach
1. Create a map to store the count of pairs with same product.
2. Run the nested loops and make sure you generate unique pairs. 
   i.e. first loop --> 0 to n ...where n is length of nums
   second loop --> i + 1 to n ...where i is the index of first loop
3. For every key, value in product map check for values with greater than 1. 
4. If value is more than 1, get the total combinations of 2 formed from value.
i.e. if value = 3 --> (a, b) (a, c) (b, c)
if value = 4 --> (a, b) (a, c) (a, d) (b, c) (b, d) (c, d)
in simple terms v * (v - 1) // 2
5. Now multiply these no. of combinations with 8. As 2 pairs will make 8 combinations in total.

# Complexity
- Time complexity: O(n**2)

- Space complexity: O(n)

# Code
```python3 []
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_map[product] = product_map.get(product, 0) + 1

        tuples = 0
        for k, v in product_map.items():
            if v > 1:
                tuples += (8 * v * (v - 1) // 2)
        return tuples

```
'''

