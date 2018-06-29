__author__ = 'Cq'
"""
    构建XML文档
"""
import csv
from xml.etree.ElementTree import Element, ElementTree
from e2 import pretty

def csvToXml(fname):
    with open(fname, 'rU', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = reader.__next__()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    pretty(root)
    return ElementTree(root)

et = csvToXml('demo.csv')
et.write('demo_copy.xml')
