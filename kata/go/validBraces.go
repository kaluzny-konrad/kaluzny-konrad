package kata

import (
	"strings"
)

func ValidBraces(str string) bool {
	for i := 0; i < len(str); {
		length := len(str)
		str = deleteValidBraces(str)
		if length == len(str) {
			return false
		}
	}
	return true
}

func deleteValidBraces(str string) string {
	str = strings.Replace(str, "()", "", -1)
	str = strings.Replace(str, "{}", "", -1)
	str = strings.Replace(str, "[]", "", -1)
	return str
}
