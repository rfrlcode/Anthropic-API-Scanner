"""
This module provides a function to check the validity of an Anthropic API key by making a test request
to a chosen model using the Anthropic client. It captures various exceptions and prints error details.
"""

import rich
from anthropic import Anthropic, APIStatusError, AuthenticationError, RateLimitError


def check_key(key, model="claude-3-haiku-20240307") -> str | None:
    """
    Check if the API key is valid.
    """
    try:
        client = Anthropic(api_key=key)

        message = client.messages.create(
            model=model,
            max_tokens=10,
            messages=[
                {
                    "role": "user",
                    "content": "Say yes"
                }
            ]
        )
        result = message.content[0].text if message.content else "No response"
        rich.print(f"🔑 [bold green]available key[/bold green]: [orange_red1]'{key}'[/orange_red1] ({result})\n")
        return "yes"
    except AuthenticationError as e:
        rich.print(f"[deep_sky_blue1]authentication_error ({e.status_code})[/deep_sky_blue1]: '{key[:10]}...{key[-10:]}'")
        return "authentication_error"
    except RateLimitError as e:
        rich.print(f"[deep_sky_blue1]rate_limit_error ({e.status_code})[/deep_sky_blue1]: '{key[:10]}...{key[-10:]}'")
        return "rate_limit_error"
    except APIStatusError as e:
        rich.print(f"[bold red]api_status_error ({e.status_code})[/bold red]: '{key[:10]}...{key[-10:]}'")
        return "api_status_error"
    except Exception as e:  # pylint: disable=broad-except
        rich.print(f"[bold red]{e}[/bold red]: '{key[:10]}...{key[-10:]}'")  # type: ignore
        return "Unknown Error"


if __name__ == "__main__":
    check_key("sk-ant-api03-12345")
