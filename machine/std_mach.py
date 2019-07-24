# -*- coding: UTF-8 -*-
import random
import codecs
import os
import csv
import rsa
from binascii import b2a_hex, a2b_hex

def create_deck_54(new_deck):
    '推出一副新牌'
    print('\n-- debug: I made a new deck.')
    cardJokers = ('♞', '♘')
    cardMarks = ('♠', '♥', '♦', '♣')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    for c in cardJokers:
        new_deck.append(c)
# print(deck)

    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)
    return


def create_deck_52(new_deck):
    '推出一副新牌'
    print('\n-- debug: I made a new deck.')
    '''
    cardJokers = ('♞', '♘')
    '''
    cardMarks = ('♠', '♥', '♦', '♣')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)
    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n--debug:I shuffled a deck')
    random.shuffle(deck_to_be_shuffled)
    return

'''
def record_deck(deck_to_be_record, filename):
    '记录一副牌'
    print('\n--debug: I record a deck')
    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    print('--debug: %s' % (out_path))
    f = codecs.open(out_path, 'w', 'utf-8')
    for card in deck_to_be_record:
        f.write(card)
        f.write('\t')
    f.close

    return
'''
def make_deck_by_type(play_type, out_deck):
    if play_type == 1:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_csv_deck(out_deck, '争上游-刚洗好的牌.txt')
    if play_type == 2:
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_csv_deck(out_deck, '桥牌-刚洗好的牌.txt')
    if play_type == 3:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_csv_deck(out_deck, '三人斗地主-刚洗好的牌.txt')
    if play_type == 4:
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        shuffled_deck(out_deck)
        record_csv_deck(out_deck, '四人斗地主-刚洗好的牌.txt')

        return

def record_csv_deck(deck_to_be_record,csv_filename):
    '用CSV格式记录一副牌'

    csv_path = os.getcwd() + '\\csv_deck\\' + csv_filename
    with open(csv_path,"w",encoding='utf-8',newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(deck_to_be_record)
    return
    '''
def read_deck_csv(csv_filename, out_deck):
    '读取 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_deck\\' + csv_filename
    with open(in_path, "r", encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            out_deck.extend(line)

    return
    '''
def record_deck_crypted_csv(deck_to_be_record, csv_filename, public_key):
    '用加密的CSV格式记录一副牌'

    csv_path = os.getcwd() + '\\csv_deck\\crypted_' + csv_filename
    joined_deck = ','.join(deck_to_be_record)
    # 因为rsa加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    row_data = rsa.encrypt(joined_deck.encode(), public_key)
    #print('--debug: row_data before b2a is %s' % row_data)
    row_data = b2a_hex(row_data)
    #print('--debug: row_data after b2a is %s' % row_data)

    f = open(csv_path, 'wb')
    f.write(row_data)
    f.close()

    # Poker 4.0 added
    msg = '把牌的内容记录到了文件 (%s)' % csv_path
    logger.debug(msg)

    return

'''
def record_csv_deck_crypted(csv_filename, out_deck, private_key):
    '读取加密过的 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_deck\\crypted_' + csv_filename
    f = open(in_path, 'rb')
    line = f.read()
    f.close()

    s = a2b_hex(line)
    row_data = rsa.decrypt(s, private_key)
    #print('--debug: read from csv file : %s' % row_data.decode())
    s = row_data.decode()
    out_deck.extend(s.split(','))
    print(out_deck)

    # Poker 4.0 added
    msg = '从文件 (%s) 中读取了牌的内容' % in_path
    logger.debug(msg)

    return
'''
def record_csv_deck_crypted(deck_to_be_record, csv_filename, public_key):
    '用加密的CSV格式记录一副牌'

    csv_path = os.getcwd() + '\\csv_deck\\crypted_' + csv_filename
    joined_deck = ','.join(deck_to_be_record)
    # 因为rsa加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    row_data = rsa.encrypt(joined_deck.encode(), public_key)
    #print('--debug: row_data before b2a is %s' % row_data)
    row_data = b2a_hex(row_data)
    #print('--debug: row_data after b2a is %s' % row_data)

    f = open(csv_path, 'wb')
    f.write(row_data)
    f.close()

    # Poker 4.0 added

    return

def read_csv_deck_crypted(csv_filename, out_deck, private_key):
    '读取加密过的 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_deck\\crypted_' + csv_filename
    f = open(in_path, 'rb')
    line = f.read()
    f.close()

    s = a2b_hex(line)
    row_data = rsa.decrypt(s, private_key)
    #print('--debug: read from csv file : %s' % row_data.decode())
    s = row_data.decode()
    out_deck.extend(s.split(','))
    print(out_deck)

    # Poker 4.0 added

    return
