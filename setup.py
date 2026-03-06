import pylint
import flake8

# Install required tools
def install_tools():
    # Install pylint
    pylint.install()
    
    # Install flake8
    flake8.install()

# Run linter
def run_linter():
    # Run pylint
    pylint.run()
    
    # Run flake8
    flake8.run()

# Run the linter
install_tools()
run_linter()