import pickle


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

def dump_emp(emp, file):
    with open(file, 'wb') as f:
        pickle.dump(emp, f)
    f.close()


emp1 = Employee("Mary", 2000)
dump_emp(emp1, 'file.pickle')