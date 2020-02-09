# coding:utf-8
--- 等待添加Gerber文件清理项 ---
import sys
import os
import shutil


def checkPrj(Path):
    for fileName in os.listdir(Path):  # 查找 .prjpcb 文件来确定当前在AD工程目录
        if os.path.splitext(fileName)[1] == '.PrjPCB':
            print('Got it: ' + fileName)
            return os.path.splitext(fileName)[0]


def adClean():
    prjPach = os.path.abspath('.')  # 获取当前路径
    prjName = ''
    print('Path: ' + prjPach)

    prjName = checkPrj(prjPach)  # 检查是否拥有Altium工程文件
    if prjName != '':  # 文件名不为空（找到了文件）

        structurePath = prjPach + '\\' + prjName + '.PrjPCBStructure'  # 工程结构文件
        print(structurePath)
        if os.path.exists(structurePath):
            os.remove(structurePath)
            print('delete file: ' + structurePath)
        else:
            print('unknow PrjPCBStructure file')

        historyPath = prjPach + '\\History'  # 历史文件夹路径
        if os.path.exists(historyPath):
            shutil.rmtree(historyPath)
            print('delete dir: ' + historyPath)
        else:
            print('unknow history path')

        previewsPath = prjPach + '\\__Previews'  # 预览文件夹路径
        if os.path.exists(previewsPath):
            shutil.rmtree(previewsPath)
            print('delete dir: ' + previewsPath)
        else:
            print('unknow previews path')

        logPath = prjPach + '\\Project Logs for ' + prjName  # Log文件路径
        if os.path.exists(logPath):
            shutil.rmtree(logPath)
            print('delete dir: ' + logPath)
        else:
            print('unknow log path')

        gerberPath = prjPach + '\\Project Outputs for ' + prjName  # Gerber文件路径
        if os.path.exists(gerberPath):
            print(gerberPath)
        else:
            print('notdir')

    else:
        print('SearchErr')


if __name__ == '__main__':
    print('clean start')
    adClean()
