package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var regex_for_part_1 *regexp.Regexp = regexp.MustCompile(`(?m)mul\(\d{1,3},\d{1,3}\)`)

func main() {
	input_string := readFile()
	fmt.Println(part1(input_string))
}

func part1(input_string string) int {
	var result int = 0
	data := regex_for_part_1.FindAllString(input_string, -1)
	for _, v := range data {
		split := strings.Split(v, "(")
		split = strings.Split(split[1], ")")
		split = strings.Split(split[0], ",")
		result += (castToInt(split[0]) * castToInt(split[1]))
	}

	return result
}

func readFile() string {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	return_str := ""
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		return_str += scanner.Text()
	}

	return return_str
}

func castToInt(s string) int {
	res, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}

	return res
}
