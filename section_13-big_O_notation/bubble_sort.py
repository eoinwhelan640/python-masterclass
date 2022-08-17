# naive implementation
def bubble_sort(data: list) -> None:
    """Sorts a list in place"""
    n = len(data)
    comparison_count = 0

    #compare all the way up til youre comparing penultimate thing to last thing (n-1 comparisons to be made)
    for i in range(n-1):
        for j in range(n-1):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j +1], data[j]
        print(f"End of pass {i}. `data` is now {data}")
    print(f"comparison_count is {comparison_count}")


def bubble_sort_opt(data: list) -> None:
    """Sorts a list in place"""
    n = len(data)
    comparison_count = 0
    for i in range(n-1):
        # reduce the amount of times it goes around, no more pointless comparisons
        for j in range(n-1-i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j +1], data[j]
        print(f"End of pass {i}. `data` is now {data}")
    print(f"comparison_count is {comparison_count}")


def bubble_sort_opt_more(data: list) -> None:
    """Sorts a list in place"""
    n = len(data)
    comparison_count = 0
    for i in range(n-1):
        swapped = False
        # reduce the amount of times it goes around, no more pointless comparisons
        for j in range(n-1-i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j +1], data[j]
                swapped = True
        print(f"End of pass {i}. `data` is now {data}")
        if not swapped:
            # the last pass had no swaps, so early exit as data is now sorted
            break
            # could while not swapped: version of loop using while instead of for loop
    print(f"comparison_count is {comparison_count}")

# best worst and average case for algo
# worst case is the data in reverse order, so everything must be sorted backward

# best case - already sorted
#numbers = [1,2,3,4,5,6,7] # when running this we're making n-1 comparisons, best case
numbers = [7, 6, 5, 4, 3, 2, 1] # worst case we make 21 comparisons, worst case
#numbers = [3, 2, 4, 1, 5, 7, 6]
#numbers = [1,2,3,4,6,5,7]
#numbers = list(range(70, 0, 1))

print(f"Sorting {numbers}")
bubble_sort_opt_more(numbers)
print(f"The sorted data is {numbers}")

