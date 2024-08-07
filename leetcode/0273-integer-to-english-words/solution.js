/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function (num) {
    if (num === 0) return "Zero"
    const ones = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    ];
    const tens = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ];
    const teens = [
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ];
    const suffixes = [
        "",
        "Thousand",
        "Million",
        "Billion",
        "Trillion",
        "Quadrillion",
        "Quintillion",
        "Sextillion",
        "Septillion",
        "Octillion",
        "Nonillion",
        "Decillion",
    ];
    let words = [];
    let i = 0;
    while (num > 0) {
        let triplet = num % 1000;
        num = Math.floor(num / 1000);
        if (triplet === 0) {
            i ++;
            continue;
        }
        let temp = [];
        if (Math.floor(triplet / 100) > 0) {
            temp.push(ones[Math.floor(triplet / 100)]);
            temp.push("Hundred");
        }
        if (triplet % 100 >= 10 && triplet % 100 <= 19) {
            temp.push(teens[triplet % 10]);
        }
        else {
            if (triplet % 100 >= 20) {
                temp.push(tens[Math.floor(triplet % 100 / 10)]);
            }
            if (triplet % 10 > 0) {
                temp.push(ones[triplet % 10]);
            }
        }
        if (i > 0) {
            temp.push(suffixes[i]);
        }
        words = [...temp, ...words];
        i++;
    }
    return words.join(" ");
};
