const fs = require("fs");

const input = fs.readFileSync("Advent of Code 2022/Day 1/input.txt", "utf-8");
const arr = input.split("\r\n\r\n");

let max_cal = [0, 0, 0];
let total = 0;
for (let item = 0; item < arr.length; item++) {
	const element = arr[item].split("\r\n");

	let sum = 0;
	for (let cal = 0; cal < element.length; cal++) {
		let val = parseInt(element[cal]);
		sum += val;
	}

	for (let cal = 0; cal < max_cal.length; cal++) {
		let val = max_cal[cal];
		if (sum > val) {
			max_cal[cal] = sum;
			max_cal.sort();
			break;
		}
	}
}

max_cal.forEach((num) => (total += num));
console.log(total);
