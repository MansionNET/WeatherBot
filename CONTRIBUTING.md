# Contributing to WeatherBot

First off, thank you for considering contributing to WeatherBot! It's people like you that make WeatherBot such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Include any error messages you received
- Note your Python version and operating system

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the proposed functionality
- Explain why this enhancement would be useful
- List any similar features in other IRC bots if you know of any

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure your code follows the existing code style
4. Update the documentation if needed
5. Issue the pull request

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create your configuration:
```bash
cp config.example.py config.py
```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Include docstrings for all functions and classes
- Comment complex logic
- Keep functions focused and modular

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Example:
```
Add weather alerts feature

- Implement severe weather warnings
- Add configuration options for alert thresholds
- Update documentation with new features

Fixes #123
```

## Testing

Currently, WeatherBot uses manual testing. When adding new features:

- Test your changes with multiple IRC servers
- Verify error handling works as expected
- Test edge cases (e.g., cities with special characters)
- Ensure rate limiting works correctly

## Documentation

- Update the README.md if you change or add functionality
- Add comments to explain complex code
- Update configuration examples if you add new options
- Document any new commands in the help system

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.
