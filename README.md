# eCom-Chatbot-Data-pipeline
**eCom-Chatbot-Data-pipeline** is a scalable, robust data warehousing solution designed to handle large-scale e-commerce data, with a focus on Amazon's user reviews and product metadata. This project aims to streamline the extraction, transformation, and loading (ETL) of vast datasets into a structured, query-optimized data warehouse. By integrating advanced data modeling techniques, EcomDataVault helps in generating valuable insights for decision-making in e-commerce, such as customer preferences, product performance, and market trends.

## Key Features:

- **Efficient handling of large datasets** with millions of records.
- **Support for complex data relationships** (e.g., user reviews, product metadata).
- **Optimized for scalability and high performance**, ensuring fast query times and data retrieval.
- **Built-in data quality and integrity checks** to maintain accurate and consistent data.

---

## Setting Up Your Development Environment
For an efficient development experience, please follow these two essential steps:
### 1. Install the Virtual Environment
First, create an isolated environment to house your project dependencies. Execute the following commands:

```bash
# For Windows
python -m venv venv
# For macOS and Linux
python3 -m venv venv
```

### 2. Install All Required Libraries
Next, activate your virtual environment and install the necessary libraries in one swift command:

```bash
# For Windows
.\venv\Scripts\activate
# For macOS and Linux
source venv/bin/activate
# Install all dependencies
pip install -r requirements.txt
```

### 3. Storing API keys
To securely store your API keys and other sensitive information, you should create a `.env` file. 
Follow these steps:

```bash
# In the root directory of your project, create a new file named `.env`:
touch .env
```
```bash
#Open the `.env` file in your favorite text editor and add your API keys in the following format:
GROQ_API_KEY=<your-api-key-here>
```
