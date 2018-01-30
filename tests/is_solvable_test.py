import npuzzle_mod

npuzzle = npuzzle_mod.build_npuzzle()
print("npuzzle: {}\nsolvable: {}".format(npuzzle, npuzzle_mod.is_solvable(npuzzle, len(npuzzle))))

