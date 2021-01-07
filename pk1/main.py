import csv
import time
from faker import Faker

from pk1 import utils


class hospital:
    name = ""
    grade = ""
    scale = ""
    online_consultation = ""
    main_departments = ""
    number_of_patients = ""
    service = ""
    quality = ""
    effectiveness = ""


    def __init__(self,a):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])

    def __init__(self, b):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])


def GenerateData():
    with open('hospital.csv', 'w', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, 100):
            hospital = hospital()
            spamwriter.writerow([hospital.name, hospital.grade, hospital.scale,
                                 hospital.online_consultation, hospital.main_departments,
                                 hospital.number_of_patient,hospital.service,
                                 hospital.quality,hospital.effectiveness])

class Search:
    def search1(self):
        itemNum = -1
        name = self.text()
        print(name)
        data = self.readData()
        nrows = data[1]
        values = data[0]
        ncols = data[2]
        for row in range(nrows):
            cell = values[row][1]
            if name.lower() == cell.lower():
                itemNum = row
                print(itemNum)
                print(values[itemNum])
                break
            else:
                continue

        if itemNum < 1:
            print("error")
        else:
            dict = {}
            for row in range(1, nrows):
                if itemNum != row:
                    a = utils.tra(values[itemNum], values[row])
                    b = utils.tra(values[row])
                    row_num = values[row][0]
                    distance = utils.PearsonCorrelation(a, b)
                    dict[row_num] = distance
                else:
                    continue
            newDis = sorted(dict.items(), key=lambda d: d[1], reverse=True)
            print(newDis[0], newDis[1], newDis[2])
            hospital1 = int(newDis[0][0])
            hospital2 = int(newDis[1][0])
            hospital3 = int(newDis[2][0])
            print(hospital1, hospital2, hospital3)


    def search2(self):
        data = self.readData()
        nrows = data[1]
        values = data[0]
        ncols = data[2]

        dict = {}
        for row in range(1, nrows):
            c = utils.tra(input, values[row])
            d = utils.tra(values[row])
            name2 = values[row][1]
            row_num = values[row][0]
            # print(c, d, name2)
            distance = utils.Euclidean(c, d)
            dict[row_num] = distance
            # print(f"{name2} distance = {distance}")
            # print(dict)

        # Dictionary sort
        newDis = sorted(dict.items(), key=lambda d: d[1])
        print(newDis)
        print(newDis[0], newDis[1], newDis[2])
        index = {}
        for i in range(0, 6):
            index[i] = int(newDis[i][0])
        for row in range(len(index)):
            for col in range(1, ncols):
                self.model.setItem(row, col - 1)
        return index

    def add_sub(self):
        str = []
        for i in range(self.model.rowCount()):
            str.append(self.model.data(self.model.index(i, 0)))
        print(str)
        for i in range(len(str)):
            self.model2.setItem(i)



search = Search()
