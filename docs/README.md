# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## 1. General description of the solution
The library is designed to calculate the areas and perimeters of the main shapes: circle, square, rectangle and triangle.
Each shape is implemented in a separate Python module with two functions: `area()` and `perimeter()'.

Project structure:
- `circle.py`
- `square.py`
- `rectangle.py`
- `triangle.py`
- `docs/README.md`

## 2. Description of functions with call examples

### `circle.py`

`area(r)` - Takes the value of the radius and returns the value of the area of the circle  

r: float - circle radius
```
area(5)
return 25 * pi 
```

`perimeter(r)` - Takes the value of the radius and returns the length of the circle.

r: float - circle radius
```
perimeter(5)
return 10 * pi
```

### `square.py`

`area(a)` - Takes the length of the side of a square and returns the area of the square

a: float - side of a square
```
area(5)
return 25
```

`perimeter(a)` - Takes the length of the side of the square and returns the perimeter of the square

a: float - side of a square
```
perimeter(5)
return 20
```

### `rectangle.py`

`area(a, b)` - Takes the values of the sides of a rectangle and returns the area of the rectangle

a: float - side of a rectangle

b: float - side of a rectangle
```
area(3, 5)
return 15
```

`perimeter(a, b)` - Takes the values of the sides of the rectangle and returns the perimeter of the rectangle

a: float - side of a rectangle

b: float - side of a rectangle
```
perimeter(3, 5)
return 16
```

### `triangle.py`
`area(a, h)` - Takes the values of the side and height of the triangle and returns the area of the triangle

a: float - side of a triangle

b: float - height of a triangle
```
area(2, 3)
return 3
```

`perimeter(a, b, c)` - Takes the values of the sides of a triangle and returns the perimeter of the triangle

a: float - side of a triangle

b: float - side of a triangle

c: float - side of a triangle

```
perimeter(3, 5, 7)
return 15
```
### 3. Testing

Added tests to verify the correctness of the work. 

The tests are in the files test_circle.py, test_rectangle.py, test_square.py, test_triangle.py


### 4. Project change history
```
2025-09-19 — fixed an error in the file rectangle.py — 31f5f4c
2025-09-19 — new file has been added — 690e40a
2021-03-04 — L-03: Docs added — d078c8d
2021-03-04 — L-03: Circle and square added — 8ba9aeb
```