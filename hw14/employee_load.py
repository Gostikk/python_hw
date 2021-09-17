import pickle
from hw14.employee_dump import Employee


def load_emp(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    f.close()
    return data


emp2 = load_emp('file.pickle')
print(emp2)