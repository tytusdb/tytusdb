import json
import hashlib
import os
import csv


def turn_on_safe_mode(database, table):
    blockchain = {}
    with open('data/info/safeModeTables/' + database + table + '.json', 'w') as file:
        json.dump(blockchain, file, indent=4)


def turn_off_safe_mode(database, table):
    os.remove('data/info/safeModeTables/' + database + table + '.json')


def concat_register(register):
    concat_string = ''
    for i in register:
        concat_string += str(i)
    return concat_string


def generate_hash(string_data):
    return hashlib.sha256(string_data.encode()).hexdigest()


def generate_chain(database, table, registers):
    blockchain = {}
    blockId = 1
    previous = '0000000000000000000000000000000000000000000000000000000000000000'

    for register in registers:
        hash = generate_hash(concat_register(register))
        blockchain[blockId] = {'blockId': blockId, 'data': register, 'previous': previous, 'hash': hash, 'status': 0}
        blockId += 1
        previous = hash

    with open('data/info/safeModeTables/' + database + table + '.json', 'w') as file:
        json.dump(blockchain, file, indent=4)


def update_block(database, table, newRegister, oldRegister):
    oldHash = generate_hash(concat_register(oldRegister))
    newHash = generate_hash(concat_register(newRegister))
    with open('data/info/safeModeTables/' + database + table + '.json', 'r') as file:
        blockchain = json.load(file)
        for blockId in blockchain:
            if blockchain[blockId]['hash'] == oldHash:
                blockchain[blockId]['data'] = newRegister
                blockchain[blockId]['hash'] = newHash
                blockchain[blockId]['status'] = 1
                break
    with open('data/info/safeModeTables/' + database + table + '.json', 'w') as file:
        json.dump(blockchain, file, indent=4)


def delete_block(database, table, register):
    hash = generate_hash(concat_register(register))
    with open('data/info/safeModeTables/' + database + table + '.json') as file:
        blockchain = json.load(file)
        for blockId in blockchain:
            if blockchain[blockId]['hash'] == hash:
                del blockchain[blockId]
                break
    with open('data/info/safeModeTables/' + database + table + '.json', 'w') as file:
        json.dump(blockchain, file, indent=4)


def insert_block(database, table, register):
    with open('data/info/safeModeTables/' + database + table + '.json') as file:
        blockchain = json.load(file)
        if len(blockchain) == 0:
            previous = '0000000000000000000000000000000000000000000000000000000000000000'
            blockId = 1
        else:
            previousId = int(list(blockchain.keys())[-1])
            previous = blockchain[str(previousId)]['hash']
            blockId = previousId + 1
        hash = generate_hash(concat_register(register))
        blockchain[blockId] = {'blockId': blockId, 'data': register, 'previous': previous, 'hash': hash, 'status': 0}
    with open('data/info/safeModeTables/' + database + table + '.json', 'w') as file:
        json.dump(blockchain, file, indent=4)


def chartBlockchain(database, table):
    blockchain = None
    with open('data/info/safeModeTables/' + database + table + '.json') as file:
        blockchain = json.load(file)
    file = open('blockchain.dot', 'w')
    file.write('digraph blockchain {\n')
    file.write('rankdir=LR;\n')
    file.write('node[shape=box]\n')
    color = '#DCF0C2'
    previous = '0000000000000000000000000000000000000000000000000000000000000000'
    if len(blockchain) > 0:
        for i in blockchain.values():
            if color == '#DCF0C2' and (i['status'] == 1 or i['previous'] != previous):
                color = '#F3ABAB'
            file.write(str(i['blockId']) + '[label=<')
            file.write('<TABLE BORDER="0" BGCOLOR=' + '"' + color + '" ' +
                       'CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">')
            file.write('<TR><TD>' + 'Bloque: ' + '</TD><TD>' + '# ' + str(i['blockId']) + '</TD></TR>')
            file.write('<TR><TD>' + 'Datos: ' + '</TD><TD>' + str(i['data']) + '</TD></TR>')
            file.write('<TR><TD>' + 'Anterior: ' + '</TD><TD>' + str(i['previous']) + '</TD></TR>')
            file.write('<TR><TD>' + 'Hash: ' + '</TD><TD>' + str(i['hash']) + '</TD></TR>')
            file.write('</TABLE>')
            file.write('>, ];')
            previous = i['hash']
    count = 0
    nodes = list(blockchain.keys())
    for i in nodes:
        if count + 1 < len(nodes):
            file.write(nodes[count] + '->' + nodes[count + 1] + '\n')
        count += 1
    file.write('}')
    file.close()
    os.system("dot -Tpng blockchain.dot -o blockchain.png")
    os.system('blockchain.png')


def insert_block_CSV(results, file, database, table):
    count = 0
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for i in reader:
            if results[count] == 0:
                insert_block(database, table, i)
            count += 1
