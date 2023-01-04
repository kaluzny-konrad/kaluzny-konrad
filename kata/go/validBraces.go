package kata

func ValidBraces(str string) bool {
	for i := 0; i < len(str); i++ {
		openingBrace := string(str[i])
		if isClosingBrace(openingBrace) {
			break
		}

		closingBrace := getClosingBrace(i, str)
		if !isValidClosingBrace(openingBrace, closingBrace) {
			return false
		}
	}

	return true
}

func getClosingBrace(i int, str string) string {
	toSkip := 0
	for j := i + 1; j < len(str); j++ {
		brace := string(str[j])
		if isClosingBrace(brace) {
			return string(str[j+toSkip])
		} else {
			toSkip++
		}
	}
	return ""
}

func isOpeningBrace(brace string) bool {
	return brace == "(" || brace == "[" || brace == "{"
}

func isClosingBrace(brace string) bool {
	return brace == ")" || brace == "]" || brace == "}"
}

func isValidClosingBrace(openingBrace string, closingBrace string) bool {
	if openingBrace == "(" {
		return closingBrace == ")"
	}
	if openingBrace == "[" {
		return closingBrace == "]"
	}
	if openingBrace == "{" {
		return closingBrace == "}"
	}
	return false
}
