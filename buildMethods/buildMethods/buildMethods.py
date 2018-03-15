# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 07:05:19 2018

@author: Aron
"""


import os
import shutil
import time
import stat
#import numpy



#sourceRoot = r'\\cii6s029\DE12S'
#destRoot = r'\\shi6s007\DE12S'
#folderPath = r''


sourceRoot = r'\\plm\cinas\cae_nxn\nastran_tools'
destRoot = r'\\shv6s12\nxn\nastran_tools'

folderPath = r'bin'



skipFolderFullPaths = [r'\\cii6s029\DE13S\nxn13\nast\tpl',]
#skipFolderFullPaths = [r'\\cii6s029\DE12S\nxn12\nast\tpl', r'\\cii6s029\DE12S\nxn12p01\nast\tpl', r'\\cii6s029\DE12S\nxn12p02\nast\tpl']

findKeyWords = []
#findKeyWords = ['.bat']

excludeKeyWords = []
#excludeKeyWords = ['.#makebook','.NxnAqa','.viminfo','#qa_','@']


subFolders = True



# Full Path
sourcePath = os.path.join(sourceRoot,folderPath)
destPath = os.path.join(destRoot,folderPath)


#skipPath = os.path.join(sourceRoot,skipFolder)
skipList = skipFolderFullPaths


# Dir and File Name
sourceFileDir = os.path.dirname(sourcePath)
sourceFileName = os.path.basename(sourcePath)
destFileDir = os.path.dirname(destPath)
destFileName = os.path.basename(destPath)

print('From:    ',sourcePath)
print('Copy to: ',destPath)



#print('Source File?',os.path.isfile(sourcePath))
#print('Source Dir ?',os.path.isdir(sourcePath)) 





##################################################################



def copyDirectory(src,dst,skipList=[],findKeys=[],exKeys=[],subFd=True):
    names = os.listdir(src)
    
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)

        if os.path.isfile(srcname):
            fileCopy = False
            if findKeys == [] :
                fileCopy = True
            else:
                for findKey in findKeys :
                    if findKey in srcname :
                        fileCopy = True
                        
            for excludeKey in exKeys:
                if excludeKey in srcname:
                    fileCopy = False
            
            
            if fileCopy:
                if not os.path.exists(dst):
                    os.makedirs(dst)
                    print('++ Destination File Tree Created ',dst)
                    
                    
                identicalFile = False
                if os.path.isfile(dstname):
    #                fSource = os.stat(srcname)
    #                fDest = os.stat(dstname)
    #                identicalFile = fSource.st_mtime == fDest.st_mtime
                    os.chmod(dstname, stat.S_IWRITE)
                    identicalFile = (os.stat(srcname).st_mtime == os.stat(dstname).st_mtime)
                    
                if identicalFile:
                    print('Same File',srcname)
                else:
                    print('>Copy File: ',srcname)
                    shutil.copy2(srcname, dstname)
            else:
                print('File skipped-> ',srcname)
        
        elif os.path.isdir(srcname):
            if srcname in skipList:
                print('**Skip Path**: ',srcname)
            else:
                if subFolders:
                    if not os.path.exists(dstname):
                        os.makedirs(dstname)
                        print('++ Destination File Tree Created ',dstname)
                    
                    copyDirectory(srcname,dstname,skipList,findKeys,exKeys,subFd)
                
                else:
                    print('*<Skip Subfolders>*: ',srcname)
                
        










###################################################################







print('\n---------- File Transfer Started ----------')
localtime1 = time.clock()
print('Clock Time at: %0.4e' % localtime1)


if os.path.isfile(sourcePath):
    fileCopy = False
    if findKeyWords == [] :
        fileCopy = True
    else:
        for findKey in findKeyWords :
            if findKey in sourcePath :
                fileCopy = True
                
    for excludeKey in excludeKeyWords:
        if excludeKey in sourcePath:
            fileCopy = False

                
    if fileCopy :
        if not os.path.exists(destFileDir):
            os.makedirs(destFileDir)
            print('++ Destination File Tree Created ',destFileDir)
            
            
        identicalFile = False
        if os.path.isfile(destPath):
            fSource = os.stat(sourcePath)
            fDest = os.stat(destPath)
            os.chmod(destPath, stat.S_IWRITE)
            identicalFile = fSource.st_mtime == fDest.st_mtime
            
        if identicalFile:
            print('Same File ',sourcePath)
        else:
            print('>Copy File: ',sourcePath)
            shutil.copy2(sourcePath, destPath)
    else:
        print('File skipped-> ',sourcePath)

elif os.path.isdir(sourcePath):
    if sourcePath in skipList:
        print('**Skip Path**: ',sourcePath)
    else:
        if not os.path.exists(destPath):
            os.makedirs(destPath)
            print('++ Destination File Tree Created ',destPath)
        
        copyDirectory(sourcePath,destPath,skipList,findKeyWords,excludeKeyWords,subFolders)


else:
    print('\n>>>>>>>>>> Not a valid source !!! <<<<<<<<<<\n')







localtime2 = time.clock()
print('---------- File Tansfer Completed ----------')
print('Clock Time at: %0.4e' % localtime2)
print('===== Total Clock Time =====: %0.4f s' % (localtime2-localtime1) )


'''







##############################################3




###############################################

#os.rmdir()
#shutil.rmtree()
'''
