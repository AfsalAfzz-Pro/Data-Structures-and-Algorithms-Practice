# Data-Structures-and-Algorithms-Practice

**Array**

*   **Definition:** A collection of elements of the same data type stored in contiguous memory locations.
*   **Common Operations:**
    *   Access (O(1))
    *   Search (O(n))
    *   Insertion (O(n))
    *   Deletion (O(n))
*   **Use Cases**
    *   Storing lists of items (student scores, product prices)
    *   Implementing other data structures (stacks, queues, heaps)
    *   Basic matrices in image processing
*   **Code Implementation (Example in Python):**

**Linked List**

*  **Definition:** A linear data structure where elements are stored in non-contiguous memory locations. Each element (node) contains data and a pointer to the next node in the sequence.
*  **Common Operations:**
    *   Insertion (Head/Tail): O(1) 
    *   Deletion (Head/Tail): O(1)
    *   Search: O(n)
    *   Traversal: O(n)
*  **Use Cases:**
    *   Implementing stacks and queues
    *   Representing song playlists or browser history (where order matters)
    *   Efficiently inserting/removing elements in dynamic memory scenarios

**Stack**

*  **Definition:** A Last-In, First-Out (LIFO) data structure. Think of a stack of plates.
*  **Common Operations:**
    *   Push (adding an element to the top): O(1)
    *   Pop (removing the top element): O(1)
    *   Peek (viewing the top element): O(1)
*  **Use Cases**
    *   Function call management in programming
    *   Undo/redo operations in software
    *   Backtracking (e.g., in maze-solving algorithms)

**Queue**

*  **Definition:** A First-In, First-Out (FIFO) data structure. Think of a waiting line at a store.
*  **Common Operations**
    *   Enqueue (adding an element to the rear): O(1)
    *   Dequeue (removing an element from the front): O(1)
    *   Front/Rear (viewing the front or rear element): O(1)
*  **Use Cases**
    *   Task scheduling (e.g., print jobs)
    *   Serving requests in a network
    *   Breadth-First Search (BFS) graph traversal 

**Hashtable (Hash Map)**

*  **Definition:** Uses a hash function to map keys to indices in an array (hash table). Ideal for fast lookups, insertions, and deletions.
*  **Common Operations:**
    *   Insert: Average O(1) 
    *   Search: Average O(1)
    *   Delete: Average O(1)
*  **Use Cases:**
    *   Implementing caches
    *   Storing username-password combinations
    *   Finding duplicate elements in an array

**Tree**

*  **Definition:** A hierarchical data structure where nodes have a parent-child relationship. There's a single root node, and each node can have zero or more children.
*  **Common Operations:**
    *   Insertion: O(log n) in balanced trees, O(n) in worst case  
    *   Search: O(log n)  in balanced trees, O(n) in worst case
    *   Traversal (Pre-order, In-order, Post-order): O(n) 
*  **Use Cases:**
    *   Representing hierarchical data (file systems, organization charts)
    *   Decision trees in machine learning
    *   Storing syntax trees in compilers

**Graph**

*  **Definition:** A collection of nodes (vertices) connected by edges. Edges can be directed or undirected.
*  **Common Operations:**
    *   Adding/removing nodes or edges: Varies based on implementation
    *   Traversal (Breadth-First Search, Depth-First Search): O(V + E) 
*  **Use Cases:**
    *   Representing networks (social networks, road maps)
    *   Pathfinding algorithms (GPS navigation)
    *   Modeling dependencies in projects

**Binary Tree**

*  **Definition:** A type of tree where each node has at most two children, referred to as the left child and right child.
*  **Common Operations:** (same as in 'Tree' section)
*  **Use Cases:**
    *   Binary Search Trees (see below)
    *   Heaps (see below)
    *   Expression parsing

**Binary Search Tree (BST)**

*  **Definition:** A binary tree with the key property: For every node, the value of all nodes in its left subtree is smaller, and the value of all nodes in its right subtree is larger.
*  **Common Operations:**
    *   Insertion: O(log n) on average
    *   Search: O(log n) on average
    *   Deletion: O(log n) on average
*  **Use Cases:**
    *   Fast lookup, insertion, and deletion of ordered data
    *   Implementing sets and maps

**Binary Heap**

*  **Definition:** A specialized tree-based data structure that satisfies the heap property.  
    *   **Min Heap:**  Parent node is always smaller than its children
    *   **Max Heap:**  Parent node is always larger than its children
*  **Common Operations**
    *   Insert: O(log n)
    *   Remove (root): O(log n)
    *   Peek (find min/max): O(1)
*  **Use Cases:**
    *   Implementing priority queues
    *   Heap Sort algorithm

**Priority Queue**

*  **Definition:** An abstract data type where each element has a priority. Elements with higher priority are dequeued before those with lower priority.
*  **Common Operations:**
    *   Insert with priority: O(log n) (due to heap)
    *   Remove highest priority element: O(log n) (due to heap)
    *   Change priority: O(log n) (due to heap)
*  **Use Cases:**
    *   Task scheduling (prioritizing urgent tasks)
    *   Dijkstra's shortest path algorithm
    *   Event simulations


