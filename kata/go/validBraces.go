package kata

func ValidBraces(str string) bool {

	length := len(str)
	for i := 0; i < length; i++ {
		toSkip := 0

		openingBrace := string(str[i])
		if isOpeningBrace(openingBrace) {
			closingBrace := ""

			for j := i + 1 + toSkip; j < length; j++ {
				brace := string(str[j])
				if isClosingBrace(brace) {
					closingBrace = string(str[j+toSkip])
					break
				} else {
					toSkip++
				}
			}

			validClosingBrace := getCloseBrace(openingBrace)
			if closingBrace != validClosingBrace {
				return false
			}
		}
	}

	return true
}

func isOpeningBrace(brace string) bool {
	return brace == "(" || brace == "[" || brace == "{"
}

func isClosingBrace(brace string) bool {
	return brace == ")" || brace == "]" || brace == "}"
}

func getCloseBrace(openingBrace string) string {
	if openingBrace == "(" {
		return ")"
	}
	if openingBrace == "[" {
		return "]"
	}
	if openingBrace == "{" {
		return "}"
	}
	return ""
}
