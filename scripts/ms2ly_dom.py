#!/usr/bin/env python

from xml.dom import minidom
import sys

indent = ['']


def enterNode(node):
    indent.append(getName(node))
    attributes = "" if len(getAttributes(
        node)) == 0 else ' attr="' + str(getAttributes(node)) + '"'
    text = ' text="' + getText(node) + '"' if len(getText(node)) else ""
    print("->", getPath() + text + attributes)


def exitNode(node):
    print("<-", getPath())
    indent.pop()


def getPath():
    return('/'.join(indent))


def getName(node):
    return node.tagName


def getText(node):
    rc = []
    for node in node.childNodes:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc).strip()


def getAttributes(node):
    attrs = []
    for attr in node.attributes.items():
        attrs.append(attr)
    return attrs


def parseElement(node):
    if (getPath() == "/museScore/Score/Staff"):
        return True
    return False


def parseNode(node):
    if node.nodeType == node.ELEMENT_NODE:
        enterNode(node)
        for subnode in node.childNodes:
            if (not parseElement(node)):
                parseNode(subnode)
        exitNode(node)


if __name__ == "__main__":
    doc = minidom.parse(sys.stdin)
    rootNode = doc.childNodes[0]
    # parserAllElements(doc.childNodes)
    parseNode(rootNode)
