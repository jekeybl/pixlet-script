# pixlet-script
---

Once your Tidbyt app has been completed, there are a number of checks that should be performed using the Pixlet app before a PR is submitted.  This script is used to automatically run through all eight checks that ensure the app will work properly on the community server.

`Usage: python3 pixlet-script.py <file_name>`

As the script steps through each check, if there is an error returned, the script terminates and does not go to the next check until the error has been addressed.

In this script, various Pixlet commands are run, both for the common Pixlet tool itself and its community version.
Here is what happens in the code:

1. **Import libraries:** It starts by importing necessary libraries, namely `subprocess` (used for running system commands) and `sys` (used for working with Python program or script run-time environment).
2. **Define `run_pixlet` function:** This function is used to run the Pixlet tool (or its community version). It receives three arguments:
    - `community`: If this is set to "community", it uses the community version of Pixlet. If it's set to `None`, it uses the non-community version.
    - `command`: The Pixlet command to be executed.
    - `file_name`: The name of the file to be processed by Pixlet.    
    The function runs the Pixlet command using `subprocess.run`, capturing both the standard output and standard error. It prints the standard output if there is one, and returns `True` if the command was successful and `False` otherwise.
3. **Define `main` function:** This function takes a file name as an argument and runs various Pixlet commands using that file name.
    - It first checks whether a file name is provided. If not, it prints the usage message and exits with code 1.
    - It then runs a series of Pixlet and Pixlet community commands for the given file: "format", "spell-check", "lint", "validate-icons", "check", "profile", "load-app", and "validate-manifest". If any execution fails, the script exits with code 1.
4. **Script Execution:** If the script is run directly (not imported as a module), the `main` function is executed.
