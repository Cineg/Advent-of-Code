const fs = require("fs");

const input = fs
	.readFileSync("Advent of Code 2022/Day 3/input.txt", "utf-8")
	.split("\r\n");

result = 0;
const a_letter = "a".charCodeAt(0);
const A_letter = "A".charCodeAt(0);

input.forEach((item) => {
	half = Math.round(item.length / 2);

	let dct = {};
	let seen = {};

	for (let index = 0; index < half; index++) {
		const letter = item[index];
		dct[letter] = "";
	}

	for (let index = half; index < item.length; index++) {
		const letter = item[index];
		if (letter in dct && !seen.hasOwnProperty(letter)) {
			char = letter.charCodeAt(0);
			if (a_letter <= char && char <= a_letter + 26) {
				result += char - a_letter + 1;
			} else {
				result += char - A_letter + 1 + 26;
			}

			seen[letter] = "";
		}
	}
});

console.log(result);
