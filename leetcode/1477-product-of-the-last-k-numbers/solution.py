class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix_product = []
        self.last_zero = -1
        

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.last_zero = len(self.nums) - 1
        if len(self.nums) == 1 or self.prefix_product[-1] == 0:
            self.prefix_product.append(num)
        else:
            self.prefix_product.append(num * self.prefix_product[-1])

        

    def getProduct(self, k: int) -> int:
        n = len(self.prefix_product)
        idx = n - k - 1
        # print(idx, self.last_zero)
        if self.last_zero != -1 and idx < self.last_zero:
            return 0
        if idx == -1 or self.prefix_product[idx] == 0:
            return self.prefix_product[-1] 
        return self.prefix_product[-1] // self.prefix_product[idx]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
