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
	var err error
	scanner.Scan()
	value := scanner.Text()
	seeds := strings.Split(strings.TrimSpace(strings.Split(value, ":")[1]), " ")
	scanner.Scan()

	pipeline := map[int][]string{}
	pipeline_map := map[int]map[int]int{}
	pindex := -1
	fmt.Print(seeds)

	for scanner.Scan() {
		value := scanner.Text()
		if value == "" {
			continue
		}
		if strings.Contains(value, ":") {
			pindex += 1
			if pindex == 2 {
				break
			}
			pipeline_map[pindex] = make(map[int]int)
			continue
		}
		pipeline[pindex] = append(pipeline[pindex], value)

		values := strings.Split(value, " ")
		source, _ := strconv.Atoi(values[0])
		dest, _ := strconv.Atoi(values[1])
		offset, _ := strconv.Atoi(values[2])
		for i := 0; i < offset; i++ {
			pipeline_map[pindex][source+i] = dest + i
			break
		}
	}

	fmt.Println(pipeline_map[0])
	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}
	return 0
}

func main() {
	log.SetPrefix("day05:part1: ")
	file, err := os.Open("../../input/day05.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
