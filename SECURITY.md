# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability within Roommate CLI, please send an email or open a GitHub issue. All security vulnerabilities will be promptly addressed.

**Please do not publicly disclose the issue until it has been addressed by the team.**

### What to Include in Your Report

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- **Initial Response**: We will acknowledge receipt of your vulnerability report within 48 hours.
- **Status Update**: We will provide a detailed response indicating the next steps within 7 days.
- **Resolution**: We aim to resolve critical security issues within 30 days.

## Security Best Practices for Users

When using Roommate CLI, please follow these security best practices:

1. **Protect Your API Password**: If using a private server with authentication, keep your `api_password.txt` file secure and never commit it to version control.

2. **Use HTTPS**: The application connects to the API over HTTPS by default. Never modify the code to use HTTP for production use.

3. **Keep Dependencies Updated**: Regularly update the dependencies by running:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

4. **Verify Source**: Only download Roommate CLI from the official GitHub repository.

5. **Review Code**: Before running, review the source code, especially if you've made modifications.

## Known Security Considerations

- **API Authentication**: The application stores API passwords in plain text in the configuration file. Consider using environment variables or a secure secret management system for production deployments.

- **Network Traffic**: All communication with the API server should be over HTTPS to prevent man-in-the-middle attacks.

- **Input Validation**: User inputs are sent directly to the API. Ensure your API server properly validates and sanitizes all inputs.

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find any similar problems
3. Prepare fixes for all supported versions
4. Release patched versions as soon as possible

## Comments on This Policy

If you have suggestions on how this policy could be improved, please submit a pull request or open an issue.

---

Thank you for helping keep Roommate CLI and its users safe!
