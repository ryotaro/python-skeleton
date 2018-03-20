if __name__ == '__main__':
  from module import Adder
  from datetime import datetime
  adder = Adder(1)
  print('Hello world', adder.add(datetime.now().hour))