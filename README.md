# GPT4Free Wrapper

A robust GPT interface with multiple providers, automatic cycling, and error handling for reliable AI-powered text generation.

## Description:

This package provides a flexible and resilient interface for interacting with various GPT models through multiple providers. It offers the following key features:

- Multiple Provider Support: Integrates with several GPT providers allowing for diverse model access.
- Automatic Provider Cycling: If one provider fails, the system automatically cycles to the next available provider, ensuring continuous operation.
- Robust Error Handling: Implements retry logic to handle exceptions, improving reliability in unstable network conditions or when providers are temporarily unavailable.
- Configurable Delay: Includes a customizable delay between requests to respect rate limits and prevent overloading providers.
- Comprehensive Logging: Detailed logging of all operations, including prompts, responses, and errors, for easy debugging and monitoring.
- Easy-to-Use Interface: Provides a simple prompt_gpt function that handles all the complexity of provider selection, error handling, and retries.
- Customizable Provider List: Allows easy addition or removal of providers to suit specific needs or adapt to changes in provider availability.

This package is ideal for developers and researchers who need a reliable way to interact with GPT models, especially in scenarios where a single provider might not always be available or sufficient. It's particularly useful for applications that require high uptime and consistent access to AI-powered text generation capabilities.

## How to install:

Run the following command in your python venv:

```sh
pip install git+https://github.com/avivilloz/g4f_wrapper.git@main#egg=g4f_wrapper
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/g4f_wrapper.git@main#egg=g4f_wrapper
```

And run the following command:

```sh
pip install -r requirements.txt
```

## How to use:

```python
from g4f_wrapper import prompt_gpt

prompt = "hello, how are you?
response = prompt_gpt(prompt=prompt)
print(response)
```