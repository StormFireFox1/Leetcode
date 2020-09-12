package main

import "strings"
import "fmt"

var solutionSet []string

func backtrack(n int, current string) {
    numberOpen := strings.Count(current, "(");
    numberClosed := strings.Count(current, ")");
    if numberClosed == n {
        solutionSet = append(solutionSet, current);
    } else {
        if numberOpen > numberClosed {
            backtrack(n, current + ")");
        }
        if numberOpen < n {
            backtrack(n, current + "(");
        }
    }
}

func generateParenthesis(n int) []string {
    backtrack(n, "");
    defer func(){solutionSet = nil}();
    return solutionSet;
}

func main() {
  fmt.Println(generateParenthesis(3));
}
