def bubble_sorting(arr: list[int]):
    num = len(arr)

    for i in range(num - 1):
        for j in range(0, num - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)


def main():
    data_array: list[int] = [1, 8, 5, 6, 2, 5]

    # sorting
    bubble_sorting(data_array)


if __name__ == '__main__':
    main()
