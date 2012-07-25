# -*- coding: cp936 -*-

#logfile = file('test_ltp_python_interface_log.txt', 'w')

from ltp_interface import *

logfilename = 'log.txt'

def test_SplitSentence():
    logfile = open(logfilename, 'a')
    try:
        logfile.write('\n\n--------------\ntest SplitSentence\n')
        CreateDOMFromTxt("test.txt")
        logfile.write('\n\nbefore split sentence, para info')
        coutNum = CountParagraphInDocument()
        for i in range(coutNum):
            logfile.write('\npara ')
            logfile.write(str(i))
            para = GetParagraph(i)
            if para != None:
                logfile.write('\n')
                logfile.write(str(para))

        SplitSentence()
        SaveDOM(r'test_splitsentence.xml')
    finally:
        logfile.close()

if __name__ == '__main__':
    test_SplitSentence()
#CreateDOMFromString("���ﳵλ���٣�ͣ�����鷳����ʱ��Ϊ�˰�ȫ��Ҫͣ���Ա߻�԰��");

#CreateDOMFromTxt("test.txt");
#SplitSentence()
#IRLAS()
#CRFWordSeg()
#PosTag()
#WSD()
#NER()
#Parser()
#GParser()
#SRL()
#SaveDOM('test.xml')

'''
print GetWordsFromSentence(0)
print GetNEsFromSentence(0)

sentNum = CountSentenceInDocument()
for i in range(0, sentNum):
    print GetSentence(i)+"\n"
'''

'''
#----------

print CreateDOMFromTxt('test.txt')
#print SaveDOM('test.xml')
#print CreateDOMFromXml('test.xml')
print SplitSentence()
#print IRLAS()
#print NER()
print WSD()
#print GParser()
print SaveDOM('test.xml')
#print SRL()


#----------

print CreateDOMFromString("�����˾�����Ա20���������������ڰ͸���ϲ�����\
��ʧ�١�����������ʿ�������صķ�����װ��²���Ҳ���ɱ����20�����磬\
�Ѿ���Ա��һ�����վ�����ҵ����������˵�ʬ�塣������Ա��ʾ���м��������\
��������������ǰ���⵽���ǳ��п��Ű��������Ϥ��������ֻ��23���25�����\
������ǰ���ڰ͸���ϲ��Ĺ�·���վִ�ڡ���װ����������͵Ϯ�˸ü��վʱ��\
���������˷�²�⣬������һ�����������������������˰�ȫ��������ɳ���8000����\
��չ�˴��ģ���Ѿȹ����������ҵ���������ʿ�������塣")
print IRLAS()
print SaveDOM('test_string.xml')

#----------

CreateDOMFromXml('test.xml')
NER()
GParser()
WSD()
SRL()
SaveDOM('test.xml')
'''
#----------
'''
CreateDOMFromXml('test.xml')
paraNum = CountParagraphInDocument()
print paraNum
for i in range(paraNum):
    sentNum = CountSentenceInParagraph(i)
    print sentNum, '\n-----'
    for j in range(sentNum):
        print CountWordInSentence(i, j)
    break

sentNum = CountSentenceInDocument()
print sentNum, '\n-----'
for i in range(4):
    print CountWordInSentence(i)

#----------

CreateDOMFromXml('test.xml')

sentNum = CountSentenceInDocument()
for i in range(4, 6):
    wordNum = CountWordInSentence(i)
    for j in range(wordNum-10, wordNum):
        print GetWord(i, j),
        print GetPOS(i, j),
        print GetNE(i, j),
        (wsd, explain) = GetWSD(i, j)
        print wsd, explain,
        #print GetWSD(i, j)
        (parent, relate) = GetParse(i, j)
        print parent, relate
        #print GetParse(i, j)

#----------

CreateDOMFromXml('test.xml')
sentNum = CountSentenceInDocument()
for i in range(sentNum):
    word_list = GetWordsFromSentence(i)
    pos_list = GetPOSsFromSentence(i)
    ne_list = GetNEsFromSentence(i)
    wsd_list = GetWSDsFromSentence(i)
    explain_list = GetWSDExplainsFromSentence(i)
    (parent_list, relate_list) = GetParsesFromSentence(i)
    for j in range(len(word_list)):
        logfile.write("%s %s %s %s %s %d %s\n" % (word_list[j],
                                                  pos_list[j],
                                                  ne_list[j],
                                                  wsd_list[j],
                                                  explain_list[j],
                                                  parent_list[j],
                                                  relate_list[j]
                                                  )
                      )
    logfile.write("\n-----\n")

#--------------
    
CreateDOMFromXml('test.xml')
#print GetTextSummary()
#print GetTextClass()
wordNum = CountWordInDocument()
for i in range(wordNum):
    type_list, beg_list, end_list = GetPredArgToWord(i)
    if type_list == None or type_list == []:
        continue
    for (t, b, e) in zip(type_list, beg_list, end_list):
        logfile.write("%s %d %s\n" % (t, b, e))
'''  


#logfile.close()


