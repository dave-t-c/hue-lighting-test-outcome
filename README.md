# Change the color of a phillips hue light based on the result of tests

This script shows if maven tests have passed or failed by changing an RGB phillips hue light to either green or red.

You can modify the script to use whatever testting method that you want.
As long as the return code of the test command to the shell is 0 on success, and > 0 on failiure, then this should work straight away.

To connect the bridge to the program, press the button on the top of the bridge, then, within 30 seconds, run the program. This only needs to be done the first time you run the program.
