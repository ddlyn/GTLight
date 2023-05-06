# GTLight

GTLight is a graph RL method for traffic signal control. 


Firstly, traffic status information is encoded by MLP.
Then use graph transformer network to capture the spatial dependency. 
Finally, the signal timing scheme is obtained by a phase-timing optimization algorithm. 
The code follows similar structure [CoLight](https://github.com/wingsweihua/colight).