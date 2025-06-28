"""
This module is used to store the configurations.
"""

import re

# Keywords are not enabled by current version.
KEYWORDS = [
    "anthropic",
    "claude",
    "claude-1",
    "claude-2", 
    "claude-3",
    "claude-3-opus",
    "claude-3-sonnet",
    "claude-3-haiku",
    "claude-instant",
    "api key",
    "apikey",
    "artificial intelligence",
    "chain of thought",
    "chatbot",
    "competitor analysis",
    "content strategy",
    "conversational AI",
    "data analysis",
    "deep learning",
    "experiment",
    "key",
    "keyword clustering",
    "keyword research",
    "lab",
    "language model experimentation",
    "large language model",
    "llm",
    "long-tail keywords",
    "machine learning",
    "multi-agent",
    "multi-agent systems",
    "natural language processing",
    "personalized AI",
    "project",
    "rag",
    "retrieval-augmented generation",
    "search intent",
    "semantic search",
    "thoughts",
    "virtual assistant",
    "实验",
    "密钥",
    "测试",
    "语言模型",
]

LANGUAGES = [
    "Dotenv",
    "Text",
    "JavaScript",
    "Python",
    "TypeScript",
    "Dockerfile",
    "Markdown",
    '"Jupyter Notebook"',
    "Shell",
    "Java",
    "Go",
    "C%2B%2B",
    "PHP",
]

PATHS = [
    "path:.xml OR path:.json OR path:.properties OR path:.sql OR path:.txt OR path:.log OR path:.tmp OR path:.backup OR path:.bak OR path:.enc",
    "path:.yml OR path:.yaml OR path:.toml OR path:.ini OR path:.config OR path:.conf OR path:.cfg OR path:.env OR path:.envrc OR path:.prod",
    "path:.secret OR path:.private OR path:*.key",
]

# regex, have_many_results, result_too_lang
REGEX_LIST = [
    # Anthropic Claude API Key (current format)
    (re.compile(r"sk-ant-api03-[A-Za-z0-9_-]{95}"), True, True),
    # Alternative Anthropic key patterns
    (re.compile(r"sk-ant-[A-Za-z0-9_-]{48,}"), True, True),
    # Generic anthropic key pattern (for legacy or alternative formats)
    (re.compile(r"ant_[A-Za-z0-9_-]{40,}"), False, False),
]
