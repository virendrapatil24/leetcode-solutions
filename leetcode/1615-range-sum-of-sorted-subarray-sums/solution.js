/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
    let subSum = [];
    for (let i = 0; i < n; i ++) {
        let sum = 0;
        for (let j = i; j < n; j++) {
            sum += nums[j]
            subSum.push(sum)
        }
    }
    const mod = 10 ** 9 + 7
    subSum.sort((a, b) => a - b)
    console.log(subSum)
    return subSum.slice(left-1, right).reduce((acc, val) => acc + val, 0) % mod
};
