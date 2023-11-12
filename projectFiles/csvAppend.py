from csv import writer

row = [314, 123]

with open('event.csv', 'a') as fobj:
    wrObj = writer(fobj)
    wrObj.writerow(row)
    fobj.close
