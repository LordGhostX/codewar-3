package main

import "fmt"

func main() {
	fmt.Println(solution([]int{1, 2, 3, 4, 5}, 3))
}

func solution(nums []int, target int) []int {
	m := make(map[int]int)
	for i, v := range nums {
		remainder := target - v
		if val, ok := m[remainder]; ok {
			return []int{m[val], i}
		} else {
			m[v] = i
		}
	}
	return nil
}
