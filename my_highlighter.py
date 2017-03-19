# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MyHighlighterCpp(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(MyHighlighterCpp, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b"]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)

class MyHighlighter1C(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(MyHighlighter1C, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.red)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["\\b[нН][оО][вВ][ыЫ][йЙ]\\b",
        "\\b[пП][оО][кК][аА]\\b",
        "\\b[вВ][оО][зЗ][вВ][рР][аА][тТ]\\b",
         "\\b[тТ][оО][гГ][дД][аА]\\b", 
         "\\b[иИ][нН][аА][чЧ][еЕ]\\b",
         "\\b[еЕ][сС][лЛ][иИ]\\b", 
         "\\b[иИ][нН][аА][чЧ][еЕ][еЕ][сС][лЛ][иИ]\\b", 
         "\\b[кК][оО][нН][еЕ][цЦ][еЕ][сС][лЛ][иИ]\\b", 
         "\\b[иИ][сС][тТ][иИ][нН][аА]\\b",
         "\\b[лЛ][оО][жЖ][ьЬ]\\b",
         "\\b[Дд][лЛ][яЯ]\\b",
         "\\b[пП][оО]\\b",
         "\\b[Дд][лЛ][яЯ]\\s[кК][аА][жЖ][дД][оО][гГ][оО]\\b", 
         "\\b[цЦ][иИ][кК][лЛ]\\b",
         "\\b[кК][оО][нН][еЕ][цЦ][цЦ][иИ][кК][лЛ][аА]\\b",
         "\\b[пП][рР][оО][цЦ][еЕ][дД][уУ][рР][аА]\\b",
         "\\b[кК][оО][нН][еЕ][цЦ][пП][рР][оО][цЦ][еЕ][дД][уУ][рР][ыЫ]\\b",
         "\\b[фФ][уУ][нН][кК][цЦ][иИ][яЯ]\\b",
         "\\b[кК][оО][нН][еЕ][цЦ][фФ][уУ][нН][кК][цЦ][иИ][иИ]\\b",
         "\\b[пП][оО][пП][ыЫ][тТ][кК][аА]\\b",
         "\\b[иИ][сС][кК][лЛ][юЮ][чЧ][еЕ][нН][иИ][еЕ]\\b",
         "\\b[кК][оО][нН][еЕ][цЦ][пП][оО][пП][ыЫ][тТ][кК][иИ]\\b", 
         "\\b[эЭ][кК][сС][пП][оО][рР][тТ]\\b"]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        symbolFormat = QTextCharFormat()
        symbolFormat.setForeground(Qt.red)
        symbolFormat.setFontWeight(QFont.Bold)

        symbolPatterns = ["\.","\+","\-","\=","\;","\>","\<"]

        for pattern in symbolPatterns:
            self.highlightingRules.append((QRegExp(pattern), symbolFormat))
        # classFormat = QTextCharFormat()
        # classFormat.setFontWeight(QFont.Bold)
        # classFormat.setForeground(Qt.darkMagenta)
        # self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
        #         classFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.darkGreen)

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.black)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        # functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("\\b[А-Яа-я0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # startIndex = 0
        # if self.previousBlockState() != 1:
        #     startIndex = self.commentStartExpression.indexIn(text)

        # while startIndex >= 0:
        #     endIndex = self.commentEndExpression.indexIn(text, startIndex)

        #     if endIndex == -1:
        #         self.setCurrentBlockState(1)
        #         commentLength = len(text) - startIndex
        #     else:
        #         commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

        #     self.setFormat(startIndex, commentLength,
        #             self.multiLineCommentFormat)
        #     startIndex = self.commentStartExpression.indexIn(text,
        #             startIndex + commentLength);