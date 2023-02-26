import csv
import json
from collections import OrderedDict

#2019510038 Simay Göçen - 2019510094 Elif Özker
f = open('students.csv', 'r')
reader = csv.reader(f)
header = next(reader)
students = {}
for row in reader:#file reading
    for word in row:
        word = word.split(';')
        students[word[0]] = {'id': word[0], 'name': word[1], 'lastname': word[2], 'email': word[3],
                             'grade': word[4]}

#Please enter name quotes like this '' on the normal computer keyboard format!!!!!!

def main():
    flag = True
    while (flag):
        query = input("Enter query: ")
        query = query.split(" ")
        if query[0].upper() == "SELECT":#SELECT CONTROL
            select_keyword = query[1].split(",")
            for w in select_keyword:
                if w == "name" or w == "lastname" or w == "email" or w == "grade" or w == "id":#format controlling
                    continue
                else:
                    print("Invalid format")
                    flag = False
            if flag == False:
                break

            if query[2].upper() == "FROM" and query[3].upper() == "STUDENTS" and query[4].upper() == "WHERE":
                if query[8].upper() == "AND" or query[8].upper() == "OR":
                    if query[5] == 'id' or query[5] == 'grade':
                        if query[8].upper() == "AND":
                            if query[9] == 'id' or query[9] == 'grade':
                                tempdict = int_comparison(query[5], query[6], query[7], students)
                                tempdict2 = int_comparison(query[9], query[10], query[11], students)
                            else:
                                tempdict = int_comparison(query[5], query[6], query[7], students)
                                tempdict2 = string_comparison(query[9], query[10], query[11], students)
                            common = common_AND(tempdict, tempdict2, query[14])
                            print_Common(common, select_keyword)
                        elif query[8].upper() == "OR":
                            if query[9] == 'id' or query[9] == 'grade':
                                tempdict = int_comparison(query[5], query[6], query[7], students)
                                tempdict2 = int_comparison(query[9], query[10], query[11], students)
                            else:
                                tempdict = int_comparison(query[5], query[6], query[7], students)
                                tempdict2 = string_comparison(query[9], query[10], query[11], students)
                            common = common_OR(tempdict, tempdict2, query[14])
                            print_Common(common, select_keyword)

                        else:
                            print("Invalid Format!")


                    else:
                        if query[8].upper() == "AND":
                            if query[9] == 'id' or query[9] == 'grade':
                                tempdict = string_comparison(query[5], query[6], query[7], students)
                                tempdict2 = int_comparison(query[9], query[10], query[11], students)
                            else:
                                tempdict = string_comparison(query[5], query[6], query[7], students)
                                tempdict2 = string_comparison(query[9], query[10], query[11], students)
                            common = common_AND(tempdict, tempdict2, query[14])
                            print_Common(common, select_keyword)

                        elif query[8].upper() == "OR":
                            if query[9] == 'id' or query[9] == 'grade':
                                tempdict = string_comparison(query[5], query[6], query[7], students)
                                tempdict2 = int_comparison(query[9], query[10], query[11], students)
                            else:
                                tempdict = string_comparison(query[5], query[6], query[7], students)
                                tempdict2 = string_comparison(query[9], query[10], query[11], students)
                            common = common_OR(tempdict, tempdict2, query[14])
                            print_Common(common, select_keyword)
                        else:
                            print("Invalid Format!")

                elif query[2].upper() == "FROM" and query[3].upper() == "STUDENTS" and query[4].upper() == "WHERE" and \
                        query[8].upper() == "ORDER" and query[9].upper() == "BY":  # BİR GİRDİLİ OLAN
                    if query[5] == 'id' or query[5] == 'grade':
                        tempdict = int_comparison(query[5], query[6], query[7], students)
                    else:
                        tempdict = string_comparison(query[5], query[6], query[7], students)

                    if (query[10].upper() == "ASC"):
                        tempdict = OrderedDict(sorted(tempdict.items(), key=lambda i: i[1]['id']))
                        print_Common(tempdict, select_keyword)
                    elif (query[10].upper() == "DSC"):
                        tempdict = OrderedDict(sorted(tempdict.items(), key=lambda i: i[1]['id'], reverse=True))
                        print_Common(tempdict, select_keyword)
                    else:
                        print("Invalid Format!")
                else:
                    print("Invalid Format!")
            else:
                print("Invalid Format!")

        # INSERT CONTROL
        elif query[0].upper() == "INSERT" and query[1].upper() == "INTO" and query[2].upper() == "STUDENTS":
            word = query[3].split("(")
            word2 = word[1].split(",")
            word3 = word2[4].split(")")
            students[word2[0]] = {'id': word2[0], 'name': word2[1], 'lastname': word2[2], 'email': word2[3],
                                  'grade': word3[0]}


        # DELETE CONTROL
        elif  query[0].upper() == "DELETE" and query[1].upper() == "FROM" and query[2].upper() == "STUDENTS" and query[3].upper() == "WHERE" and (query[4] == 'id' or query[4] == 'name' or query[4] == 'lastname' or query[4] == 'email' or query[
            4] == 'grade'):
            if query[5] == 'id' or query[5] == 'grade':
                tempdict = int_comparison(query[4], query[5], query[6], students)
            else:
                tempdict = string_comparison(query[4], query[5], query[6], students)
            delete(tempdict)

        elif query[0].upper() == "DELETE" and query[1].upper() == "FROM" and query[2].upper() == "STUDENTS" and query[3].upper() == "WHERE" and (query[7].upper() == "AND" or query[7].upper() == "OR"):
            if query[4] == 'id' or query[4] == 'grade':
                if query[7].upper() == "AND":
                    if query[8] == 'id' or query[8] == 'grade':
                        tempdict = int_comparison(query[4], query[5], query[6], students)
                        tempdict2 = int_comparison(query[8], query[9], query[10], students)
                    else:
                        tempdict = int_comparison(query[4], query[5], query[6], students)
                        tempdict2 = string_comparison(query[8], query[9], query[10], students)

                    delete_AND(tempdict, tempdict2)

                elif query[7].upper() == "OR":
                    if query[8] == 'id' or query[8] == 'grade':
                        tempdict = int_comparison(query[4], query[5], query[6], students)
                        tempdict2 = int_comparison(query[8], query[9], query[10], students)
                    else:
                        tempdict = int_comparison(query[4], query[5], query[6], students)
                        tempdict2 = string_comparison(query[8], query[9], query[10], students)
                    delete_OR(tempdict, tempdict2)
                else:
                    print("Invalid Format!")

            else:
                if query[7].upper() == "AND":
                    if query[8] == 'id' or query[8] == 'grade':
                        tempdict = string_comparison(query[4], query[5], query[6], students)
                        tempdict2 = int_comparison(query[8], query[9], query[10], students)

                    else:
                        tempdict = string_comparison(query[4], query[5], query[6], students)
                        tempdict2 = string_comparison(query[8], query[9], query[10], students)

                    delete_AND(tempdict, tempdict2)

                elif query[7].upper() == "OR":
                    if query[8] == 'id' or query[8] == 'grade':
                        tempdict = string_comparison(query[4], query[5], query[6], students)
                        tempdict2 = int_comparison(query[8], query[9], query[10], students)
                    else:
                        tempdict = string_comparison(query[4], query[5], query[6], students)
                        tempdict2 = string_comparison(query[8], query[9], query[10], students)
                    delete_OR(tempdict, tempdict2)
                else:
                    print("Invalid Format!")
        elif query[0].upper() == "EXIT":
            flag = False
        else:
            print("Invalid Format!")
        creatingJSON(students)




