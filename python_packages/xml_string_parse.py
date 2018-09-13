import xml.dom.minidom

xml_string = """<?xml version="1.0"?>
<launch>
  <basedir path="/home/sommer/src/inet/examples/erlangen6" />
  <seed value="1234" />
  <copy file="net.net.xml" />
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
print("basedir nodes:", basedir_nodes)
print("path:", p.documentElement.getElementsByTagName("basedir")[0].getAttribute("path"))
print("seed:", launch_node.getElementsByTagName("seed")[0].getAttribute("value"))

copy_nodes = [x for x in launch_node.getElementsByTagName("copy") if x.parentNode == launch_node]
print(copy_nodes)
