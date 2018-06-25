#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import os


class Dataan(object):    
    def __init__(self, initdir=None):
        self.modelpath = u'题库模板.xlsx'
        self.path = u'题库模板 - 副本.xlsx'
        self.datamach(self.path)
        
        
    def datamach(self,path):
        self.modeldf = pd.DataFrame(pd.read_excel(self.modelpath))
        self.df = pd.DataFrame(pd.read_excel(path))
        for i in range(self.df.shape[0]):
            print str(self.modeldf.ix[i,u'工时明细']).find('e')
            if (self.modeldf.ix[i,u'项目']!=self.df.ix[i,u'项目']) |\
            (self.modeldf.ix[i,u'子项目']!=self.df.ix[i,u'子项目'])|\
            (self.modeldf.ix[i,u'人员']!=self.df.ix[i,u'人员']):
                self.df.ix[i,u'结果'] = '拒绝'
                self.df.ix[i,u'意见'] = '项目错误'
            elif self.modeldf.ix[i,u'工时']!=self.df.ix[i,u'工时']:
                self.df.ix[i,u'结果'] = '拒绝'
                self.df.ix[i,u'意见'] = '项目错误'
            elif self.modeldf.ix[i,u'工时明细'][:(str(self.modeldf.ix[i,u'工时明细']).find('e'))+1]!=\
            self.df.ix[i,u'工时明细'][:(str(self.df.ix[i,u'工时明细']).find('e'))+1]:
                self.df.ix[i,u'结果'] = '拒绝'
                self.df.ix[i,u'意见'] = '项目错误'
            else:
                self.df.ix[i,u'结果'] = '通过'
                self.df.ix[i,u'意见'] = 'ok'
        print (self.df)
        return self.df


if __name__ == '__main__':
    d = Dataan(os.curdir)

