import rcply
from rcply.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
node = Node.create_subscription(Int16, "countup", cb, 10)
rcply.spin(node)
