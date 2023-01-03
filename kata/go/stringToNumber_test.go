package kata_test

import (
	. "github.com/kaluzny-konrad/codewarrior"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		Expect(StringToNumber("1234")).To(Equal(1234))
	})

	It("Sample tests", func() {
		Expect(StringToNumber("605")).To(Equal(605))
	})

	It("Sample tests", func() {
		Expect(StringToNumber("1405")).To(Equal(1405))
	})

	It("Sample tests", func() {
		Expect(StringToNumber("0")).To(Equal(0))
	})

	It("Sample tests", func() {
		Expect(StringToNumber("-10")).To(Equal(-10))
	})

	It("Sample tests", func() {
		Expect(StringToNumber("-7")).To(Equal(-7))
	})
})
