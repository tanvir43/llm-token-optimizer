import tiktoken


def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    Count the number of tokens in a given text using the specified model's tokenizer.

    Args:
        text (str): The input text to tokenize.
        model (str): The model name for which to count tokens. Default is "gpt-3.5-turbo".

    Returns:
        int: The number of tokens in the input text.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except:
        # Fallback to the default encoding if the specified model is not found
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))