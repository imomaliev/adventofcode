package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const allowed = "1234567890"

func Search(i int, line string) (int, int, error) {
	x := ""
	val := string(line[i])
	for strings.Contains(allowed, val) {
		x = x + val
		i++
		val = string(line[i])
	}
	if val != "," {
		return i, 0, errors.New(", not found")
	}
	i++
	y := ""
	val = string(line[i])
	for strings.Contains(allowed, val) {
		y = y + val
		i++
		val = string(line[i])
	}
	if val != ")" {
		return i, 0, errors.New(") not found")
	}

	intx, err := strconv.Atoi(x)
	if err != nil {
		log.Fatal(err)
	}
	inty, err := strconv.Atoi(y)
	if err != nil {
		log.Fatal(err)
	}
	return i, intx * inty, nil

}

func Solve(scanner *bufio.Scanner) int {
	var err error
	var result = 0
	var apply = true
	for scanner.Scan() {
		line := scanner.Text()
		var i = 4
		for i < (len(line)) {
			if i > 7 && line[i-7:i] == "don't()" {
				apply = false
			}
			if line[i-4:i] == "do()" {
				apply = true
			}
			if apply && line[i-4:i] == "mul(" {
				j, res, err := Search(i, line)
				if err == nil {
					result += res
				}
				i = j
			}
			i++
		}
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return result
}

func main() {
	log.SetPrefix("day00:part1: ")
	file, err := os.Open("../../input/03.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
