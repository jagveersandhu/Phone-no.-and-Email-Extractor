Phone Number and Email Address Extractor:
This Python script is designed to extract phone numbers and email addresses from a block of text. It is useful for quickly pulling out contact information from large text files, emails, documents, or web pages.

Features:
Phone Number Extraction: Identifies and extracts phone numbers from text, supporting various formats, including international numbers.
Email Address Extraction: Finds and extracts email addresses, handling common email formats and domains.
Customizable Patterns: Allows for easy modification of regex patterns to fit specific formats or regional variations.

How It Works:
The script uses regular expressions (regex) to search for patterns that match typical phone numbers and email addresses. Once found, these matches are printed or stored for further use.

Example Input:
Contact us at support@example.com or call 123-456-7890 for more information.

Example Output:
Emails found:
support@example.com

Phone numbers found:
123-456-7890

How to Use:
a) Clone the Repository:
git clone https://github.com/jagveersandhu/Phone-no.-and-Email-Extractor.git
cd Phone-no.-and-Email-Extractor
b) Run the Script:
python "Phone number and email address extractor.py"
c) Input Text:
The script will prompt you to enter or paste the text from which you want to extract phone numbers and email addresses.
d) View Results:
Extracted phone numbers and email addresses will be displayed in the terminal.

Customization:
You can customize the script to search for different formats by modifying the regular expressions used for phone numbers and email addresses.

Modify Regex Patterns:
Phone Number Pattern: Change the phoneRegex pattern to match different phone number formats.
Email Address Pattern: Adjust the emailRegex pattern to accommodate different or unusual email formats.

Contributing:
Contributions are welcome! If you have suggestions for improving the script or adding new features, feel free to fork this repository and submit a pull request.
