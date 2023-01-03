package kata

import (
	"strconv"
)

func StringToNumber(str string) int {
	intVar, err := strconv.Atoi(str)
	if err != nil {
		panic(err)
	}
	return intVar
}
