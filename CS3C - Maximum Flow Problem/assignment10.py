"""
CS3C, Assignment #10, The Maximum Flow Problem
Matthew Heitman

Implementation of the Ford-Fulkerson algorithm for finding the maximum flow between a
pair of source and sink in a flow network.
"""
import math

from graph10 import *

class FlowEdge(Edge):

    def __init__(self, id_, src, dst, weight, flow=0):
        super().__init__(id_, src, dst, weight) # inherit Edge's attributes
        self.flow = flow
        self.reverse = None
        self.is_back_edge = False

    @property
    def capacity(self): # wrapped self.weight, call with self.capacity
        return self.weight

    @property
    def res_cap(self): # residual capacity
        return self.capacity - self.flow

    def is_usable(self):
        if self.res_cap > 0:
            return True
        else:
            return False


class FlowVertex(Vertex): # keep below FlowEdge
    EdgeClass = FlowEdge # override the class attribute to use FlowEdge instead

class FlowGraph(Graph):

    VertexClass = FlowVertex  # override class attribute to use FlowVertex

    def __init__(self, id_, vertices, edges):
        super().__init__(id_, vertices, edges)

    def add_edge(self, src, dst, weight=1):
        # Hopefully this is the correct approach, I couldn't figure out how to do this otherwise without
        # duplicating the logic in Graph.spf()

        src_v = self.vertices[src]
        dst_v = self.vertices[dst]

        # Checking "edge" case (ha, get it?) in case there's max flow problems with back edges in the graph
        # like in test #4
        edge_id = Edge.edge_id(src_v, dst_v)
        if edge_id in self.edges:
            self.edges[edge_id].weight = weight
            return

        # create the forward edge
        super().add_edge(src, dst, weight)
        forward_edge = self.edges[Edge.edge_id(src_v, dst_v)] # retrieve by id

        # create the back edge, zero'd weight which increases as flow is used
        super().add_edge(dst, src, weight=0)
        back_edge = self.edges[Edge.edge_id(dst_v, src_v)] # retrieve by id
        back_edge.is_back_edge = True

        # link the forward edge and back edge
        forward_edge.reverse = back_edge
        back_edge.reverse = forward_edge

    def max_flow(self, source, sink):
        """
        returns a set of tuples (src, dst, flow) that represents the max flow
        """

        # raise ValueError is source is same as sink
        if source == sink:
            raise ValueError("Source and sink can't be the same vertex")

        # Reset all flow to 0 so can be called multiple times
        for edge in self.edges.values():
            edge.flow = 0

        # Keep finding paths
        path, weight = self.spf(source, sink)
        while weight != math.inf:  # while capacity is finite...

            # Find the minimum residual capacity along the path
            min_res_cap = math.inf
            for i in range(len(path) - 1):
                src_v = self.vertices[path[i]]
                dst_v = self.vertices[path[i + 1]]
                edge = self.edges[Edge.edge_id(src_v, dst_v)]
                min_res_cap = min(min_res_cap, edge.res_cap)

            # Push flow along the path by the min_res_cap amount
            for i in range(len(path) - 1):
                src_v = self.vertices[path[i]]
                dst_v = self.vertices[path[i + 1]]
                edge = self.edges[Edge.edge_id(src_v, dst_v)]
                # Increase flow on forward edge
                edge.flow += min_res_cap
                # Increase capacity on back-edge (so can go backwards)
                edge.reverse.weight += min_res_cap

            # Get next path
            path, weight = self.spf(source, sink)

        # Build result set of (src, dst, flow) tuples
        result = set()

        # Only include edges that have flow > 0 and are forward edges
        for edge in self.edges.values():
            if edge.is_back_edge == False and edge.flow > 0:
                result.add((edge.src.id, edge.dst.id, edge.flow))

        return result
