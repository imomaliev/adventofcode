package main

import (
	"bufio"
	"fmt"
	"strings"
	"testing"
)

var INPUT_S string = `
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
`

var tests = []struct {
	input    string
	expected int
}{
	{INPUT_S, 281},
}

// TestHelloName calls greetings.Hello with a name, checking
// for a valid return value.
func TestSolve(t *testing.T) {
	for i, tc := range tests {
		t.Run(fmt.Sprintf("Solve=%d", i), func(t *testing.T) {
			scanner := bufio.NewScanner(strings.NewReader(strings.Trim(tc.input, "\n")))
			got := Solve(scanner)
			if got != tc.expected {
				t.Fatalf("got %v; expected %v", got, tc.expected)
			} else {
				t.Logf("Success !")
			}

		})
	}
}
