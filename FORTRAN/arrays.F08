! Arrays are declared as their data type, plus a dimension attribute:
    real, dimension(4) :: array
    real, dimension(4,4) :: matrix

! Assigning values to an entire array:
    array = (\1.5, 2, 2.5, 3 \)

! Indexing arrays:
    array(2) = 1.5
    matrix(2,1) = 1.9
