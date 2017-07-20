! Starting and ending a program:
program program_name
implicit none
! Insert code here.
end program program_name



! All variables used in the program must be declared at the top.
! Declaration of data types:
    real :: a, b
    integer :: c
    complex :: d
    logical :: e   ! Boolean value, .true. or .false.
    character :: f   ! String

! Specifying size of variables in bytes:
    real(kind = 4) :: a
    integer(kind = 16) :: b

! Specifying length of string: (1 byte(1 ASCII character) by default):
    character(len = 12) :: name

! Constant variable that can't be changed during runtime:
    real, parameter :: pi = 3.14


! Printing:
    print*, a, b    ! Printing variable a and b.


! Checking the size of an integer or real: (in bytes)
    print*, kind(a)

! Size of a string:
    print*, len(a)
! Appending multiple strings:
    x = a//b//c

! Relation operators:
    a == b
    a /= b
    a > b
    a < b
    a >= b
    a <= b

! Logical operators:
    a .and. b
    a .or. b
    .not. a
    a .eqv. b    ! Equivalent. True if a and b holds same boolean value.
    a .neqv. b


! if / else blocks: (else if's and else is optional.)
    if ( a < 20 ) then
        print*, "a is less than 20"
    else if ( a < 40 ) then
        print*, "a is less than 40"
    else
        print*, "a is more than 40"
    end if


! Select case. Compares an expression (here x) against multiple "cases" (here a and b).
! The expression and cases must be the same data type, either logical, integer or character.
    select case (x)
        case (a)
            print*, "x is equal to a"
        case (b)
            print*, "x is equal to b"
        case default
            print*, "x is not equal to a or b"
    end select

! With integers, you can also specify a range for the selector:
    select case (x)
        case (10:20)
    end select


! For-loops:
    do i = 1, 10, 2   ! (start, stop, increment(optional))
        print*, "i =", i
    end do

! While-loops:
    do while ( i < 10 )
        i = i+1
    end do

! Flow control statements:
    exit    ! exits the loop
    cycle    ! starts at the next iteration cycle of the loop
