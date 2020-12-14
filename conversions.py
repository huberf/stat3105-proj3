import json

def accel_conv(fname):
    contents = open(fname, 'r').read()
    lines = contents.split('\n')
    data = []
    start_collect = False
    for l in lines:
        if start_collect and not l == '':
            row = [float(i) for i in l.split(', ')]
            data.append(row)
        if l == '@DATA':
            start_collect = True
    return data

if __name__ == '__main__':
    file_name = input('File path: ')
    data = accel_conv(file_name)
    open('out.csv', 'w').write('\n'.join(['time,xacc,yacc,zacc'] + [', '.join([str(i) for i in row]) for row in data]))
