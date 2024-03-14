#######################################################################################################################
# Author: Nick Vovk                                                                                         #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (CaseOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the CaseOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from CaseOwnPeer2PeerNode import CaseOwnPeer2PeerNode

# local
node_1 = CaseOwnPeer2PeerNode("127.0.0.1", 8001)  # , 'first_1w')
# for Linux remote, random ID
node_2 = CaseOwnPeer2PeerNode("0.0.0.0", 8886)  # , 'secnd_2w')
node_3 = CaseOwnPeer2PeerNode("0.0.0.0", 8889)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()

time.sleep(1)

debug = False
node_1.debug = debug
node_2.debug = debug
node_3.debug = debug


node_1.connect_with_node('0.0.0.0', 8889)
node_2.connect_with_node('127.0.0.1', 8001)
node_3.connect_with_node('0.0.0.0', 8886)

time.sleep(2)

node_1.send_to_nodes("message: Hi there!")
node_2.send_to_nodes({ "name" : "Maurice", "number" : 11, "list": 0 })

time.sleep(5)

print("press enter to stop")
input()
print("node 1 is stopping..")
node_1.stop()

time.sleep(10)

node_2.send_to_nodes("message: Hi there node 2!")
node_2.send_to_nodes("message: Hi there node 2!")
node_2.send_to_nodes("message: Hi there node 2!")
node_3.send_to_nodes("message: Hi there node 2!")
node_3.send_to_nodes("message: Hi there node 2!")
node_3.send_to_nodes("message: Hi there node 2!")

time.sleep(5)

node_1.stop()
node_2.stop()
node_3.stop()
print('end test')
