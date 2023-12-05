package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
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
	for _, item := range input {
		first := -1
		var last int
		for _, c := range item {
			if v, err := strconv.Atoi(string(c)); err == nil {
				if first == -1 {
					first = v
				}
				last = v
			}
		}
		res = res + first*10 + last

	}
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
