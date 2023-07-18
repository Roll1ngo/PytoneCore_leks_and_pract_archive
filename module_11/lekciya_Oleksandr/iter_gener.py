
class MyIterator:

    def __iter__(self):
      return Iterator()

my_iterator = MyIterator()
for i in my_iterator:
    pass

