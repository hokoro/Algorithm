def solution(s_list):
    s_split = []
    for s in s_list:
        s_split.append(s.split(', '))

    # for s in s_split:
    #      print(s)

    s_split.sort(key=lambda x: (x[1], x[2]))

    file_list = []

    warsaw_count = 1
    london_count = 1
    paris_count = 1

    for s in s_split:
        if s[1] == 'Warsaw':
            file_list.append([s[1] + '0' + str(warsaw_count) + s[0][-4:], s[2]])
            warsaw_count += 1
        if s[1] == 'London':
            file_list.append([s[1] + str(london_count) + s[0][-4:], s[2]])
            london_count += 1
        if s[1] == 'Paris':
            file_list.append([s[1] + str(paris_count) + s[0][-4:], s[2]])
            paris_count += 1

    answer = []

    for s in s_list:
        s = s.split(', ')
        for file in file_list:
            if s[2] == file[1]:
                answer.append(file[0])
    return answer

s_list = ['photo.jpg, Warsaw, 2013-09-05 14:08:15',
          'john.png, London, 2015-06-20 15:13:22',
          'myFriends.png, Warsaw, 2013-09-05 14:07:13',
          'Eiffel.jpg, Paris, 2015-07-23 08:03:02',
          'pisatower.jpg, Paris, 2015-07-22 23:59:59',
          'BOB.jpg, London, 2015-08-05 00:02:03',
          'notredame.png, Paris, 2015-09-01 12:00:00',
          'me.jpg, Warsaw, 2013-09-06 15:40:22',
          'a.png, Warsaw, 2016-02-13 13:33:50',
          'b.jpg, Warsaw, 2016-01-02 15:12:22',
          'c.jpg, Warsaw, 2016-01-02 14:34:30',
          'd.jpg, Warsaw, 2016-01-02 15:15:01',
          'e.png, Warsaw, 2016-01-02 09:49:09',
          'f.png, Warsaw, 2016-01-02 10:55:32',
          'g.jpg, Warsaw, 2016-02-29 22:13:11']


print(solution(s_list))

# s_split = []
# for s in s_list:
#     s_split.append(s.split(', '))
#
# # for s in s_split:
# #      print(s)
#
# s_split.sort(key=lambda x: (x[1], x[2]))
#
# file_list = []
#
# warsaw_count = 1
# london_count = 1
# paris_count = 1
#
# for s in s_split:
#     if s[1] == 'Warsaw':
#         file_list.append([s[1] + '0' + str(warsaw_count) + s[0][-4:], s[2]])
#         warsaw_count += 1
#     if s[1] == 'London':
#         file_list.append([s[1] + str(london_count) + s[0][-4:], s[2]])
#         london_count += 1
#     if s[1] == 'Paris':
#         file_list.append([s[1] + str(paris_count) + s[0][-4:], s[2]])
#         paris_count += 1
#
# answer = []
#
# for s in s_list:
#     s = s.split(', ')
#     for file in file_list:
#         if s[1][:5] == file[0][:5] and s[2] == file[1]:
#             answer.append(file[0])
# print(answer)
