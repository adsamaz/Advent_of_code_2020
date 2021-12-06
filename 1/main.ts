const file = await Deno.readTextFile("./1/input.txt");

const arr = file
  .split("\n")
  .map((elem) => elem.replace("\r", ""))
  .map((elem) => parseInt(elem, 10));

const findIncreasing = (arr: number[]) => {
  const arrClone = [...arr];
  return arrClone
    .splice(1)
    .reduce((acc, curr, i) => (curr > arr[i] ? acc + 1 : acc), 0);
};

// # Only need to compare at the first number of the window and the last number of the new window.
// # The two numbers in the middle are shared by both windows
const findIncreasingThree = (arr: number[]) => {
  const arrClone = [...arr];
  return arrClone
    .splice(3)
    .reduce((acc, curr, i) => (curr > arr[i] ? acc + 1 : acc), 0);
};

console.log(findIncreasing(arr));
console.log(findIncreasingThree(arr));
