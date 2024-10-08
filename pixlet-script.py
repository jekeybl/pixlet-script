import subprocess
import sys

def run_pixlet(command, file_name, community=False):
    """
    Runs the Pixlet tool with the given command and file name.
    
    Args:
        command: The Pixlet command to run.
        file_name: The name of the file to process.
        community: Set to True if using the Pixlet community command.
        
    Returns:
        True if the command was successful, False otherwise.
    """
    pixlet_cmd = ["pixlet", "community"] if community else ["pixlet"]
    pixlet_cmd += [command, file_name]
    
    # Print the full command being run
    print(f"Running command: {' '.join(pixlet_cmd)}")
    
    process = subprocess.run(pixlet_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Output the results of the command
    if process.stdout.strip():
        print(process.stdout)
    if process.stderr.strip():
        print(process.stderr)
    
    return process.returncode == 0

def main():
    """
    Takes a file name as an argument and runs the Pixlet or Pixlet community tools with various commands.
    """

    if len(sys.argv) != 2:
        print("Usage: pixlet-script.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]

    # List of Pixlet commands to run
    commands = [
        {"command": "format", "community": False},
        {"command": "lint", "community": False},
        {"command": "check", "community": False},
        {"command": "profile", "community": False},
        {"command": "validate-icons", "community": True},
        {"command": "load-app", "community": True},
        {"command": "validate-manifest", "community": True, "file_name": "manifest.yaml"}
    ]

    # Execute each command
    for cmd in commands:
        cmd_file = cmd.get("file_name", file_name)  # Use specified file_name if provided
        print(f"Running Pixlet command: {'community ' if cmd['community'] else ''}{cmd['command']} on file '{cmd_file}'")
        
        if not run_pixlet(cmd["command"], cmd_file, cmd["community"]):
            print(f"Error occurred")
            sys.exit(1)
        else:
            print(f"Successfully completed")

if __name__ == "__main__":
    main()
