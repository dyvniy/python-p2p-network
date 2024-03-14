#######################################################################################################################
# Author: Nick Vovk                                                                                             #
# Version: 0.2 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# CaseOwnPeer2PeerNode is an example how to switch incoming requests        #
# 10/03/2024: created
#######################################################################################################################
from p2pnetwork.node import Node
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
import pickle
import zlib

class CaseOwnPeer2PeerNode(MyOwnPeer2PeerNode):

    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=100):
        super(CaseOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)
        print("MyPeer2PeerNode: Started")

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        # super(CaseOwnPeer2PeerNode, self).outbound_node_connected(node)
        pass
        
    def inbound_node_connected(self, node):
        # super(CaseOwnPeer2PeerNode, self).inbound_node_connected(node)
        pass
        
    def inbound_node_disconnected(self, node):
        # super(CaseOwnPeer2PeerNode, self).inbound_node_disconnected(node)
        pass
        
    def outbound_node_disconnected(self, node):
        # super(CaseOwnPeer2PeerNode, self).outbound_node_disconnected(node)
        pass
        
    def node_disconnect_with_outbound_node(self, node):
        # super(CaseOwnPeer2PeerNode, self).node_disconnect_with_outbound_node(node)
        pass
        
    def node_request_to_stop(self):
        # super(CaseOwnPeer2PeerNode, self).node_request_to_stop()
        pass

    def node_message(self, node, data):
        super(CaseOwnPeer2PeerNode, self).node_message(node, data)
        # self.id + " - " + node.id + ": " + str(data)
        if isinstance(data, str):
            return
        if isinstance(data, dict):
            if 'list' in data:
                self.send_list(data['list'])

    def send_list(self, params):
        print('- send list ' + str(params))
        # for node in self.all_nodes:
        #    print(node.host, node.port) 
        # self.print_connections()
        nodes = self.all_nodes
        nodelist = []
        for node in nodes:
            nodelist.append((node.host, node.port))
        # du = pickle.dumps(nodelist)
        # zi = zlib.compress(du)
        # self.send_to_nodes({"pickled_zipped": zi})
        self.send_to_nodes({"hello": nodelist})


