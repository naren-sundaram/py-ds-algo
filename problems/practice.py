def picking_numbers(a):
    diffs = []
    for idx, ele in enumerate(a):
        pos_neg_diff = [0, 0]
        for i_idx, i_ele in enumerate(a):
            if idx != i_idx:
                if abs(ele - i_ele) <= 1:
                    if ele >= i_ele:
                        pos_neg_diff[0] += 1
                    else:
                        pos_neg_diff[1] += 1
        diffs.append(max(pos_neg_diff))
        break
    return max(diffs) + 1 if diffs else 0


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = picking_numbers(a)
    print(result)
