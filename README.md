# TempMail Verification Code Generator

This script allows you to generate a temporary email address, retrieve verification messages, and extract verification codes from those email received.

## Features

- Generate a new temporary email address.
- Retrieve verification messages for the generated email.
- Extract a verification code from the email's HTML content.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Files

- `token.txt`: Stores the temporary email token.
- `email.txt`: Stores the temporary email address.

## Usage

1. **Generate Email Address and Verification Code**

   Run the script:

   ```bash
   python tempmail.py
   ```

   The script will:
   - Prompt you to choose between generating a new email or using the existing one.
   - If you choose to generate a new email, it will request a new email address and save the token and email address.
   - If you choose to use the existing email or if a token is already available, it will use that email address.
   - Retrieve messages and extract the verification code.

2. **Configuration**

   The script saves and loads the token and email address from `token.txt` and `email.txt` respectively. Make sure these files are writable by the script.

## Error Handling

- The script handles errors by retrying after a short delay.
- Errors are printed to the console for debugging purposes.

## Notes

- The script is designed to extract only verification codes that are numerical and at least 6 digits long from the HTML content of emails. It will not handle or extract other types of information from the emails.
- Please ensure that the code is running behind when you request code on platform. If you accidentally stop the code. You need to run the code again & request new code.
- Ensure that your network connection is stable as the script relies on external API requests.
- The script runs continuously and starts a new thread for each cycle of email generation and message retrieval.

## License

This script is provided as-is. Feel free to use and modify it as needed.

---

For further information or issues, contact the author at `@rxxv`.
