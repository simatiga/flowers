# -*- coding: utf-8 -*-
'''
Created on 2022. 4. 29.

@author: parlo
'''
import pandas as pd

# sr = pd.Series([17000, 18000, 1000, 5000],
#                index=["피자", "치킨", "콜라", "맥주"])
#
# print('시리즈 출력 :')
# print('-'*15)
#
# print(sr)
#
# print('시리즈의 값 : {}'.format(sr.values))
# print('시리즈의 인덱스 : {}'.format(sr.index))

# values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# index = ['one', 'two', 'three']
# columns = ['A', 'B', 'C']

# df = pd.DataFrame(values, index=index, columns=columns)

# print('데이터프레임 출력 :')
# print('-'*18)
# print(df)

# print('데이터프레임의 인덱스 : {}'.format(df.index))
# print('데이터프레임의 열이름: {}'.format(df.columns))
# print('데이터프레임의 값 :')
# print('-'*18)
# print(df.values)



# data = [['1행', '1행2열', '1행3열'],
#         ['2행', '2행2열', '2행3열'],
#         ['3행', '3행2열', '3행3열']]
#
# df = pd.DataFrame(data, columns=['c1', 'c2', 'c3'])
# print(df)


####kakao talk
# text = ""
#
# with open("C:\Users\parlo\Desktop\KakaoTalk_20220429_1103_31_378_group.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         text+=line
#
# print(text)


####kakao talk
import re
import pandas as pd


# def katalk_msg_parse(file_path):
def katalk_msg_parse(file_path):
    text = ""
    
    # with open("C:\\Users\\parlo\\Desktop\\KakaoTalk_20220429_1103_31_378_group.txt", "r", encoding="utf-8") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         text+=line
    #
    # print(text)
    
    my_katalk_data = list()
    katalk_msg_pattern = "[0-9]{4}[년.] [0-9]{1,2}[월.] [0-9]{1,2}[일.] 오\S [0-9]{1,2}:[0-9]{1,2},.*:"
    date_info = "[0-9]{4}년 [0-9]{1,2}월 [0-9]{1,2}일 \S요일"
    in_out_info = "[0-9]{4}[년.] [0-9]{1,2}[월.] [0-9]{1,2}[일.] 오\S [0-9]{1,2}:[0-9]{1,2}:.*"
    
    for line in open(file_path, "r", encoding="UTF-8"):
        if re.match(date_info, line) or re.match(in_out_info, line):
            continue
        elif line == '\n':
            continue
        elif re.match(katalk_msg_pattern, line):
            line = line.split(",")
            date_time = line[0]
            user_text = line[1].split(" : ", maxsplit=1)
            user_name = user_text[0].strip()
            text = user_text[1].strip()
            my_katalk_data.append({'date_time': date_time,
                                   'user_name': user_name,
                                   'text': text
                                   })
    
        else:
            if len(my_katalk_data) > 0:
                my_katalk_data[-1]['text'] += "\n"+line.strip()
    
    my_katalk_df = pd.DataFrame(my_katalk_data)
    
    return my_katalk_df


katalk_msg_parse('C:\\Users\\parlo\\Desktop\\KakaoTalk_20220429_1103_31_378_group.txt')

