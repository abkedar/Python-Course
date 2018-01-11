# example
#
# Remove duplicate entries from a sequence while keeping order
def dupli(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 6, 9, 1, 3, 5]
    print (a)
    print list(dupli(a))