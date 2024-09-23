<div align="center">
  <h3 align="center">MSCS532 Assignment 5</h3>
</div>

<!-- CLONING THE REPOSITORY -->
## Cloning the Repository

To get a local copy of this repository, use the following commands:
```sh
# Clone the repository
git clone https://github.com/abhattarai28547/MSCS532_Assignment4.git

# Navigate into the project directory
cd MSCS532_Assignment4
```
<!-- Running the code-->
### Quicksort Implementation

To test the **Deterministic Quicksort** implementation, execute:
```sh
python deterministic_quicksort.py
```
This will run the deterministic algorithm on a sample array and output the sorted result.

To test the **Randomized Quicksort** implementation , execute:

```sh
python randomized_quicksort.py
```
This will run the randomized version of Quicksort on a sample array and output the sorted result

### Performance Comparison

To compare the performance of both Quicksort implementations, execute:
```sh
python comparison.py
```
This will run both deterministic and randomized Quicksort on arrays of varying sizes and distributions (random, sorted, reverse-sorted) and display the execution times.


<!-- CUSTOMIZATION -->
Customization
You can modify the array sizes or input data within the Python scripts for testing different scenarios:

`comparison.py`: Adjust the sizes array to test different input sizes for sorting algorithms. You can also change the array generation logic in the `generate_test_arrays()` function to customize input distributions.


 <!-- SUMMARY OF FINDINGS -->

 
### Summary of Findings
<div> 
  <li>
   **Deterministic Quicksort**: The deterministic version showed acceptable performance across various input types but exhibited worst-case behavior on reverse-sorted arrays, with time complexity reaching 𝑂(𝑛^2).
  </li> 
  <li>
    **Randomized Quicksort**: This version consistently outperformed the deterministic implementation by mitigating worst-case scenarios, achieving average-case time complexity of 𝑂(𝑛log𝑛) across all input types.
  </li>
  <li>
    **Merge Sort**: Similar to Quicksort, Merge Sort (also implemented using Python's `sorted()`) was highly efficient and had comparable performance to Timsort. As expected, it performed steadily across all input sizes and types due to its stable time complexity of 𝑂(𝑛log𝑛).
  </li>
  <li>**Results**: Randomized Quicksort performed better on reverse-sorted arrays, demonstrating the benefits of random pivot selection for balanced partitions.
  </li>
</div>

### Instructions:
<ol>
  <li>
    Clone the Repository: Use the provided Git commands to clone the repository and navigate into the project directory.
  </li> 
  <li>
    Run Scripts: Execute the provided Python scripts to test both versions of Quicksort and their performance comparison.
  </li> 
  <li>Customize: Modify the input arrays or task lists as needed to explore different test scenarios.
  </li> 
  <li>
    Review Findings: Refer to the summary of findings to understand the performance characteristics observed during the implementation and testing.
  </li>
</ol>

This `README.md` now includes detailed instructions for running the implementations, customizing them, and a summary of the findings.
