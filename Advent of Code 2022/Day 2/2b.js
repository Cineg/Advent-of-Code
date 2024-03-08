const fs = require("fs");

const input = fs
	.readFileSync("Advent of Code 2022/Day 2/input.txt", "utf-8")
	.split("\r\n");

const wins = {
	Rock: "Paper",
	Paper: "Scissors",
	Scissors: "Rock",
};

const lose = {
	Rock: "Scissors",
	Paper: "Rock",
	Scissors: "Paper",
};

const figures = {
	A: "Rock",
	B: "Paper",
	C: "Scissors",
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

	f2 == "X"
		? (total_points += figure_point[lose[f1]])
		: f2 == "Y"
		? (total_points += 3 + figure_point[f1])
		: (total_points += 6 + figure_point[wins[f1]]);
});

console.log(total_points);
