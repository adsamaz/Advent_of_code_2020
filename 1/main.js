var fs = require("fs");

// const file = fr.readAsText("input.txt");
// const text = fr.result;

fs.readFile("1/input.txt", "utf8", function (err, data) {
  //   console.log(data);

  const nums = [];
  let elf = 0;
  data.split("\n").forEach(function (line) {
    const num = line.replace("\r", "");
    if (num) nums[elf] = (nums[elf] ?? 0) + parseInt(num);
    else elf += 1;
  });

  console.log(nums);
  console.log(Math.max(...nums));

  console.log(
    nums
      .sort()
      .slice(nums.length - 3)
      .reduce((prev, next) => prev + next)
  );
});
