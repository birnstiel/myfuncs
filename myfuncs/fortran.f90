doubleprecision function mypower(a, f)
    doubleprecision, intent(in) :: a, f
    mypower = a**f
end function mypower

subroutine myaddition(a, b, c)
    doubleprecision, intent(in) :: a, b
    doubleprecision, intent(out) :: c
    c = a + b
end subroutine myaddition