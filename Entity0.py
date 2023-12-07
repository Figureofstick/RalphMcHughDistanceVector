"""this is the 0th entity; you need to modify this to
   implement the distance routing algorithm for this entity
"""

from Entity import Entity
from Packet import Packet


class Entity0(Entity):
    """Implementation of Entity0"""

    def __init__(self, sim, startvector):
        """Perform any necessary initialization in the constructor.
        startvector is the initial costs known to this node.
        startvector[0] is 0 (no cost to talk to yourself) and if
        startvector[n] is 999, then this node and 'n' are not connected"""
        super().__init__(sim)
        self.sim = sim
        
        # create NxN matrix for distance storage
        self.distance_table = []
        for _ in range(len(startvector)):
            self.distance_table.append([999] * len(startvector))

        # these are the base link costs to get to each nodes from 0
        self.distance_table[1][1] = 5
        self.distance_table[2][2] = 3
        self.distance_table[3][3] = 7


    def start(self):
        """This function is called once the simulator is fully
        ready handle packets. You can start to send packets in
        this function."""
        
        # make packets that have the link info for node0
        # this is the packet for node1
        # for ralph later, the min cost is just the base vector [0 (self cost for node 0), 5, 3, 7]
        mincost = [0 , 5, 3, 7]
        
        starterPacket = Packet(self.sim, 0, 1, [0, 5, 3, 7])
        self.sim.to_layer2(0, starterPacket)
        # packet for node2
        starterPacket = Packet(self.sim, 0, 2, [0 , 5, 3, 7])
        self.sim.to_layer2(0, starterPacket)
        # packet for node3
        starterPacket = Packet(self.sim, 0, 3, [0 , 5, 3, 7])
        self.sim.to_layer2(0, starterPacket)

    def update(self, pkt):
        """Handle updates when a packet is received.  Students will need to call
        NetworkSimulator.toLayer2() with new packets based upon what they
        send to update.  Be careful to construct the source and destination of
        the packet correctly.
        details."""

    def link_cost_change_handler(self, which_link, new_cost):
        """This function is called when the topology of the network
        has changed. `which_link` is the number of the neighbor
        for whom the cost has changed and `new_cost` is the new cost
        of that path"""

    def print_dt(self):
        """Called at simulation end (or for debugging) to print
        the distance table for this node."""

        print("           via")
        print(" D0 |   1   2   3")
        print("----+------------")
        for i in range(self.sim.nentities()):
            if i == 0:
                continue
            print(f"   {i}|", end='')
            for j in range(self.sim.nentities()):
                if j == 0:
                    continue

                print(f"{self.distance_table[i][j]:>5}", end='')
            print('')
