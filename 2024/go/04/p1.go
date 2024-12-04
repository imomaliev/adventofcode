package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"slices"
)


func Solve(scanner *bufio.Scanner) int {
	var matrix [][]byte
	var err error
	var result = 0
	var vertical, diagonal, rdiagonal string
	re := regexp.MustCompile(`(XMAS|SAMX)`)
	var rowLength = 0
	for scanner.Scan() {
		row := scanner.Text()
		rowLength = len(row)
		matrix = append(matrix, []byte(row))
		result += len(re.FindAll([]byte(row), -1))
	}
	var colHeight = len(matrix)
	// count vertical
	for i:=0; i<rowLength; i++ {
		vertical = ""
		for j:=0; j<colHeight; j++ {
			vertical += string(matrix[j][i])
		}
		result += len(re.FindAll([]byte(vertical), -1))
	}

	// count diagonal
	var visited [][2]int
	x:=0
	y:=0
	cursor:=0
	for cursor < colHeight {
		diagonal = ""
		for x < colHeight && y < rowLength {
			if !slices.Contains(visited, [2]int{x, y}) {
				diagonal += string(matrix[x][y])
				visited = append(visited, [2]int{x, y})
			}
			x++
			y++
		}
		result += len(re.FindAll([]byte(diagonal), -1))
		cursor++
		x=cursor
		y=0
	}
	x=0
	y=0
	cursor=0
	for cursor < rowLength {
		diagonal = ""
		for x < colHeight && y < rowLength {
			if !slices.Contains(visited, [2]int{x, y}) {
				diagonal += string(matrix[x][y])
				visited = append(visited, [2]int{x, y})
			}
			x++
			y++
		}
		result += len(re.FindAll([]byte(diagonal), -1))
		cursor++
		y=cursor
		x=0
	}

	// count rdiagonal
	var rvisited [][2]int
	x=0
	y=rowLength - 1
	cursor=0
	for cursor < colHeight {
		rdiagonal = ""
		for x < colHeight && y >= 0 {
			if !slices.Contains(rvisited, [2]int{x, y}) {
				rdiagonal += string(matrix[x][y])
				rvisited = append(rvisited, [2]int{x, y})
			}
			x++
			y--
		}
		result += len(re.FindAll([]byte(rdiagonal), -1))
		cursor++
		x=cursor
		y=rowLength - 1
	}
	x=0
	y=rowLength - 1
	cursor=0
	for cursor < rowLength {
		rdiagonal = ""
		for x < colHeight && y >= 0 {
			if !slices.Contains(rvisited, [2]int{x, y}) {
				rdiagonal += string(matrix[x][y])
				rvisited = append(rvisited, [2]int{x, y})
			}
			x++
			y--
		}
		result += len(re.FindAll([]byte(rdiagonal), -1))
		cursor++
		y=rowLength - cursor
		x=0
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Scanner error: %v", err)
	}

	return result
}

func main() {
	log.SetPrefix("day00:part1: ")
	file, err := os.Open("../../input/00.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Print(Solve(scanner))
}
