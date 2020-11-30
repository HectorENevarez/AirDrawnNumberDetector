# Air Draw Number Detector
Air Draw Number Detector is a tool that allows you to draw any figure you'd like using your webcam/camera. It also has an additional feature that will guess the number you drew. You can toggle this feature on or off based on your goals with this tool

## Breaking down the files
#### AirDraw.py
This file contains the portion of the code that allows the user to draw using their webcam. The tool uses the Lucas-Kanade Optical Flow algorithm in order to detect movement. The user will specify a given point that it wants to start at, and using the agorithm, based on the movement of that starting point it will track that same point. We then draw a line connecting all of the movements and then a image is able to be seen. There is a 10 second timer which limits the drawing time for a user. If they would like this changed, it is possible to change the duration of the while loop in this file to a larger number or to implement an infinite loop. The escape key is used to exit the drawing mode.

#### DrawModel.py
This file contains the code that will save the model that predicts the number drawn. It implements a simple neural network that classifies different numbers trained on the MNIST dataset. The model is then saved in the working directory so that it can be implemented, if the user specifies, with the Air draw.

#### draw.py
This is the main file that connects the two previous files. It uses an argument parser to identify whether the user would like to implement the Number Detector on their drawn image. It then prints out on the command line which number the model guessed

## Using the software<br>

The software was made with the following dependencies:

- Python 3.8
- Tensorflow 2.3
- Numpy 1.18
- OpenCV 4.4

The steps for using the tool are:
1. Download the correct depenencies
2. Download the repo from github
3. Run Draw_Model.py in order to get the model
4. Run draw.py and specify whether you want to have the model guess your number
  - To toggle this feature specify 
  	```bash
    python draw.py --predictnumber True
    ```
   
