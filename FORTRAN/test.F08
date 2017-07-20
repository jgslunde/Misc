program program_name
implicit none

integer(kind = 8) :: a, b, result
character(len = 8) :: name
logical :: bool1, bool2

a = 1
b = 2
result = a + b
print*, a, b, result

name = "Jonas"
print*, name

bool1 = .true.
bool2 = .false.
print*, .not. bool1 .or. bool2


end program program_name
