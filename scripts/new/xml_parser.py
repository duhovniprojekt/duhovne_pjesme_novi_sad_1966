#!/usr/bin/env python

from xml.dom import minidom
import sys

print_debug = False

class XmlParser():
    indent = ['']

    def __init__(self, path):
        if print_debug: print("%% init")
        doc = minidom.parse(path)
        node = doc.childNodes[0]
        self.parse_node(node)

    def enter_node(self, node):
        self.indent.append(self.get_name(node))
        attributes = "" if len(self.get_attributes(
            node)) == 0 else ' attr="' + str(self.get_attributes(node)) + '"'
        text = ' text="' + self.get_text(node) + \
            '"' if len(self.get_text(node)) else ""
        if print_debug: print("%% ->", self.get_path() + repr(text) + attributes)

    def on_node_exit(self):
        pass

    def exit_node(self, node):
        if print_debug: print("%% <-", self.get_path())
        self.on_node_exit()
        self.indent.pop()

    def get_path(self, custom_indent=None):
        if (custom_indent == None):
            custom_indent = self.indent
        return('/'.join(custom_indent))

    def get_name(self, node):
        return node.tagName

    def get_text(self, node):
        rc = []
        for node in node.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc).strip()

    def get_attributes(self, node):
        attrs = []
        for attr in node.attributes.items():
            attrs.append(attr)
        return dict(attrs)

    def get_parent_node_by_path(self, current_node, path):
        indent_path = list(self.indent)
        node_parent = current_node
        while (len(indent_path)):
            indent_path.pop()
            node_parent = node_parent.parent_node
            if (self.get_path(indent_path) == path):
                break
        return node_parent

    def parse_element(self, node):
        return False

    def parse_node(self, node):
        if node.nodeType == node.ELEMENT_NODE:
            self.enter_node(node)
            if (not self.parse_element(node)):
                for subnode in node.childNodes:
                    self.parse_node(subnode)
            self.exit_node(node)

    def is_text_in_children(self, node, text):
        children_text = []
        # TODO: recursive?
        for subnode in node.childNodes:
            children_text.append(self.get_text(subnode))
        return text in children_text

    def get_text_from_child(self, node, child_name):
        for subnode in node.childNodes:
            if subnode.nodeType == subnode.ELEMENT_NODE:
                if ('/' in child_name):
                    if (self.get_name(subnode) == child_name.split('/')[0]):
                        return self.get_text_from_child(subnode, "/".join(child_name.split('/')[1:]))
                else:
                    if (self.get_name(subnode) == child_name):
                        return self.get_text(subnode)
        return ""

    def has_child(self, node, child_name):
        for subnode in node.childNodes:
            if subnode.nodeType == subnode.ELEMENT_NODE:
                if (self.get_name(subnode) == child_name):
                    return True
        return False

if __name__ == "__main__":
    x = XmlParser(sys.stdin)
