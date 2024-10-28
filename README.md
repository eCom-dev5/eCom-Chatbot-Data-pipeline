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

### 3. Storing API keys and other secret keys
To securely store your API keys and other sensitive information, you should create a `.env` file. 
Follow these steps:

```bash
# In the root directory of your project, create a new file named `.env`:
touch .env
```
```bash
#Open the `.env` file in your favorite text editor and add your API keys in the following format:
API_KEY=<your-api-key-here>
```
Cover the following in your .env file: DB_USER, DB_PASS, DB_NAME, INSTANCE_CONNECTION_NAME, GOOGLE_APPLICATION_CREDENTIALS, GCS_BUCKET_NAME


### 4. Generating a GCP JSON Connection File
To generate a JSON connection file for Google Cloud Platform (GCP), follow these steps:
1. **Access Credentials**:
   - Navigate to **Credentials** in the Google Cloud Console.
2. **Create a Service Account**:
   - Click on **Create Credentials** and select **Service Account**.
3. **Assign a Role**:
   - Choose the **Viewer** role for the Service Account, then click **Done**.
4. **Generate JSON Key**:
   - Locate your newly created Service Account.
   - Click on **Keys**.
   - Select **Add Key**, then choose **JSON**.
   - Save the generated JSON file securely.
5. **Store the JSON File**:
   - Place the JSON file in the main directory of your project.




