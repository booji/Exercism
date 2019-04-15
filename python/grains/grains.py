def on_square(integer_number: int) -> int:
    is_valid_num(integer_number)
    return 1 << (integer_number - 1)


def total_after(integer_number: int) -> int:
    is_valid_num(integer_number)
    return (1 << integer_number) - 1


def is_valid_num(integer_number: int) -> bool:
    if not(1 <= integer_number <= 64):
        raise ValueError("Integer has to be in range of 1-64")
    return True
