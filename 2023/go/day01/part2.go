package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Solve(scanner *bufio.Scanner) int {
	var input []string
	var err error
	for scanner.Scan() {
		value := scanner.Text()
		if err != nil {
			log.Fatal(err)
		}
		input = append(input, value)
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}

	var res = 0
	digits := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	// for _, item := range input {
	// 	first := -1
	// 	var last int
	//
	// 	i := 0
	// 	while i < len(item) {
	// 		c := item[i]
	// 		tree = item[i:i+3]
	// 		four
	// 		five
	// 	}
	//
	// 	for i := len(item) {
	// 		if v, err := strconv.Atoi(string(c)); err == nil {
	// 			if first == -1 {
	// 				first = v
	// 			}
	// 			last = v
	// 		}
	// 	}
	// 	fmt.Printf("%s\n", item)
	// 	fmt.Printf("%d %d\n", first, last)
	// 	res = res + first*10 + last
	// 	fmt.Printf("%d\n", res)
	//
	// }
	return res
}

func main() {
	log.SetPrefix("day01:part1: ")
	file, err := os.Open("../../input/day01.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
