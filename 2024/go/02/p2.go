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

func getDirection(b bool) int {
	if b {
		return 1
	}
	return -1
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

		direction := getDirection(curr > prev)
		total := len(values)

		diff := AbsInt(curr - prev)
		if diff < 1 || diff > 3 {
			continue
		}

		prev = curr
		nobreak := true
		fmt.Println(direction)
		for _, val := range values[2:] {
			curr, err := strconv.Atoi(val)
			if err != nil {
				log.Fatal(err)
			}

			direction += getDirection(curr > prev)
			fmt.Println(direction)
			diff = AbsInt(curr - prev)
			if diff < 1 || diff > 3 {
				nobreak = false
				break
			}
			prev = curr
		}
		absDirection := AbsInt(direction)
		fmt.Println(values)
		fmt.Println(nobreak, direction, absDirection)
		if nobreak && absDirection >= total-3 {
			fmt.Println("safe")
			result += 1
		}
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return result
}

func main() {
	log.SetPrefix("day00:part2: ")
	file, err := os.Open("../../input/02.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
