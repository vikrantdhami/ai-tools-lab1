/**
 * Binary Search in JavaScript
 * Key Language Nuance: Numbers are 64-bit double-precision floats; integer division
 * requires explicit truncation using `Math.floor()`.
 */
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);

        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

const nums = [1, 3, 5, 7, 9, 11, 13];
const target = 7;
const result = binarySearch(nums, target);
console.log(`JavaScript: Target ${target} found at index: ${result}`);