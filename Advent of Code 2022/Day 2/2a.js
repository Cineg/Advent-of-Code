const fs = require("fs");

const input = fs
	.readFileSync("Advent of Code 2022/Day 2/input.txt", "utf-8")
	.split("\r\n");

const wins = {
	"Rock Paper": 0,
	"Paper Scissors": 0,
	"Scissors Rock": 0,
};

const figures = {
	A: "Rock",
	B: "Paper",
	C: "Scissors",
	X: "Rock",
	Y: "Paper",
	Z: "Scissors",
};

const figure_point = {
	Rock: 1,
	Paper: 2,
	Scissors: 3,
};

let total_points = 0;

input.forEach((item) => {
	f1 = item.split(" ")[0];
	f2 = item.split(" ")[1];

	f1 = figures[f1];
	f2 = figures[f2];

	total_points += figure_point[f2];

	if (`${f1} ${f2}` in wins) {
		total_points += 6;
	} else if (f1 === f2) {
		total_points += 3;
	}
});

console.log(total_points);
