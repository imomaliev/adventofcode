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

func Solve(scanner *bufio.Scanner) int {
	var err error
	var rules = make(map[int][]int)
	rulesScanned := false
	var updates [][]int
	result := 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			rulesScanned = true
			continue
		}

		if !rulesScanned {
			values := strings.Split(line, "|")
			key, err := strconv.Atoi(values[0])
			if err != nil {
				log.Fatal(err)
			}
			val, err := strconv.Atoi(values[1])
			if err != nil {
				log.Fatal(err)
			}
			rules[key] = append(rules[key], val)
		} else {
			values := strings.Split(line, ",")
			var update []int
			for _, val := range values {
				page, err := strconv.Atoi(val)
				if err != nil {
					log.Fatal(err)
				}
				update = append(update, page)
			}
			updates = append(updates, update)
		}

	}

	for _, update := range updates {
		correct := true
		for i, page := range update {
			for j := 0; j < len(update); j++ {
				if j < i && !slices.Contains(rules[update[j]], page) {
					correct = false
					break
				}
				if j > i && !slices.Contains(rules[page], update[j]) {
					correct = false
					break
				}
			}
		}
		if correct {
			result += update[len(update)/2]
		}
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return result
}

func main() {
	log.SetPrefix("day00:part1: ")
	file, err := os.Open("../../input/05.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
