package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func Matcher(m [3][3]byte) int {
	if m[1][1] != byte('A') {
		return 0
	}
	if m[0][0] == byte('M') && m[0][2] == byte('M') && m[2][0] == byte('S') && m[2][2] == byte('S') {
		return 1
	}
	if m[0][0] == byte('M') && m[0][2] == byte('S') && m[2][0] == byte('M') && m[2][2] == byte('S') {
		return 1
	}
	if m[0][0] == byte('S') && m[0][2] == byte('S') && m[2][0] == byte('M') && m[2][2] == byte('M') {
		return 1
	}
	if m[0][0] == byte('S') && m[0][2] == byte('M') && m[2][0] == byte('S') && m[2][2] == byte('M') {
		return 1
	}
	return 0
}

func Solve(scanner *bufio.Scanner) int {
	var matrix [][]byte
	var err error
	var result = 0
	var rowLength = 0

	for scanner.Scan() {
		row := scanner.Text()
		rowLength = len(row)
		matrix = append(matrix, []byte(row))
	}
	var colHeight = len(matrix)

	for i := 0; i < colHeight; i++ {
		for j := 0; j < rowLength; j++ {
			if i+3 <= colHeight && j+3 <= rowLength {
				var window [3][3]byte
				for wi := 0; wi < 3; wi++ {
					for wj := 0; wj < 3; wj++ {
						window[wi][wj] = matrix[i+wi][j+wj]
					}
				}
				result += Matcher(window)
			}
		}
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}

	return result
}

func main() {
	log.SetPrefix("day00:part2: ")
	file, err := os.Open("../../input/04.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
