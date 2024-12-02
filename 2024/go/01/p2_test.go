package main

import (
	"bufio"
	"fmt"
	"strings"
	"testing"
)

var INPUT_S string = `
<<<<<<< HEAD
3   4
4   3
2   5
1   3
3   9
3   3
=======
>>>>>>> 062e609 (2024: day1 part1)
`

var tests = []struct {
	input    string
	expected int
}{
<<<<<<< HEAD
	{INPUT_S, 31},
=======
	{INPUT_S, ...},
>>>>>>> 062e609 (2024: day1 part1)
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
