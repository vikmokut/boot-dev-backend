package main

import (
	"fmt"
	// "math"
)

func printPrimes(max int) {
	min := 2
	i := 3
	for min <= max {
		if min == 2 {
			fmt.Println(min)
			min++
			continue
		} else if min%2 == 0 {
			min++
			continue
		}
		for i*i < min {
			if min%i == 0 {
				continue
			}
			i += 2
		}
		fmt.Println(min)
		// increment before reiteration
		min++
	}
}

// don't edit below this line

func test(max int) {
	fmt.Printf("Primes up to %v:\n", max)
	printPrimes(max)
	fmt.Println("===============================================================")
}

func main() {
	test(10)
	test(20)
	test(30)
}
