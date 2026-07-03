from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    Sum = 0
    for i in range(3):
        Sum += triplet[i]
    return (Sum)


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    Volume = 1
    for i in range(3):
        Volume = Volume * box_dimensions[i]
    return(Volume)
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
