# coding:utf-8
import os,sys,shutil

#print 'Hello',
#'Lyp'  


movie_name = os.listdir('E:\\music')

singers = dict.fromkeys([u'邓丽君', u'陈瑞', u'韦唯', u'降央卓玛', \
                         u'刀郎', u'李谷一', u'卓依婷', u'周华健', \
                         u'苏有朋', u'杨洪基', u'叶倩文', u'李茂山', \
                         u'费翔', u'容祖儿', u'毛阿敏', u'李娜', u'张明敏',\
                         u'韩红', u'韦唯', u'黄安', u'苏小明', u'183Club', \
                         u'Beyond',u'少女时代',u'杨幂',u'田馥甄',u'魏晨', \
                         u'183Club',u'BY2',u'BY2',u'F4',u'JS',u'KOKIA', \
                         u'Madonna',u'Rain',u'Rain',u'S.H.E',u'Sara&后弦', \
                         u'Sara',u'Sweety',u'一加一组合',u'五月天',u'付辛博', \
                         u'任贤齐',u'何韵诗',u'凤凰传奇',u'凤凰传奇',u'吴克群', \
                         u'吴建豪',u'姜育恒',u'孙耀威',u'安心亚',u'容祖儿', \
                         u'容祖儿',u'少女时代',u'张栋梁',u'张靓颖',u'戚薇', \
                         u'戚薇',u' 新建文件夹',u'李佳薇',u'李治廷',u'杨丞琳', \
                         u'杨丞琳',u'杨丞琳',u'杨宗纬',u'汪峰',u'泳儿',u'王力宏', \
                         u'王祖蓝',u'田馥甄',u'田馥甄',u'田馥甄',u'白智英',u'胡夏',u'苏打绿', \
                         u'蔡幸娟',u'邓福如',u'那英',u'郭静',u'陈势安',u'陈楚生',u'陈楚生',u'魏晨',u'黄鸿升'], ['UNKNOWN'])

#dira = list()
filea = list()
max_num = 0
start_num = 0

for song in movie_name:
	if len(song.split()) > 1:
		 		num, name = song.split()[0:2]
				if num.isdigit():
					 			if int(num) > max_num:
									max_num = int(num)
												
start_num = max_num + 1

for song in movie_name:			
		 if len(song.split()) > 1:
		 		num, name = song.split()[0:2]
		 		if num.isdigit():
		 			num_tmp = song.split(' ')[0]
		 			name = song.split(' ')[1]
		 			if len(name.split('-'))> 1 :
		 				name = name.split('-')[0]
		 				#print '~~~~~~', name

		 				#singers.setdefault(name, ['UNKNOWN'])
		 				
		 			continue	
		 		elif len(song.split('-')) > 1:
		 			name, rest = song.split('-')[0:2]
		 			#print name
		 			#print '~~~~~~', name
		 			
		 			#singers.setdefault(name, ['UNKNOWN'])
		 			new_numeric_name = str(start_num) +' ' + song
		 			start_num += 1
		 			os.rename('E:\\music\\'+song, 'E:\\music\\'+new_numeric_name)
		 			print 'new name is ', 'E:\\music\\'+new_numeric_name
		 		else:
		 			print 'LEAVE', song	
		 else:
		 		new_numeric_name = str(start_num) +' ' + song
		 		start_num += 1
		 		os.rename('E:\\music\\'+song, 'E:\\music\\'+new_numeric_name)
		 			
		 		if len(song.split('-')) > 1:
		 			name, rest = song.split('-')[0:2]
		 			print '~~~~~~', name
		 			
		 			#singers.setdefault(name, ['UNKNOWN'])
		 		else:
		 			print 'special', song
		 			
#print '!!!max num is : %s, dictory is:' %max_num

#for key in singers.keys():
#	print key	,						  	


for temp in movie_name:
    path = 'E:\\music' + temp
    if os.path.isdir(path):
    		print 'hihihihi 1'
    		print 'hi'
    		#path2 = ''.join('E:\\music\"', temp , '\"')
    		#print path2
    		shuitl.copy(path2, 'E:\\music')
    		#cmd = r'xcopy /S /Y \"%s\" E:\\music\' %path2
    		#print cmd
    		#exit(0)	
    		
				#print path2
				
        #dira.append(path)       
        #print 'hi'
				#cmd = r"xcopy /S /Y %s E:\\music\" %path2
				#print cmd, path2
				#os.system(cmd)
    else:
        for key in singers:
            if ['UNKNOWN'] == singers[key]:
                singers[key] = list()
            #print key,  singers[key], len(singers[key]), '++++++', temp.decode("GBK")

            #continue

            # if temp.index(key) >= 0 :
            #    print 'temp!!'
            # continue
            #s = u'中文'
            #if (isinstance(s, str)):
                # s为'中文'
            #    print '1:', s.decode('utf8').encode('gb2312')

            #else:
                # s为u'中文'
            #    print '2:', s, key, temp.decode("GBK"), key in temp.decode("GBK")#s.decode('utf8').encode('gbk')


            if key in temp.decode("GBK"):
                #print 'GBK found 11!!',  len(singers[key]), key, singers #temp.decode("GBK"), singers[key], temp,temp.decode("GBK")
                singers[key].append(temp.decode("GBK"))#temp.decode("GBK"))
            #else:
                #print 'GBK not found 22!!', len(singers[key]), key, singers[key]#[-1] #, '|', temp, temp.decode("GBK")

            # filea.append(path)

# print '===DIR==='
# for items in dira:
#   print items
print

#print '===FILE==='
#for items in filea:
#    print items

print
#print '===SONG==='

for key in singers:
    if singers.get(key, False) and len(singers.get(key)) > 0:
        print '\n===>', key#, 'Song Len: ', len(singers[key]) #, --> "," means do not change lines

    for each_song_of_singer in singers[key]:
        print '  ', key, each_song_of_singer	
