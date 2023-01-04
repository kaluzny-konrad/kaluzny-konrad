package kata

func ReverseWords(str string) (result string) {
	toReverse := ""
	for i := 0; i < len(str); i++ {
		char := string(str[i])
		if char == " " {
			result += reverse(toReverse)
			toReverse = ""
			result += char
		} else {
			toReverse += char
		}
	}
	result += reverse(toReverse)
	return
}

func reverse(str string) (result string) {
	for _, v := range str {
		result = string(v) + result
	}
	return
}
