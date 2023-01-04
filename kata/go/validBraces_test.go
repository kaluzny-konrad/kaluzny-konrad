package kata_test

import (
	"fmt"

	. "github.com/kaluzny-konrad/codewarrior"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func singleTest(str string, res bool) {
	It(fmt.Sprintf("should return %v for \"%v\"", res, str), func() {
		Expect(ValidBraces(str)).To(Equal(res))
	})
}

var _ = Describe("Valid Braces", func() {
	singleTest("(){}[]", true)
	singleTest("([{}])", true)
	singleTest("(}", false)
	singleTest("[(])", false)
	singleTest("[({)](]", false)
})
