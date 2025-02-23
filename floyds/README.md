## 🚀 Floyd-Warshall Algorithm in Python 

This repository implements the Floyd-Warshall Algorithm using both recursive and iterative approaches. The project includes performance tests and unit tests to compare the efficiency of both implementations.

## 📌 What is this repository for? 

* Version: 1.0
* Implements the Floyd-Warshall Algorithm for finding shortest paths between all pairs of nodes.
* Includes performance benchmarking and unit tests.

## 🛠️ How do I get set up?

* Install Dependencies

        pip install -r requirements.txt

## 🚀 Running the Scripts

1️⃣ Run the Floyd-Warshall Implementations

* Recursive Version

        python recursion/recursive_floyd.py

* Iterative Version

      python iterative/iterative_floyd.py

2️⃣ Run Performance Test

* To compare the execution times of both implementations:

        python tests/performance_test.py

3️⃣ Run Unit Tests

* To verify that both implementations work correctly:

        python tests/unittests.py

## 📂 Project Structure

floyd-warshall-python/
│── recursion/
│   ├── __init__.py
│   ├── recursive_floyd.py  # Recursive implementation
│── iterative/
│   ├── __init__.py
│   ├── iterative_floyd.py  # Iterative implementation
│── tests/
│   ├── __init__.py
│   ├── unittests.py  # Unit tests
│   ├── performance_test.py  # Performance benchmarking between recursive and iterative approach
│── requirements.txt  # Dependencies (if any)
│── README.md  # Project documentation

## 📖 Explanation of Floyd-Warshall Algorithm

The Floyd-Warshall Algorithm is used to find the shortest paths between all pairs of nodes in a weighted graph. It works by iteratively updating distances using the formula:

distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

Where:

i is the starting node,

j is the ending node,

k is an intermediate node.

## Recursive vs Iterative Approach

| Approach  | Pros                         | Cons                        |
|-----------|------------------------------|-----------------------------|
| Recursive | Elegant, uses function calls | Slower, higher memory usage |
| Iterative | More efficient, faster       | Uses explicit loops         |


## 📦 Requirements

Python 3.8+

No additional external libraries are required.

## ⚖️ License

This project is licensed under the MIT License.

## 📞 Contact

For any questions, reach out at:

📧 Email: m.a.siddique@liverpool.ac.uk/primesimon440@gmail.com

🌍 GitHub: prime97


