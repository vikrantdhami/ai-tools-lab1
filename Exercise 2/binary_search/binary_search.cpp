/**
 * Binary Search in C++
 * Key Language Nuance: Direct memory access, STL vectors passed by const reference
 * to eliminate copy overhead.
 */
#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> nums = {1, 3, 5, 7, 9, 11, 13};
    int target = 7;
    int result = binarySearch(nums, target);
    std::cout << "C++: Target " << target << " found at index: " << result << std::endl;
    return 0;
}