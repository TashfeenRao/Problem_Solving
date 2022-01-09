// Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
// Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
// Output: [2.2, 2.8, 2.4, 3.6, 2.8]

const arr1 = [1, 3, 2, 6, -1, 4, 1, 8, 2];
const k = 5;
const result = [];

// brute force solution
for (let i = 0; i < arr1.length; i++) {
  let sum = 0;
  for (let j = i; j < k + i; j++) {
    sum += arr1[j];
  }
  if (sum) result.push(sum / k);
}

// sliding window solution
//
let windowStart = 0,
  sum = 0;
for (let windowEnd = 0; windowEnd < arr1.length; windowEnd++) {
  sum += arr1[windowEnd];

  if (windowEnd >= k - 1) {
    result.push(sum / k);
    sum -= arr1[windowStart];
    windowStart += 1;
  }
}

console.log(result);
