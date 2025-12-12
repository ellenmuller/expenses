# Expense Tracker

This is a Streamlit web application for tracking shared expenses between myself (Ellen) and my partner (Alex). The app connects to Google Sheets for data storage and provides an interface for viewing balances, transactions, and adding new expenses.

## Features

- 💰 **Balance Overview**: See who owes whom at a glance
- 📊 **Transaction History**: View and filter past expenses
- 💵 **Add Expenses**: Quickly log new shared expenses

## Prerequisites

- Python 3.13
- A Google account
- A Google Cloud Platform project with Google Sheets API enabled

## Setup

### 1. Create a Google Spreadsheet

Create a new Google Sheet with the following columns:

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| Date | Date | Format: DD/MM/YYYY |
| Description | Text | Description of the expense |
| Value | Number | Amount spent (e.g., 25.50) |
| Paid by | Text | Who paid (Ellen or Alex) |
| Paid for | Text | Who the expense was for (Ellen, Alex, or Both) |

### 2. Set up Google Sheets API Access

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the Google Sheets API for your project
4. Create a Service Account:
   - Go to "IAM & Admin" → "Service Accounts"
   - Create a new service account
   - Download the JSON key file
5. Share your Google Sheet with the service account email (found in the JSON file under `client_email`)

### 3. Configure Streamlit Secrets

Create a file at `.streamlit/secrets.toml` with your Google Sheets credentials:

```toml
[connections.gsheets]
spreadsheet = "YOUR_GOOGLE_SHEETS_URL"

# From your JSON key file
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

**Note**: The `.streamlit/secrets.toml` file is gitignored to keep your credentials secure.

**Another note**: More detailed instructions can be found in the [Streamlit docs](https://docs.streamlit.io/develop/tutorials/databases/private-gsheet)!

### 4. Install Dependencies

If you don't have poetry yet, first brew install:

```bash
brew install poetry
```

After which you can run:

```bash
poetry install
```

## Running the App

```bash
poetry run streamlit run expenses.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage

### Balance Page
- View the current balance between Ellen and Alex
- See who owes whom and the total amount

### Transactions Page
- Browse all recorded transactions
- Filter by who paid and who the expense was for

### Add Expense Page
- Log a new expense with:
  - Description (e.g., "Cinema tickets")
  - Amount
  - Who paid
  - Who the expense was for (Both, Ellen, or Alex)

## Project Structure

```
expenses/
├── expenses.py              # Main app entry point
├── pages/
│   ├── balance.py          # Balance overview page
│   ├── transactions.py     # Transaction history page
│   └── add_expense.py      # Add new expense page
├── utils/
│   ├── sheets.py           # Google Sheets connection
│   ├── debt.py             # Balance calculation logic
│   └── transactions.py     # Transaction filtering logic
├── .streamlit/
│   └── secrets.toml        # Configuration (not in git)
└── pyproject.toml          # Project dependencies
```

## How It Works

The app calculates the balance by:
1. Summing what each person has paid
2. Calculating what each person has spent (including half of "Both" expenses)
3. Computing the difference to determine who owes whom

## Security Note

Never commit your `.streamlit/secrets.toml` file to version control. It contains sensitive credentials and is already included in `.gitignore`.
