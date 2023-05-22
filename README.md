# Progressive Dropout
<img src="./channels.png" width="1080px"></img>

The Progressive Dropout layer sets entire feature maps to zero, progressing from left to right. This strategy encourages a model to learn a set of maps that are sorted by importance, from left to right. This approach facilitates the transmission of partial feature representations over a network with minimal performance loss, thereby saving on communication costs.

# Ciation
```
@inproceedings{10.1145/3417313.3429379,
  author = {Samplawski, Colin and Huang, Jin and Ganesan, Deepak and Marlin, Benjamin M.},
  title = {Towards Objection Detection Under IoT Resource Constraints: Combining Partitioning, Slicing and Compression},
  year = {2020},
  isbn = {9781450381345},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3417313.3429379},
  doi = {10.1145/3417313.3429379},
  booktitle = {Proceedings of the 2nd International Workshop on Challenges in Artificial Intelligence and Machine Learning for Internet of Things},
  pages = {14–20},
  numpages = {7},
  keywords = {computation off-loading, edge computing, cloud computing, deep neural networks, object detection},
  location = {Virtual Event, Japan},
  series = {AIChallengeIoT '20}
}
```