def int_comparison(query1, query2, query3, students):
    tempdict = {}
    for k, v in students.items():
        if query2 == "<":
            if int(v[query1]) < int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}

        elif query2 == ">":
            if int(v[query1]) > int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}

        elif query2 == "=":
            if int(v[query1]) == int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}

        elif query2 == "!=":
            if int(v[query1]) != int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}

        elif query2 == "<=":
            if int(v[query1]) <= int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}
        elif query2 == ">=":
            if int(v[query1]) >= int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}

        elif query2 == "!<":
            if int(v[query1]) > int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}
        elif query2 == "!>":
            if int(v[query1]) < int(query3):
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}
        else:
            print("Invalid Input")
    return tempdict


def string_comparison(query1, query2, query3, students):
    tempdict = {}

    for k, v in students.items():
        str = "'" + v[query1] + "'"
        if query2 == "=":
            if str == query3:
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}
        elif query2 == "!=":
            if str != query3:
                tempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                     'grade': v['grade']}
        else:
            print("Invalid Format!")
    return tempdict


def common_AND(dict1, dict2, query_14):
    common = {}
    for k, v in dict1.items():
        for k1, v1 in dict2.items():
            if (v['id'] == v1['id']):
                common[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                   'grade': v['grade']}
    if (query_14.upper() == "ASC"):
        common = OrderedDict(sorted(common.items(), key=lambda i: i[1]['id']))
    elif (query_14.upper() == "DSC"):
        common = OrderedDict(sorted(common.items(), key=lambda i: i[1]['id'], reverse=True))
    return common


def common_OR(dict1, dict2, query_14):
    # SELECT name,lastname FROM STUDENTS WHERE grade !< 40 ORDER BY ASC

    newtempdict = {}
    for k, v in dict1.items():
        for k1, v1 in dict2.items():
            if v['id'] not in v1['id']:
                newtempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'],
                                        'email': v['email'],
                                        'grade': v['grade']}
    for k, v in dict2.items():
        newtempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                'grade': v['grade']}

    if query_14.upper() == "ASC":
        newtempdict = OrderedDict(sorted(newtempdict.items(), key=lambda i: i[1]['id']))
    elif query_14.upper() == "DSC":
        newtempdict = OrderedDict(sorted(newtempdict.items(), key=lambda i: i[1]['id'], reverse=True))

    return newtempdict


def print_Common(common, select_keyword):
    if len(common) != 0:
        for k, v in common.items():
            for w in select_keyword:
                print(v[w], end=" ")
            print()
    else:
        print("There is no student with the given features")

def delete_AND(dict1, dict2):
    if len(dict1) != 0 and len(dict2) != 0:
        for k, v in dict1.items():
            for k1, v1 in dict2.items():
                if v['id'] == v1['id']:
                    del students[v['id']]
    else:
        print("There is no student with the given features")

def delete(dict1):
    if len(dict1) != 0 :
        for k, v in dict1.items():
            del students[v['id']]
    else:
        print("There is no student with the given features")

def delete_OR(dict1, dict2):
    newtempdict = {}
    for k, v in dict1.items():
        for k1, v1 in dict2.items():
            if v['id'] not in v1['id']:
                newtempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'],
                                        'email': v['email'], 'grade': v['grade']}
    for k, v in dict2.items():
        newtempdict[v['id']] = {'id': v['id'], 'name': v['name'], 'lastname': v['lastname'], 'email': v['email'],
                                'grade': v['grade']}

    if len(newtempdict) != 0:
        for k, v in newtempdict.items():
            del students[v['id']]
    else:
        print("There is no student with the given features")

def creatingJSON(myRecord):
    my_Record_Json = json.dumps(myRecord, ensure_ascii=False)
    with open("myRecord", "w") as f:
        f.write(my_Record_Json)

main()
