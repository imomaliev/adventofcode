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
	var left []int
	var right = make(map[int]int)
	var err error
	for scanner.Scan() {
		values := strings.Split(scanner.Text(), "   ")
		lvalue, err := strconv.Atoi(values[0])
		if err != nil {
			log.Fatal(err)
		}
		left = append(left, lvalue)

		rvalue, err := strconv.Atoi(values[1])
		if err != nil {
			log.Fatal(err)
		}
		if _, ok := right[rvalue]; ok {
			right[rvalue] += 1
		} else {
			right[rvalue] = 1
		}

	}

	var result = 0
	for _, val := range left {
		if rval, ok := right[val]; ok {
			result += val * rval
		}
	}
	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return result
}

func main() {
	log.SetPrefix("day01:part2: ")
	file, err := os.Open("../../input/01.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
