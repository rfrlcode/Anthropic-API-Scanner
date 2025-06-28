# Anthropic-API-Scanner

This tool scans GitHub for available Anthropic API Keys.

![Result Demo 1](pics/demo.png)

> [!NOTE]
> As of `August 21, 2024`, GitHub has enabled push protection to prevent API key leakage, which could significantly impact this repository.

> [!NOTE]
> As of `March 11, 2024`, secret scanning and push protection will be enabled by default for all new user-owned public repositories that you create.
> Check this announcement [here](https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository).

> [!WARNING]
> **⚠️ DISCLAIMER**
>
> THIS PROJECT IS ONLY FOR ***SECURITY RESEARCH*** AND REMINDS OTHERS TO PROTECT THEIR PROPERTY, DO NOT USE IT ILLEGALLY!!
>
> The project authors are not responsible for any consequences resulting from misuse.

## Keeping Your API Key Safe

It's important to keep it safe to prevent unauthorized access. Here are some useful resources:

- [Anthropic API Key Management](https://docs.anthropic.com/claude/docs/getting-access-to-claude)
- [Anthropic Security Best Practices](https://support.anthropic.com/en/articles/8114494-how-can-i-access-the-anthropic-api)
- [API Key Security Guidelines](https://docs.anthropic.com/claude/docs/api-keys)

## Prerequisites

This project has been tested and works perfectly on macOS, Windows and WSL2 (see [Run Linux GUI apps on the Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps))

Ensure you have the following installed on your system:

- Google Chrome
- Python3

## Installation

1. Clone the repository:

    ```bash
    https://github.com/rfrlcode/Anthropic-API-Scanner

    cd Anthropic-API-Scanner
    ```

2. Install required pypi packages

    ```bash
    pip install selenium tqdm anthropic rich
    ```

## Usage

1. Run the main script:

    ```bash
    python3 src/main.py
    ```

2. You will be prompted to log in to your GitHub account in the browser. Please do so.

That's it! The script will now scan GitHub for available Anthropic API Keys.

## Command Line Arguments

The script supports several command line arguments for customization:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--from-iter` | Start scanning from a specific iteration | `None` |
| `--debug` | Enable debug mode for detailed logging | `False` |
| `-ceko, --check-existed-keys-only` | Only check existing keys in the database | `False` |
| `-k, --keywords` | Specify a list of search keywords | Default keyword list |
| `-l, --languages` | Specify a list of programming languages to search | Default language list |

Examples:

```bash
# Start scanning from iteration 100
python3 src/main.py --from-iter 100

# Only check existing keys
python3 src/main.py --check-existed-keys-only

# Use custom keywords and languages
python3 src/main.py -k "anthropic" "claude" -l python javascript
```

## Results

The results are stored in the `anthropic_github.db` SQLite database, which is created in the same directory as the script.

You can view the contents of this database using any SQLite database browser of your choice.

<figure>
  <img
  src="pics/demo2.png"
  alt="Running Demo">
  <p align="center">
    Running Demo
  </p>
</figure>

<figure>
  <img
  src="pics/db.png"
  alt="Result in DB">
  <p align="center">
    Result stored in SQLite (different API Key status)
  </p>
</figure>

## FAQ

**Q: Why are you using Selenium instead of the GitHub Search API?**

A: The official GitHub search API does not support regex search. Only web-based search does.

**Q: Why are you limiting the programming language in the search instead of searching all languages?**

A: The web-based search only provides the first 5 pages of results. There are many API keys available. By limiting the language, we can break down the search results and obtain more keys.

**Q: Why don't you use multithreading?**

A: Because GitHub searches and Anthropic API are rate-limited. Using multithreading does not significantly increase efficiency.

**Q: Why is the API Key provided in your repository not working?**

A: The screenshots in this repo demonstrate the tool's ability to scan for available API keys. However, these keys may expire within hours or days. Please use the tool to scan for your own keys instead of relying on the provided examples.

**Q: What's the push protection?**

A: see picture.

<p align="center">
    <kbd><img src="pics/warning1.png" alt="GitHub Push Protection" width="400"> </kbd>
</p>
