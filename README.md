# Vector Class

Implement a class named Vector2D to represent points in the 2-dimensional Euclidean space R^2, which includes the following properties (variables) and methods (functions):

- Two variables x and y
- Initialization method __init__
- Method __str__ to display the vector as (x, y)
- Method __add__ for adding two instances of this class
- Method __eq__ for comparing two instances of this class
- Method norm for calculating the magnitude of a vector.

#### Sample code:
```
p1 = Vector2D(1, 2)
p2 = Vector2D(3, 1)
p3 = p1 + p2

print(p1)
print(p2)
print(p3)
print(p3.norm())
print(p1==p2)
```

#### Output:
```
(1, 2)
(3, 1)
(4, 3)
5.0
False
```
