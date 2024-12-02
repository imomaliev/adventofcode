package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func AbsInt(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func Solve(scanner *bufio.Scanner) int {
	var err error
	var result = 0

	for scanner.Scan() {
		values := strings.Split(scanner.Text(), " ")
		prev, err := strconv.Atoi(values[0])
		if err != nil {
			log.Fatal(err)
		}
		curr, err := strconv.Atoi(values[1])
		if err != nil {
			log.Fatal(err)
		}

		incr := curr > prev

		diff := AbsInt(curr - prev)
		if diff < 1 || diff > 3 {
			continue
		}

		prev = curr
		nobreak := true
		for _, val := range values[2:] {
			curr, err := strconv.Atoi(val)
			if err != nil {
				log.Fatal(err)
			}

			diff = AbsInt(curr - prev)
			if curr > prev != incr {
				nobreak = false
				break
			}
			if diff < 1 || diff > 3 {
				nobreak = false
				break
			}
			prev = curr
		}
		if nobreak {
			result += 1
		}
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return result
}

func main() {
	log.SetPrefix("day00:part1: ")
	file, err := os.Open("../../input/02.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
