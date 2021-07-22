# Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

### Example 1:

![image](./images/rainwatertrap.png)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

### Example 2:

Input: height = [4,2,0,3,2,5]

Output: 9
 

### Constraints:

n == height.length

0 <= n <= 3 * 104

0 <= height[i] <= 105

### Strategy
the water a block can hold on it is the difference between its height and 

(**the value** :=min(max(heights to the left), max(heights to the right))).

We can use 2 pointer tech. to keep track of each side's max height to compute **the value** .

Implementation:
1. left pointer starts at index 0, right pointer starts at len(height) - 1;
2. do operation on the smaller side till left index == right index == argmax(height):
    1. if the current height is greater than the side max height, update the side max height
    2. else, calculate water on its top and add to the total water amount
    3. move pointer inward

### Time complex.
O(n)
