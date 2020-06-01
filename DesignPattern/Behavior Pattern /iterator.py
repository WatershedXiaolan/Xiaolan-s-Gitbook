def iterator(iterable, n):
    iterator = zip(range(n), iterable)
    for _, item in iterator:
        # yield: continuously output items
        yield item

iterable = ['Apple', 'Orange', 'Pear', 'Fear']

for i in iterator(iterable, 3):
    print(i)

