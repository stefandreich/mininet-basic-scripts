#!/usr/bin/python


"""Grouptable example

              Switch2 ----switch4
            /                       \     
h1 ---Switch1                        Switch5-----h2
            \                       /
              --------Switch3 ------



# static arp entry addition

h1 arp -s 192.168.1.2 00:00:00:00:00:02
h2 arp -s 192.168.1.1 00:00:00:00:00:01



ryu stuff:

ryu-manager group_table_lb.py

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', protocols='OpenFlow13')
        s5 = self.addSwitch('s5', protocols='OpenFlow13')

        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        
        self.addLink(s1,s2,1,1)
        self.addLink(s1,s3,2,1) 
        self.addLink(s1,h1,3,1)


        self.addLink(s3,s5,2,2)
        self.addLink(s4,s2,1,2)
        self.addLink(s4,s5,2,1)
    
        self.addLink(s5,h2,3,1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #sleep(5)
    #print("Topology is up, lets ping")
    #net.pingAll()
    CLI(net)
    net.stop()
