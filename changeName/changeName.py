
# -*- coding: utf-8 -*-
import os
import os.path


path = os.path.split(os.path.realpath(__file__))[0]
path += '/png'
print("当前路径:" + path)
# curDir= os.getcwd()
# print('getcwd__' + curDir)

        
for root, dirs, files in os.walk(path):   
    print(root) #当前目录路径  
    print('\n')
    print('dirs')
    print(dirs) #当前路径下所有子目录  
    print('\n')
    print('files')
    print(files) #当前路径下所有非目录子文件  

    for filename in files: 
        if filename.find('zz') != -1 :
            newName = filename[2:]
        else:		
            newName  = 'zz'
            newName += filename
        print(filename,'----->',newName) 
        os.rename(os.path.join(root,filename),os.path.join(root,newName))
