# Contributing to Roommate CLI

Thank you for your interest in contributing to Roommate CLI! We welcome contributions from everyone.

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and what behavior you expected to see
- **Include screenshots or animated GIFs** if possible
- **Include your environment details**: OS, Python version, etc.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any alternatives** you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## 📝 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise

### Code Formatting

- Use 4 spaces for indentation
- Maximum line length: 100 characters (flexible for readability)
- Add blank lines to separate logical sections

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add conversation history feature

- Implement session storage
- Add history navigation commands
- Update documentation

Fixes #123
```

## 🧪 Testing

Before submitting a pull request:

1. Test your changes thoroughly
2. Ensure the CLI runs without errors
3. Test edge cases and error conditions
4. Verify the UI looks correct in different terminal sizes

## 📚 Documentation

- Update the README.md if you change functionality
- Add docstrings to new functions and classes
- Update comments if you change existing code
- Keep documentation clear and concise

## 🔄 Development Workflow

1. **Fork** the repository
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/YOUR-USERNAME/roommate-cli.git
   cd roommate-cli
   ```
3. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and commit them
   ```bash
   git add .
   git commit -m "Add your feature"
   ```
5. **Push** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request** from your fork to the main repository

## 💡 Development Tips

- Install dependencies in a virtual environment
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```
- Use descriptive branch names like `feature/add-history` or `fix/connection-error`
- Keep your fork synced with the upstream repository
- Write self-documenting code when possible

## 🤔 Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Our Standards

Examples of behavior that contributes to a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards others

### Unacceptable Behavior

- Harassment of any kind
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## 🎉 Recognition

Contributors will be recognized in the project documentation. Thank you for making Roommate CLI better!

---

Happy Contributing! 🚀
