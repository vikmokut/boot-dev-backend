package main

import "fmt"

func fizzbuzz() {
	num := 1
	for num <= 100 {
		if num%3 == 0 && num%5 == 0 {
			fmt.Println("fizzbuzz")
		} else if num%5 == 0 {
			fmt.Println("buzz")
		} else if num%3 == 0 {
			fmt.Println("fizz")
		} else {
			fmt.Println(num)
		}
		num++
	}
}

func main() {
	fizzbuzz()
}
