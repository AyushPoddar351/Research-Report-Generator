import importlib.metadata
packages = [
    "langgraph",
    "structlog",
    "ipykernel",
    "langchain_community",
    "langchain_core",
    "tavily-python",
    "wikipedia",
    "langchain-openai",
    "langchain-google-genai",
    "langchain-groq",
    ]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")