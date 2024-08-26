# HackerOne Reports Fetcher

This repository contains Python code for fetching HackerOne reports based on specific keywords. You can customize the keywords in the code, and the output will provide the endpoints where the reports can be accessed.

## Overview

The provided code allows you to search for HackerOne bug bounty reports that match your specified keywords. The results will include URLs to the reports that contain the keywords in their titles. This tool is useful for automating the search and retrieval of reports related to specific vulnerabilities or issues.

## Features

- Search for reports using multiple keywords.
- Fetch report URLs where the specified keywords are found in the title.
- Pagination support to handle large datasets.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hackerone-reports-fetcher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hackerone-reports-fetcher
   ```

3. Install the required dependencies:

   ```bash
   pip install requests
   ```

## Usage

1. Open the `fetch_reports.py` file in a text editor.

2. Modify the `keywords` array in the script to include the keywords you want to search for. For example:

   ```python
   keywords = ["idor", "open redirect", "cross site scripting"]
   ```

3. Run the script:

   ```bash
   python fetch_reports.py
   ```

4. The script will output the URLs of the reports that match the provided keywords. These URLs will be printed to the console and also saved to a file named `h1reports.txt`.

## Customization

- **Keywords**: Update the `keywords` list in the code to include any keywords relevant to your search.
- **Pagination**: Adjust the pagination settings if you need to fetch a different number of reports or start from a specific offset.

## Example

If you want to search for reports related to "IDOR" and "open redirect," update the `keywords` list as follows:

```python
keywords = ["idor", "open redirect"]
```

After running the script, it will print URLs of reports containing these keywords in their titles.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests if you have improvements or fixes. Contributions are welcome!

## Contact

For any questions or suggestions, please contact [yourname] at [your email address].

---

Replace placeholders like `yourusername` and `[yourname]` with your actual GitHub username and name. Also, ensure the `fetch_reports.py` file or any relevant code file name matches your actual script file name.