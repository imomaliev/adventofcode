package main

import (
	"bufio"
	"fmt"
	"strings"
	"testing"
)

var INPUT_S string = `
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
`

var tests = []struct {
	input    string
	expected int
}{
	{INPUT_S, 4},
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
