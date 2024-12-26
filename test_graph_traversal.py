import unittest
from dfs_bfs import dfs_1, dfs_2, bfs, dfs_paths

class TestGraphTraversal(unittest.TestCase):
    def setUp(self):
        """Set up test graph before each test"""
        self.graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }

    def test_dfs_1(self):
        """Test iterative DFS implementation"""
        # Test from different starting points
        self.assertEqual(len(dfs_1(self.graph, 'A')), 6)  # Should visit all nodes
        self.assertEqual(len(dfs_1(self.graph, 'F')), 6)  # Should visit all nodes
        
        # Test with single-node graph
        single_node = {'A': set()}
        self.assertEqual(dfs_1(single_node, 'A'), {'A'})

    def test_dfs_2(self):
        """Test recursive DFS implementation"""
        # Test from different starting points
        self.assertEqual(len(dfs_2(self.graph, 'A')), 6)  # Should visit all nodes
        self.assertEqual(len(dfs_2(self.graph, 'F')), 6)  # Should visit all nodes
        
        # Compare with iterative implementation
        self.assertEqual(len(dfs_1(self.graph, 'A')), len(dfs_2(self.graph, 'A')))

    def test_bfs(self):
        """Test BFS implementation"""
        # Test from different starting points
        self.assertEqual(len(bfs(self.graph, 'A')), 6)  # Should visit all nodes
        self.assertEqual(len(bfs(self.graph, 'F')), 6)  # Should visit all nodes
        
        # Test order of visited nodes from 'A'
        visited = list(bfs(self.graph, 'A'))
        # First level neighbors should be visited before second level
        self.assertTrue(visited.index('B') < visited.index('D'))
        self.assertTrue(visited.index('C') < visited.index('F'))

    def test_dfs_paths(self):
        """Test path finding using DFS"""
        # Test path exists
        paths = list(dfs_paths(self.graph, 'A', 'F'))
        self.assertTrue(len(paths) > 0)
        
        # Verify path validity
        for path in paths:
            self.assertEqual(path[0], 'A')  # Start node
            self.assertEqual(path[-1], 'F')  # End node
            # Verify each step in path is valid
            for i in range(len(path)-1):
                self.assertIn(path[i+1], self.graph[path[i]])

    def test_edge_cases(self):
        """Test edge cases and error handling"""
        # Test with empty graph
        empty_graph = {}
        with self.assertRaises(ValueError):
            dfs_1(empty_graph, 'A')
        
        # Test with non-existent start node
        with self.assertRaises(ValueError):
            dfs_1(self.graph, 'X')
        
        # Test with disconnected graph
        disconnected = {
            'A': {'B'},
            'B': {'A'},
            'C': {'D'},
            'D': {'C'}
        }
        self.assertEqual(len(dfs_1(disconnected, 'A')), 2)  # Should only visit A and B

if __name__ == '__main__':
    unittest.main()