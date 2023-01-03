package kata

// ns : slice of indices
// xs, ys : chromosomes as slices of ints
func Crossover(ns []int, xs []int, ys []int) ([]int, []int) {
	m := make(map[int]bool)
	for _, val := range ns {
		m[val] = true
	}

	for k := range m {
		for i := k; i < len(xs); i++ {
			xs[i], ys[i] = ys[i], xs[i]
		}
	}

	return xs, ys
}
