/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    let arrMap = new Map();
    for (let char of arr) {
        arrMap.set(char, (arrMap.get(char) || 0) + 1)
    }
    let count = 0
    for (let char of arr) {
        // console.log(char)
        if (arrMap.get(char) === 1) {
            // console.log(char, count)
            count++
            if (count === k) {
                return char
            }
        }
    }
    return ""
};
