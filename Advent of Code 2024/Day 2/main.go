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
	fmt.Println(part2(data))
}

func part1(data [][]int) int {
	result := 0

	for _, row := range data {
		sign := checkSign(row)
		result += checkRow(row, sign)
	}

	return result
}

func part2(data [][]int) int {
	result := 0
	for _, row := range data {
		sign := checkSign(row)
		if sign == 0 {
			continue
		}

		res := 0

		if checkRow(row, sign) == 1 {
			result += 1
			continue
		}

		for i := range len(row) {
			new_row := sliceArr(i, row)
			if checkRow(new_row, sign) == 1 {
				fmt.Println(new_row)
				res = 1
				break
			}
		}
		result += res
	}

	return result
}

func sliceArr(idx int, data []int) []int {
	temp := make([]int, len(data))
	copy(temp, data)

	if idx == len(data)-1 {
		temp = temp[:idx]
	} else {
		temp = append(temp[:idx], temp[idx+1:]...)
	}
	return temp
}

func checkRow(row []int, sign int) int {
	for i := 0; i < len(row)-1; i++ {
		res := testChars(row[i], row[i+1], sign)
		if res == 0 {
			return 0
		}
	}
	return 1
}

func testChars(char1, char2, sign int) int {
	diff := char1 - char2
	if diff == 0 {
		return 0
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

	return 1
}

func checkSign(row []int) int {
	diff := row[0] - row[len(row)-1]
	if diff > 0 {
		return 1
	}
	if diff < 0 {
		return -1
	}
	return 0
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
