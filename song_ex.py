#coding:utf-8
import os, sys, shutil

filea = list()
max_num = 0
start_num = 0

max_num = int(max([x for x in ' '.join(os.listdir(u'D:\\tests')).split() if x.isdigit()]))

movie_name = os.listdir(u'D:\\tests')

singers = dict.fromkeys([u'邓丽君', u'陈瑞', u'韦唯', u'降央卓玛', \
                         u'刀郎', u'李谷一', u'卓依婷', u'周华健', \
                         u'苏有朋', u'杨洪基', u'叶倩文', u'李茂山', \
                         u'费翔', u'容祖儿', u'毛阿敏', u'李娜', u'张明敏', \
                         u'韩红', u'韦唯', u'黄安', u'苏小明', u'183Club', \
                         u'Beyond', u'少女时代', u'杨幂', u'田馥甄', u'魏晨', \
                         u'183Club', u'BY2', u'BY2', u'F4', u'JS', u'KOKIA', \
                         u'Madonna', u'Rain', u'Rain', u'S.H.E', u'Sara&后弦', \
                         u'Sara', u'Sweety', u'一加一组合', u'五月天', u'付辛博', \
                         u'任贤齐', u'何韵诗', u'凤凰传奇', u'凤凰传奇', u'吴克群', \
                         u'吴建豪', u'姜育恒', u'孙耀威', u'安心亚', u'容祖儿', \
                         u'容祖儿', u'少女时代', u'张栋梁', u'张靓颖', u'戚薇', \
                         u'戚薇', u' 新建文件夹', u'李佳薇', u'李治廷', u'杨丞琳', \
                         u'杨丞琳', u'杨丞琳', u'杨宗纬', u'汪峰', u'泳儿', u'王力宏', \
                         u'王祖蓝', u'田馥甄', u'田馥甄', u'田馥甄', u'白智英', u'胡夏', u'苏打绿', \
                         u'蔡幸娟', u'邓福如', u'那英', u'郭静', u'陈势安', u'陈楚生', u'陈楚生', u'魏晨', u'黄鸿升'], ['UNKNOWN'])

for key in singers:
    if ['UNKNOWN'] == singers[key]:
        singers[key] = list()

start_num = max_num + 1
print start_num

for song in movie_name:
    print song
    str_val = song.split()
    str_len = len(str_val)

    path = 'D:\\tests' + song

    if os.path.isdir(path):
        shuitl.copy(path2, 'D:\\tests')
    else:
        for key in singers:

            if key in song:#.decode("GBK"):
                #singers[key].append(song.decode("GBK"))
                singers[key].append(song)

    if str_len > 1:
        num, name = str_val[0:2]
        if num.isdigit():
            pass
        elif len(song.split('-')) > 1:
            name, rest = song.split('-')[0:2]
            new_numeric_name = str(start_num) + ' ' + song
            start_num += 1
            os.rename('D:\\tests\\' + song,
                      'D:\\tests\\' + new_numeric_name)
            print 'new name is ', 'D:\\tests\\' + new_numeric_name
        else:
            print 'Cannot handle the song:', song
    else:
        new_numeric_name = str(start_num) + ' ' + song
        start_num += 1
        os.rename('D:\\tests\\' + song,
                  'D:\\tests\\' + new_numeric_name)

for key in singers:
    if singers.get(key, False) and len(singers.get(key)) > 0:
        print '\n===>', key

    for each_song_of_singer in singers[key]:
        print '  ', key, each_song_of_singer
