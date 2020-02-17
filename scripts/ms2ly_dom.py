#!/usr/bin/env python

from xml.dom import minidom
import sys


class XmlParser():
    indent = ['']

    def __init__(self, node):
        print("init")
        self.parseNode(node)

    def enterNode(self, node):
        self.indent.append(self.getName(node))
        attributes = "" if len(self.getAttributes(
            node)) == 0 else ' attr="' + str(self.getAttributes(node)) + '"'
        text = ' text="' + self.getText(node) + \
            '"' if len(self.getText(node)) else ""
        print("->", self.getPath() + text + attributes)

    def exitNode(self, node):
        print("<-", self.getPath())
        self.indent.pop()

    def getPath(self, customIndent=None):
        if (customIndent == None):
            customIndent = self.indent
        return('/'.join(customIndent))

    def getName(self, node):
        return node.tagName

    def getText(self, node):
        rc = []
        for node in node.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc).strip()

    def getAttributes(self, node):
        attrs = []
        for attr in node.attributes.items():
            attrs.append(attr)
        return attrs

    def getParentNodeByPath(self, currentNode, path):
        indentPath = list(self.indent)
        nodeParent = currentNode
        while (len(indentPath)):
            indentPath.pop()
            nodeParent = nodeParent.parentNode
            if (self.getPath(indentPath) == path):
                break
        return nodeParent

    def parseElement(self, node):
        return False

    def parseNode(self, node):
        if node.nodeType == node.ELEMENT_NODE:
            self.enterNode(node)
            if (not self.parseElement(node)):
                for subnode in node.childNodes:
                    self.parseNode(subnode)
            self.exitNode(node)

    def isTextInChildren(self, node, text):
        childrenText = []
        # TODO: recursive?
        for subnode in node.childNodes:
            childrenText.append(self.getText(subnode))
        return text in childrenText

    def getTextFromChild(self, node, childName):
        for subnode in node.childNodes:
            if subnode.nodeType == subnode.ELEMENT_NODE:
                if (self.getName(subnode) == childName):
                    return self.getText(subnode)
        return ""


class MuseScoreParser(XmlParser):
    xml_paths = {
        "measure" : "/museScore/Score/Staff/Measure",
        "chord": "/museScore/Score/Staff/Measure/voice/Chord",
        "rest": "/museScore/Score/Staff/Measure/voice/Rest",
        "staff": "/museScore/Score/Staff",
        "header": "/museScore/Score/Staff/VBox/Text",
        "keySignature": "/museScore/Score/Staff/Measure/voice/KeySig",
        "timeSignature": "/museScore/Score/Staff/Measure/voice/TimeSig",
        "rehearsalMark": "/museScore/Score/Staff/Measure/voice/RehearsalMark",
        "barLine": "/museScore/Score/Staff/Measure/voice/BarLine"
    }

    def getStaffId(self, node):
        staff = self.getParentNodeByPath(node, self.xml_paths['staff'])
        for attr in self.getAttributes(staff):
            if (attr[0] == 'id'):
                return attr[1]
        return None

    def getTitle(self, node):
        return "title"

    def parseElement(self, node):
        # if you got all data from node and don't want to make a recursion on that node return True
        if (self.getPath() == self.xml_paths['measure']):
            return False

        if (self.getPath() == self.xml_paths['header']):
            if (self.getTextFromChild(node, "style") == "Title"):
                print("title:", self.getTextFromChild(node, "text"))
                return True
            elif (self.getTextFromChild(node, "style") == "Composer"):
                print("composer:", self.getTextFromChild(node, "text"))
                return True
        
        if (self.getPath() == self.xml_paths['chord']):
            print(self.getStaffId(node))
            return True

        if (self.getPath() == self.xml_paths['keySignature']):
            print("keySignatures:", self.getTextFromChild(node, "accidental"))
            return True

        if (self.getPath() == self.xml_paths['timeSignature']):
            print("timeSignature:", self.getTextFromChild(node, "sigN") + "/" + self.getTextFromChild(node, "sigD"))
            return True

        return False


if __name__ == "__main__":
    doc = minidom.parse(sys.stdin)
    rootNode = doc.childNodes[0]
    MuseScoreParser(rootNode)
