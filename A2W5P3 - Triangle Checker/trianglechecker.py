def check_triangle(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return True
    elif (side_a >= side_b + side_c) or (side_b >= side_a + side_c) or (side_c >= side_a + side_b):
        return False
    else:
        return True


if __name__ == "__main__":
    side_a = int(input("Side A: "))
    side_b = int(input("Side B: "))
    side_c = int(input("Side C: "))

    if check_triangle(side_a, side_b, side_c):
        print("Possible triangle")
    else:
        print("Impossible triangle")