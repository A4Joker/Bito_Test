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
        """Test iterative DFS"""
        result = dfs_1(self.graph, 'A')
        self.assertEqual(len(result), 6)  # Should visit all nodes
        self.assertTrue(all(node in result for node in 'ABCDEF'))
    
    def test_dfs_2(self):
        """Test recursive DFS"""
        result = dfs_2(self.graph, 'A', set())
        self.assertEqual(len(result), 6)
        self.assertTrue(all(node in result for node in 'ABCDEF'))
    
    def test_bfs(self):
        """Test BFS traversal"""
        result = bfs(self.graph, 'A')
        self.assertEqual(len(result), 6)
        self.assertTrue(all(node in result for node in 'ABCDEF'))
        
    def test_dfs_paths(self):
        """Test path finding using DFS"""
        paths = list(dfs_paths(self.graph, 'A', 'F'))
        self.assertTrue(len(paths) > 0)
        for path in paths:
            self.assertEqual(path[0], 'A')  # Start node
            self.assertEqual(path[-1], 'F')  # End node
    
    def test_invalid_start_node(self):
        """Test with invalid start node"""
        with self.assertRaises(ValueError):
            dfs_1(self.graph, 'X')
    
    def test_empty_graph(self):
        """Test with empty graph"""
        with self.assertRaises(ValueError):
            dfs_1({}, 'A')

if __name__ == '__main__':
    unittest.main()