package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	data := readFile()
	fmt.Println(part1(data))
}

func part1(data [][]int) int {
	result := 0

	for _, row := range data {
		result += checkRow(row)
	}

	return result
}

func checkRow(row []int) int {
	sign := 0
	for i := 0; i < len(row)-1; i++ {
		diff := row[i] - row[i+1]
		if diff == 0 {
			return 0
		}

		if sign == 0 && diff > 0 {
			sign = 1
		}
		if sign == 0 && diff < 0 {
			sign = -1
		}

		if diff > 0 && sign == -1 {
			return 0
		}
		if diff < 0 && sign == 1 {
			return 0
		}

		if diff > 3 || diff < -3 {
			return 0

		}
	}
	fmt.Println(row)
	return 1
}

func readFile() [][]int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	var data [][]int
	for scanner.Scan() {
		line := scanner.Text()
		line_data := strings.Split(line, " ")
		var line_arr []int
		for num := range len(line_data) {
			line_arr = append(line_arr, castToInt(line_data[num]))
		}
		data = append(data, line_arr)
	}

	return data
}

func castToInt(s string) (i int) {
	res, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}

	return res
}
