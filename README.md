# Minimum Effort Path Class Activity

This repository is the classroom activity for the Graphs Pt. 2 Roundtable in Unit 4.

## Learning Goals 
- Practice converting a list of edges into an adjacency list.
  
## One-Time Activity Setup

Follow these directions once, at the beginning of the activity:


1. Navigate to the folder where you wish to save activities. This could be your `projects` folder, or you may want to create a new folder for all of your activities.

   If you followed Ada's recommended file system structure, you can navigate to your projects folder with the following command:

   ```bash
   $ cd ~/Developer/projects
   ```

   Or, if you want to create a new folder for all of your activities:

   ```bash
   $ cd ~/Developer
   $ mkdir activities
   $ cd activities
   ```

   If you've already created an activities directory, you can navigate to it with the following command:

   ```bash
   $ cd ~/Developer/activities
   ```

2. In Github click on the "Fork" button to fork the repository to your Github account.  This will make a copy of the activity in your Github account. 

3. "Clone" the activity into your working folder. This command makes a new folder named for the activity repository, and then puts the activity into this new folder.

   ```bash
   $ git clone <clone_url_for_the_activity>
   ```

   The `<>` syntax indicates a placeholder. You should replace `<clone_url_for_the_activity>` with the actual URL you'd use to clone this repository. If you click the green "Code" button on the GitHub page for this repository, you'll see a URL that you can copy to your clipboard.
 
   Use `ls` to confirm there's a new activity folder

4. Move your location into this activity folder

   ```bash
   $ cd <repository_directory>
   ```

   The `<repository_directory>` placeholder should be replaced with the name of the activity folder. If you're not sure what the folder is named, remember that you can use `ls` to list the contents of your current location.

5. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

6. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:
   
   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this activity with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

   Not all activities will have dependencies, but there will still be an included `requirements.txt` file.

Summary of one-time activity setup:
- [ ] Fork the activity repository
- [ ] `cd` into your working folder, such as your `projects` or `activities` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the folder for the activity
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Activity Development Workflow

1. When working on this activity, always ensure that your virtual environment is activated:

   ```bash
   $ source venv/bin/activate
   ```

2. If you want to work on another project from the same terminal window, you should deactivate the virtual environment when you are done working on the activity:

   ```bash
   $ deactivate
   ```

## Task

Using the following steps to guide you, write pseudocode for how you would approach this problem. If time allows, implement your solution.

## General Steps to Solving Shortest Path Problems

1. Identify the graph representation given
    1. If needed, convert the representation to either adjacency dictionary or adjacency matrix (for looping through neighbors in the algorithm later)
2. Identify how you will traverse the graph
3. Identify the priority and details we need to keep track of (distance, cost, etc)
4. Set up distance dictionary (and/or visited set) and priority queue
5. Loop through queue
    1. Pop highest priority node off the queue
        1. Store current node in a variable
        2. Store priority (distance/cost) in a variable, if needed
    2. If there is a destination node
        1. Check if the current node is the destination node and return, if applicable
    3. Loop through current node’s neighbors
        1. Calculate the neighbor’s priority and extra details to keep track of
        2. Push the current node’s neighbor onto the priority queue
6. Return the desired result

## Examples

### Example #1
![Heights Example #1](images/example_1.png)

*Input:* heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]
<br>
*Output:* 2
<br>
*Explanation:* The route (highlighted in green) of [1, 3, 5, 3, 5] has a maximum absolute difference of 2 in consecutive cells.

Notice the route from [1, 2, 2, 2, 5] has a maximum absolute difference of 3, so it is not the optimal route in this case.

### Example #2
![Heights Example #2](images/example_2.png)
*Input:* heights = [
    [1, 2, 3],
    [3, 8, 4],
    [5, 3, 5]
]
<br>
*Output:* 1
<br>
*Explanation:* The route of [1, 2, 3, 4, 5] (highlighted in green) has a maximum absolute difference of 1 in consecutive cells, which is better than the route [1, 3, 5, 3, 5], which has a maximum absolute difference of 2.

### Example #3
![Heights Example #3](images/example_3.png)
*Input:* heights = [
    [1,2,1,1,1],
    [1,2,1,2,1],
    [1,2,1,2,1],
    [1,2,1,2,1],
    [1,1,1,2,1]
]
<br>
*Output:* 0
<br>
*Explanation:* The route requires `0` effort due to the fact that the path highlighted (all 1's) has a maximum absolute difference of 0 between cells.
  
## Running Tests
Use the tests provided in the `test_min_effort_path.py` file to verify that your code is working correctly. You can verify the tests are working in one of two ways:

1. Run `pytest` in the terminal (make sure you are in the venv!)
2. Set up the testing environment in the VSCode Testing Pane
   1. Click on the beaker icon and click `Configure Python Tests`
   2. Select `pytest` from the list that appears
   3. Select `tests` from the new list that appears.
3. Verify the tests show up in the Testing Pane.
4. Run the tests to make sure they are all passing!