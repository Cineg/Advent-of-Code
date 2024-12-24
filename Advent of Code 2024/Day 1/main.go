package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

var input string

func main() {
	l1, l2 := readFile()
	fmt.Println(part1(l1, l2))
	fmt.Println(part2(l1, l2))
}

func part1(l1, l2 []int) int {
	slices.Sort(l1)
	slices.Sort(l2)

	ans := 0
	for i := range len(l1) {
		diff := l2[i] - l1[i]
		if diff < 0 {
			diff = -diff
		}
		ans += diff
	}
	return ans
}

func part2(l1, l2 []int) int {
	map1 := make(map[int]int)
	map2 := make(map[int]int)

	for i := range len(l1) {
		map1[l1[i]] += 1
		map2[l2[i]] += 1
	}

	ans := 0
	for key, value := range map1 {
		multiplier := map2[key]

		fmt.Println(multiplier)

		ans += multiplier * key * value
	}

	return ans
}

func readFile() (list1, list2 []int) {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, "   ")

		list1 = append(list1, castToInt(split[0]))
		list2 = append(list2, castToInt(split[1]))
	}

	return list1, list2
}

func castToInt(s string) (i int) {
	res, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}

	return res
}
