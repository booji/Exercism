def triplets_with_sum(sum_of_triplet):
    lower_c_bound = sum_of_triplet//3
    #upper_a_bound = sum_of_triplet//3

    return triplets_in_range(lower_c_bound,sum_of_triplet)


def triplets_in_range(range_start, range_end):
    result = set()
    for c in range(range_start,range_end):
        for a in range(1,range_end//3):
            b = range_end-c-a
            if b < a:
                break
            if is_triplet((a,b,c)):
                result.add((a,b,c))
    return result


def is_triplet(triplet):
    return triplet[0]**2+triplet[1]**2 == triplet[2]**2


def main():
    print(sorted(triplets_with_sum(840)))

if __name__ == '__main__':
    main()
