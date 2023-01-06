# Garden-path-sentences-entity-recognition
This quick exercise utilise the python library "spaCy" to perform entity recognition on a group of garden path sentences. 

# What the program does 
* The program automatically imports the spaCy library and load the model 
* The user must add the garden path sentences to the gardenpathSentences list. 
* The program iterates to the list and prints each sentence along with the identified entities. 

# Docker instructions
* Build the image using: `docker build -t t37-app .`
* Run the image using: `docker run -it --rm t37-app`
