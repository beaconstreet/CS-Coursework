"""
CS3C, Assignment #10, The Maximum Flow Problem - Test
Matthew Heitman

Unittest for Assignment10
"""
from assignment10 import *
from graph10 import *
from graph10_test import *
import unittest

class FlowGraphTestCase(unittest.TestCase):

    def testTwoVerticesOneEdge(self):
        # test/verify the max flow between two vertices that have a single edge between them
        graph = FlowGraph("single edge", "ab", [("a", "b", 3)])
        actual_mf = graph.max_flow("a", "b")
        expected_mf = {("a", "b", 3)}
        self.assertSetEqual(actual_mf, expected_mf)

    def testSpecSampleUsage(self):
        # test/verify the max flow of the example from Sample usage
        graph = FlowGraph("graph from sample usage", "abcd", [
            ("a", "b", 3),
            ("a", "c", 2),
            ("b", "d", 2),
            ("c", "d", 3),
            ("b", "c", 5),
        ])
        actual_mf = graph.max_flow("a", "d")

        expected_mf = {
            ("a", "b", 3),
            ("b", "d", 2),
            ("a", "c", 2),
            ("c", "d", 3),
            ("b", "c", 1),
        }

        self.assertSetEqual(actual_mf, expected_mf)

    def testMaxFlowProblemReading(self):
        # test/verify the max flow of the example described in The Maximum Flow Problem
        graph = FlowGraph("graph from sample usage", "sabcdt", [
            ("s", "a", 3),
            ("s", "b", 2),
            ("a", "b", 1),
            ("a", "d", 4),
            ("b", "d", 2),
            ("a", "c", 3),
            ("c", "t", 2),
            ("d", "t", 3),
        ])
        actual_mf = graph.max_flow("s", "t")

        expected_mf = {
            ("s", "a", 3),
            ("s", "b", 2),
            ("a", "d", 1),
            ("b", "d", 2),
            ("a", "c", 2),
            ("c", "t", 2),
            ("d", "t", 3),
        }

        self.assertSetEqual(actual_mf, expected_mf)

    def testFoundMaxFlowProblem(self):
        # test/verify the max flow of one other flow network that you create yourself or find online
        # Got this from https://www.geeksforgeeks.org/dsa/ford-fulkerson-algorithm-for-maximum-flow-problem/
        graph = FlowGraph("graph from g2g", "012345", [
            ("0", "1", 16),
            ("0", "2", 13),
            ("1", "2", 10),
            ("2", "1", 4),
            ("1", "3", 12),
            ("3", "2", 9),
            ("2", "4", 14),
            ("4", "3", 7),
            ("3", "5", 20),
            ("4", "5", 4),
        ])
        actual_mf = graph.max_flow("0", "5")

        expected_mf = {
            ("0", "1", 12),
            ("0", "2", 11),
            ("1", "3", 12),
            ("2", "4", 11),
            ("4", "3", 7),
            ("3", "5", 19),
            ("4", "5", 4),
        }

        self.assertSetEqual(actual_mf, expected_mf)

    def testSourceEqualsSink(self):
        # test that ValueError is thrown if source and sink are same
        graph = FlowGraph("single edge", "ab", [("a", "b", 3)])
        with self.assertRaises(ValueError):
            graph.max_flow("a", "a")

    def testNoFlowBetweenVertices(self):
        # test that returns empty set if there's no flow between two vertices
        graph = FlowGraph("no flow", "abc", [("a", "b", 3)])
        actual_mf = graph.max_flow("a", "c")
        self.assertSetEqual(actual_mf, set())

    def testMaxFlowMultipleTimes(self):
        graph = FlowGraph("graph from sample usage", "abcd", [
            ("a", "b", 3),
            ("a", "c", 2),
            ("b", "d", 2),
            ("c", "d", 3),
            ("b", "c", 5),
        ])

        # First run
        actual_mf = graph.max_flow("a", "d")
        expected_mf = {
            ("a", "b", 3),
            ("b", "d", 2),
            ("a", "c", 2),
            ("c", "d", 3),
            ("b", "c", 1),
        }
        self.assertSetEqual(actual_mf, expected_mf)

        # Second run - same graph with diff source/sink
        actual_mf2 = graph.max_flow("b", "d")
        expected_mf2 = {
            ("b", "c", 3),
            ("c", "d", 3),
            ("b", "d", 2),
        }
        self.assertSetEqual(actual_mf2, expected_mf2)

del GraphTestCase