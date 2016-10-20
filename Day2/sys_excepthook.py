import sys

def my_excepthook(type, value, traceback):
    print("Unhandled exception", type, value, traceback)

sys.excepthook=my_excepthook
print('Before exception')

raise RuntimeError('This is the error message')

print('After exception')
