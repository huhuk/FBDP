#!/home/huhu/pyenv/hbase/bin/python3.5

import happybase

path_folder = './'
path_meta = path_folder + 'py_stu.table'
path_data = path_folder + 'students.data'

host = 'localhost'

t_name = ''
cf = dict()
c_index = dict()

def get_meta():
    print('get meta', end='...')
    with open(path_meta, 'r') as f:
        global t_name
        t_name = f.readline().strip()
        print(t_name)
        for line in f:
            line = line.strip().split(':', 1)
            cf[line[0]] = dict()
            for c in line[1].split(','):
                c_index[c] = line[0]
        print(cf)
        print(c_index)
    print('success')

def create_connection(host):
    print('connect...')
    return happybase.Connection(host=host)

def create_table(conn, name, cf):
    print('create table', end='...')
    name = bytes(name, encoding='utf8')
    if name in conn.tables():
        print('exists...', 'delete...')
        conn.delete_table(name, disable=True)
        print('del success!', end='...')
    conn.create_table(name, cf)
    print('success!')

def scan(table):
    print('scan table...')
    print('ROW\t\tCOLUMN+CELL')
    for k, vals in table.scan():
        for val in vals:
            s = k.decode('utf8') + '\t\t'
            s += 'column=' + val.decode('utf8')
            s += ', value=' + vals[val].decode('utf8')
            print(s)

def add_data(table):
    print('add data', end='...')
    with open(path_data, 'r') as f:
        for line in f:
            line = line.strip().split(' ', 1)
            row = line[0]
            data = dict()
            for item in line[1].split(','):
                col, val = item.split(':')
                data[c_index[col] + ':' +  col] = val
            table.put(row, data)
    print('success')

if __name__ == '__main__':
    get_meta()
    conn = create_connection(host)
    create_table(conn, t_name, cf)
    table = conn.table(t_name)
    add_data(table)
    scan(table)

