'''
Created on Dec 29, 2018

@author: Boyuan Zhang
'''

xml_string = """<?xml version="1.0" encoding="UTF-8"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""

import xml.etree.ElementTree as etree


def get_attr_number(node):
    
    # loop recursively each tag element
    for elem in node.iter():
        print(elem)


if __name__ == '__main__':
    # sys.stdin.readline()
    # xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml_string))
    root = tree.getroot()
    get_attr_number(root)



