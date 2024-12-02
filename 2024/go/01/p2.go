package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func Solve(scanner *bufio.Scanner) int {
	var input []int
	var err error
	for scanner.Scan() {
		value, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		input = append(input, value)
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
}

func main() {
	log.SetPrefix("day00:part2: ")
	file, err := os.Open("../../input/00.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
