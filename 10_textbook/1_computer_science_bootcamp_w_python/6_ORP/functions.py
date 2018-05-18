
import openpyxl
import math

def get_data_from_excel(filename):
    """
    get_data_from_excel(filename) -> {'name1' : 'score1', 'name2' : 'score2'....}
    import data from excel file

    retern value (dictionary)
    key : student name
    value : score
    """

    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows

    for name, score in g:
        dic[name.value] = score.value

    return dic


def avg(scores):
    s = 0
    for score in scores:
        s += score
    return round(s/len(scores), 1)


def var(scores, avg):
    s = 0
    for score in scores:
        s += (score - avg) ** 2
    return round(s/len(scores), 1)


def std_dev(var):
    return round(math.sqrt(var), 1)


def evaluateClass(avg, total_avg, std_dev, sd):
    """
    evaluateCalss(avg, total_avg, std_dev, sd) --> None

    avg: class avg score
    total_avg : grade avg score
    std_dev : class standard deviation
    sd : target standard deviation
    """


    if avg < total_avg and std_dev > sd:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")

    elif avg > total_avg and std_dev > sd:
        print("성적이 평균 이상이지만, 학생들의 실력 차이가 너무 크다.")

    elif avg < total_avg and std_dev < sd:
        print("성적이 저조하고, 학생들의 실력차이는 크지 않다")

    elif avg > total_avg and std_dev < sd:
        print("성적은 평균이상, 학생들의 실력차이도 크지 않다")
