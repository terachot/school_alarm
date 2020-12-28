def get_box_area(width, length, height):
    box_area = width * length * height
    return box_area


box1 = get_box_area(4, 4, 3)
box2 = get_box_area(width=3, length=3, height=3)

print(box1)
print(box2)