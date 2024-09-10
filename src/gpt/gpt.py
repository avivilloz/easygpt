from .setup import logging, create_dir
from time import sleep
from retry import retry

import g4f
from g4f.Provider import DDG, Pizzagpt, ChatgptFree, Free2GPT

providers = [
    (DDG, "gpt-4o-mini"),
    (Pizzagpt, "gpt-4o-mini"),
    (ChatgptFree, "gpt-4o-mini"),
    (Free2GPT, "llama-3.1-70b"),
]

DELAY = 3
LOG = logging.getLogger(__name__)
g4f.debug.logging = False


def get_provider(should_cycle: bool = False):
    global providers
    if should_cycle and len(providers) > 1:
        providers = providers[1:] + [providers[0]]
    return providers[0]


@retry(exceptions=Exception, tries=3)
def prompt_gpt(prompt: str, logs_dir: str) -> str:

    LOG_FILE = f"{logs_dir}/gpt.log"

    create_dir(logs_dir)

    logging.basicConfig(
        filename=LOG_FILE,
        filemode="a",
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    sleep(DELAY)
    LOG.info(f"Prompt: {prompt}")
    attempts = 0
    while attempts < len(providers):
        provider, model = get_provider(should_cycle=bool(attempts > 0))
        LOG.debug(f"Prompting {provider} | {model}")
        try:
            response = g4f.ChatCompletion.create(
                model=model,
                provider=provider,
                messages=[{"role": "user", "content": prompt}],
            )
            LOG.info(f"Response: {response}")
            return response
        except Exception as e:
            LOG.error(f"Error when trying to prompt {provider} | {model}: {e}")
            attempts += 1
    raise Exception("Failed to access gpt providers")


if __name__ == "__main__":
    prompt = "hey, how are you?"
    prompt_gpt(prompt=prompt)
