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

func AbsInt(x, y int) int {
   if x < y {
      return y - x
   }
   return x - y
}

func Solve(scanner *bufio.Scanner) int {
	var left []int
	var right []int
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
		right = append(right, rvalue)
	}

	slices.Sort(left)
	slices.Sort(right)

	var result = 0
	for idx, val := range left {
		result = result + AbsInt(val, right[idx])
	}
	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return result
}

func main() {
	log.SetPrefix("day01:part1: ")
	file, err := os.Open("../../input/01.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
