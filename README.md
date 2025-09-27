# COURSENAME
This is the repository for the LinkedIn Learning course `course-name`. The full course is available from [LinkedIn Learning][lil-course-url].

![course-name-alt-text][lil-thumbnail-url] 

## Requirements
- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

## Setup

1. **Clone this repo** (or download the files).
2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Set your OpenAI API key or place in .env file**:
    ```bash
    export OPENAI_API_KEY="your_api_key"      # macOS/Linux
    setx OPENAI_API_KEY "your_api_key"        # Windows PowerShell
    ```
