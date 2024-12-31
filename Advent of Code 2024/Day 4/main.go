package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Coordinate struct {
	x int
	y int
}

type Position struct {
	start Coordinate
	end   Coordinate
}

type Possibilities struct {
	offset [4]Coordinate
}

var possibilities = [8]Possibilities{
	{offset: [4]Coordinate{{0, 0}, {0, 1}, {0, 2}, {0, 3}}},
	{offset: [4]Coordinate{{0, 0}, {0, -1}, {0, -2}, {0, -3}}},

	{offset: [4]Coordinate{{0, 0}, {1, 0}, {2, 0}, {3, 0}}},
	{offset: [4]Coordinate{{0, 0}, {-1, 0}, {-2, 0}, {-3, 0}}},

	{offset: [4]Coordinate{{0, 0}, {1, 1}, {2, 2}, {3, 3}}},       // left right diagonal down
	{offset: [4]Coordinate{{0, 0}, {-1, -1}, {-2, -2}, {-3, -3}}}, // right to left diagonal up

	{offset: [4]Coordinate{{0, 0}, {1, -1}, {2, -2}, {3, -3}}}, // right to left diagonal down
	{offset: [4]Coordinate{{0, 0}, {-1, 1}, {-2, 2}, {-3, 3}}}, // left to right diagonal up
}

func main() {
	input_data := readFile()
	fmt.Println(part1(input_data))
	fmt.Println(part2(input_data))
}

func part1(input_data []string) int {
	input_data_x := len(input_data[0])
	input_data_y := len(input_data)

	result := 0
	for i := 0; i < input_data_x; i++ {
		for j := 0; j < input_data_y; j++ {
			result += checkMatch(input_data, Coordinate{i, j}, possibilities[:])
		}
	}
	return result
}

func part2(input_data []string) int {
	input_data_x := len(input_data[0])
	input_data_y := len(input_data)

	result := 0

	possibilities := [4]string{"MMSS", "SSMM", "MSMS", "SMSM"}
	//	M	M		S	S		M	S		S	M
	//    A			  A			  A		  	  A
	//	S	S		M	M		M	S		S	M

	for i := 1; i < input_data_x-1; i++ {
		for j := 1; j < input_data_y-1; j++ {
			if string(input_data[i][j]) != "A" {
				continue
			}
			str := string(input_data[i-1][j-1]) + string(input_data[i-1][j+1]) + string(input_data[i+1][j-1]) + string(input_data[i+1][j+1])
			for _, v := range possibilities {
				if v == str {
					result += 1
				}
			}
		}
	}
	return result
}

func checkMatch(input_data []string, coord Coordinate, possibilities []Possibilities) int {
	result := 0
	for _, possibility := range possibilities {
		word := ""
		for _, offset := range possibility.offset {
			x := coord.x + offset.x
			y := coord.y + offset.y
			if x < 0 || x >= len(input_data) {
				break
			}
			if y < 0 || y >= len(input_data) {
				break
			}

			word += string(input_data[y][x])
		}

		if word == "XMAS" {
			result += 1
		}
	}
	return result
}

func readFile() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	rows := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		rows = append(rows, scanner.Text())
	}

	return rows
}
