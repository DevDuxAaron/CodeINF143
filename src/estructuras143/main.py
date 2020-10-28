import csv
import re

# Estudiante: Aaron Joel Limachi Quispe
# CI: 12732282
# INF 143
# Estructura de datos

def calculate_time(dat_1, dat_2):
    """
    :param dat_1: diccionario
    :param dat_2: diccionario
    :return: diccionario de abandonos parciales, actualizacion de tiempo de dat_2
    """
    abandon = dict([])
    eliminado = 0
    err = 0
    # print(len(dat_1), len(dat_2))
    for nro, v in dat_1.items():
        if nro in dat_2:
            # '03h 46'' 23'''''
            line1 = dat_1[nro]['tiempo']
            proof1 = re.findall("[0-9]{1,2}", line1)
            line2 = dat_2[nro]['tiempo']
            proof2 = re.findall("[0-9]{1,2}", line2)
            try:
                segu = int(proof1[2]) + int(proof2[2])
                minu = 0
                hora = 0
                if segu >= 60:
                    minu += 1
                    segu -= 60
                minu += int(proof1[1]) + int(proof2[1])
                if minu >= 60:
                    hora += 1
                    minu -= 60
                hora += int(proof1[0]) + int(proof2[0])
                dat_2[nro]['tiempo'] = "'{}h {}'' {}'''''".format(hora, minu, segu)
            except IndexError:
                err += 1
        else:
            abandon[nro] = dat_1[nro]
            eliminado += 1
    # print("Total de errores:", err)
    # print(eliminado, "Eliminados")
    return dat_2, abandon


def calculate(dat_1, dat_2, dat_3, dat_4, dat_5, dat_6):
    """
    :param dat_1: diccionario del archivo 1
    :param dat_2: diccionario del archivo 2
    :param dat_3: diccionario del archivo 3
    :param dat_4: diccionario del archivo 4
    :param dat_5: diccionario del archivo 5
    :param dat_6: diccionario del archivo 6
    :return: diccionario de abandonos y terminados
    """
    abandon = dict([])
    dat_2, aux = calculate_time(dat_1, dat_2)
    abandon.update(aux)
    dat_3, aux2 = calculate_time(dat_2, dat_3)
    abandon.update(aux2)
    dat_4, aux3 = calculate_time(dat_3, dat_4)
    abandon.update(aux3)
    dat_5, aux4 = calculate_time(dat_4, dat_5)
    abandon.update(aux4)
    finish, aux5 = calculate_time(dat_5, dat_6)
    abandon.update(aux5)
    return abandon, finish


def open_csv(arch: str):
    """
    :param arch: nombre del archivo csv
    :return: diccionario  de tipo
    {
    "numero":{
        "name":"Fulano",
        "nro":2,
        "equipo":"FBC",
        "tiempo":"'03h 46'' 23'''''"
        }
    }
    """
    aux = dict([])
    with open(arch, 'r') as csv_file:
        data = csv.reader(csv_file)
        c = 0
        for line in data:
            aux[line[1]] = {
                'name': line[0],
                'nro': int(line[1]),
                'equipo': line[2],
                'tiempo': line[3]
            }
            c += 1
    return aux

def create_list_time(data):
    with open('ordenado.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_MINIMAL
                                )
        for line in data:
            filewriter.writerow([line['name'], line['nro'], line['equipo'], line['tiempo']])


def create_list_abandon(data):
    with open('abandonos.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_MINIMAL
                                )
        for i in data.values():
            filewriter.writerow([i['name'], i['nro'], i['equipo'], i['tiempo']])


def getkey(item):
    """Llevamos las horas y minutos a segundos"""
    # '03h 46'' 23'''''
    aux = item["tiempo"]
    rex = re.findall("[0-9]{1,2}", aux)
    foo = int(rex[0])*3600 + int(rex[1])*60 + int(rex[2])
    return foo


if __name__ == '__main__':
    data1 = open_csv('tf1.csv')
    data2 = open_csv('tf2.csv')
    data3 = open_csv('tf3.csv')
    data4 = open_csv('tf4.csv')
    data5 = open_csv('tf5.csv')
    data6 = open_csv('tf6.csv')
    aban, ended = calculate(data1, data2, data3, data4, data5, data6)
    # Para ordenar convertimos el diccionario en una lista
    finish = [v for v in ended.values()]
    finish.sort(key=getkey)
    create_list_time(finish)
    create_list_abandon(aban)
