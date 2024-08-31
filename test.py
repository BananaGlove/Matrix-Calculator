from Matrix import Matrix

m = Matrix(2, 2, data={
    (1, 1): 2, (1, 2): 4,
    (2, 1): 5, (2, 2): 1
})

m *= 3

m.show()

m.inverse()

m.show()