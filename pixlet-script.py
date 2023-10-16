import subprocess
import sys

def run_pixlet(community, command, file_name):
  """Runs the Pixlet tool with the given command and file name.
  Args:
    community: The Pixlet community command is to be used if set to "community", otherwise pass None.
    command: The Pixlet command to run.
    file_name: The name of the file to process.
  Returns:
    True if the command was successful, False otherwise.
  """

  if community == None:
    process = subprocess.run(["pixlet", command, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  else:
    process = subprocess.run(["pixlet", "community", command, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  if process.stdout.strip():
    print(f"{process.stdout}")
  return False if process.returncode != 0 else True

def main():
  """Takes a file name as an argument and runs the Pixlet or Pixlet community tools with various commands."""

  if len(sys.argv) != 2:
    print("Usage: pixlet-script.py <file_name>")
    sys.exit(1)

  file_name = sys.argv[1]

  # Run the Pixlet "format" command.
  print("pixlet format...")
  if not run_pixlet(None, "format", file_name):
    sys.exit(1)

  # Run the Pixlet community "spell-check" command.
  print("pixlet community spell-check...")
  if not run_pixlet("community", "spell-check", file_name):
    sys.exit(1)

  # Run the Pixlet "lint" command.
  print("pixlet lint...")
  if not run_pixlet(None, "lint", file_name):
    sys.exit(1)

 # Run the Pixlet community "validate-icons" command.
  print("pixlet community validate-icons...")
  if not run_pixlet("community", "validate-icons", file_name):
    sys.exit(1)

  # Run the Pixlet "check" command.
  print("pixlet check...")
  if not run_pixlet(None, "check", file_name):
    sys.exit(1)

  # Run the Pixlet "profile" command.
  print("pixlet profile...")
  if not run_pixlet(None, "profile", file_name):
    sys.exit(1)

# Run the Pixlet community "load-app" command.
  print("pixlet community load-app...")
  if not run_pixlet("community", "load-app", file_name):
    sys.exit(1)

# Run the Pixlet community "vvalidate-manifest" command.
  print("pixlet community validate-manifest...")
  if not run_pixlet("community", "validate-manifest", "manifest.yaml"):
    sys.exit(1)

if __name__ == "__main__":
  main()
