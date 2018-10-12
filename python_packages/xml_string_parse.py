import xml.dom.minidom
import os

xml_string = """<?xml version="1.0"?>
<launch>
  <basedir path="/Users/LuQiang/Dropbox/Courses/Leetcode-Practice/python_packages" />
  <seed value="1234" />
  <copy file="example.net.xml" />
  <copy file="routes.rou.xml" />
  <copy file="sumo.sumo.cfg" type="config" />
</launch>
"""

print(xml_string)

p = xml.dom.minidom.parseString(xml_string)
print(p)
print(dir(p))
print("tag name:", p.documentElement.tagName)
launch_node = p.documentElement
basedir_nodes = [x for x in launch_node.getElementsByTagName("basedir") if x.parentNode==launch_node]
basedir = basedir_nodes[0].getAttribute("path")
print("basedir nodes:", basedir_nodes, "basedir:", basedir)
print("path:", p.documentElement.getElementsByTagName("basedir")[0].getAttribute("path"))
print("seed:", launch_node.getElementsByTagName("seed")[0].getAttribute("value"))

copy_nodes = [x for x in launch_node.getElementsByTagName("copy") if x.parentNode == launch_node]
print(copy_nodes)

print("copy_nodes[0] has file attribute?", copy_nodes[0].hasAttribute("file"))

file_src_name = copy_nodes[0].getAttribute("file")
file_src_path = os.path.join(basedir, file_src_name)
print("file_src_path:", file_src_path)
# read file content
file_handle = open(file_src_path, 'rb')
file_contents = file_handle.read()
file_handle.close()
print(file_contents)

print()
