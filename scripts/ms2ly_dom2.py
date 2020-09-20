#!/usr/bin/env python

from xml.dom import minidom
import sys

xml_paths = {
    "measure": "/museScore/Score/Staff/Measure",
    "chord": "/museScore/Score/Staff/Measure/voice/Chord",
    "rest": "/museScore/Score/Staff/Measure/voice/Rest",
    "staff": "/museScore/Score/Staff",
    "header": "/museScore/Score/Staff/VBox/Text",
    "keySignature": "/museScore/Score/Staff/Measure/voice/KeySig",
    "timeSignature": "/museScore/Score/Staff/Measure/voice/TimeSig",
    "rehearsalMark": "/museScore/Score/Staff/Measure/voice/RehearsalMark",
    "barLine": "/museScore/Score/Staff/Measure/voice/BarLine",
    "startRepeat": "/museScore/Score/Staff/Measure/startRepeat",
    "endRepeat": "/museScore/Score/Staff/Measure/endRepeat",
    "measureSpanner": "/museScore/Score/Staff/Measure/voice/Spanner",
    "chordSpanner": "/museScore/Score/Staff/Measure/voice/Chord/Spanner",
    "noteSpanner": "/museScore/Score/Staff/Measure/voice/Chord/Note/Spanner",
    "layoutBreak": "/museScore/Score/Staff/Measure/LayoutBreak",
    "lyrics": "/museScore/Score/Staff/Measure/voice/Chord/Lyrics",
    "clef": "/museScore/Score/Staff/Measure/voice/Clef",
    "partStaff": "/museScore/Score/Part/Staff",
    "harmony": "/museScore/Score/Staff/Measure/voice/Harmony"
}


class XmlParser():
    indent = ['']

    def __init__(self, node):
        print("# init")
        self.parseNode(node)

    def enterNode(self, node):
        self.indent.append(self.getName(node))
        attributes = "" if len(self.getAttributes(
            node)) == 0 else ' attr="' + str(self.getAttributes(node)) + '"'
        text = ' text="' + self.getText(node) + '"' if len(self.getText(node)) else ""
        print("# ->", self.getPath() + text + attributes)
        attr_text = ""
        for a in self.getAttributes(node):
            attr_text += ",%s=%s" % (a[0], a[1])
        print("cd %s%s" % (self.getName(node), attr_text))

    def onNodeExit(self):
        pass

    def exitNode(self, node):
        print("# <-", self.getPath())
        print("cd ..")
        self.onNodeExit()
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
                if ('/' in childName):
                    if (self.getName(subnode) == childName.split('/')[0]):
                        return self.getTextFromChild(subnode, "/".join(childName.split('/')[1:]))
                else:
                    if (self.getName(subnode) == childName):
                        return self.getText(subnode)
        return ""

    def hasChild(self, node, childName):
        for subnode in node.childNodes:
            if subnode.nodeType == subnode.ELEMENT_NODE:
                if (self.getName(subnode) == childName):
                    return True
        return False

if __name__ == "__main__":
    doc = minidom.parse(sys.argv[1])
    rootNode = doc.childNodes[0]
    xml = XmlParser(rootNode)