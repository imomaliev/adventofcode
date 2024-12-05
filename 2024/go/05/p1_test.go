package main

import (
	"bufio"
	"fmt"
	"strings"
	"testing"
)

var INPUT_S string = `
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
`

var tests = []struct {
	input    string
	expected int
}{
	{INPUT_S, 143},
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
