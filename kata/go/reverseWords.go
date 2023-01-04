package kata

import "strings"

func ReverseWords(str string) string {
	words := strings.Split(str, " ")
	for i, v := range words {
		words[i] = reverse(string(v))
	}

	return strings.Join(words, " ")
}

func reverse(str string) (result string) {
	for _, v := range str {
		result = string(v) + result
	}
	return
}
