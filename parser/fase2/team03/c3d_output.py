from wrapper import *
from goto import *


@with_goto
def all_code():
    clear_all_execution()
    exec_sql('CREATE DATABASE IF NOT EXISTS test;')
    exec_sql('USE test;')

    exec_sql(
        'create table tbcalifica'
        '( iditem integer not null primary key,'
        'item   varchar(150) not null,'
        'puntos float not null );'
    )

    exec_sql('insert into tbcalifica(iditem, item, puntos) values (1,\'Funcionalidades básicas\',2.0);')

    t1 = 1 + 1
    exec_sql(f'insert into tbcalifica(iditem, item, puntos) values ({t1},\'Funcionalidades X\',3.0);')

    exec_sql(f'insert into tbcalifica(iditem, item, puntos) values (3*2,\'Funcionalidades Meh\',4.0);')

    result = []
    i = 1
    stop = 5
    label.begin
    if i == stop:
        goto.end

    result.append(i)
    i += 1
    goto.begin

    label.end
    print(result)


all_code()
report_stored_st()
