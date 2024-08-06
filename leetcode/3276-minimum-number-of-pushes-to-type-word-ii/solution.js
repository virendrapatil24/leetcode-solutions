/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    let hashMap = new Map();
    for (let char of word) {
        hashMap.set(char, (hashMap.get(char) || 0) + 1);
    }
    
    const freqHeap = Array.from(hashMap.values());
    freqHeap.sort((a, b) => b - a);

    let totalPresses = 0;
    let keyPosition = 0;

    while (freqHeap.length > 0) {
        totalPresses += Math.floor(keyPosition / 8 + 1) * freqHeap.shift();
        keyPosition++;
    }

    return totalPresses
};
