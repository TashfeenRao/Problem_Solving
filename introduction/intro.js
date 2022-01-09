// Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
// Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
// Output: [2.2, 2.8, 2.4, 3.6, 2.8]

const arr = [1, 3, 2, 6, -1, 4, 1, 8, 2];
const k = 5;
const result = [];

for (let i = 0; i < arr.length; i++) {
  let sum = 0;
  for (let j = i; j < k; j++) {
    sum += arr[j];
  }
  arr.push(sum / k);
}

console.log(result);
