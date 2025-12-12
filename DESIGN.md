# Design Document: Expense Tracker

## Overview

This expense tracker is a Streamlit-based web application designed to manage shared expenses between two people (Ellen and Alex). The application uses Google Sheets as a backend database, providing a simple yet effective way to track who paid for what and calculate balances in real-time.

## Architecture

### Technology Stack

- **Frontend Framework**: Streamlit (v1.42.0+)
  - Chosen for its simplicity and because I have used it before
  - Makes it super easy to add basic widgets
  - Integrates seamlessly with Google Sheets

- **Data Storage**: Google Sheets
  - No database setup required
  - Easy manual editing if needed (which my partner does a lot when he exports his transactions from his bank)

- **Data Processing**: Pandas
  - Efficient data manipulation and filtering
  - Natural integration with Streamlit's dataframe display

- **API Integration**: st-gsheets-connection
  - Streamlit's official Google Sheets connector
  - Built-in caching mechanisms
  - Simplified authentication flow

### Application Structure

```
expenses/
├── expenses.py              # Main entry point and navigation
├── pages/                   # Streamlit pages (multi-page app)
│   ├── balance.py          # Balance overview
│   ├── transactions.py     # Transaction history with filters
│   └── add_expense.py      # Form to add new expenses
├── utils/                   # Business logic and utilities
│   ├── sheets.py           # Google Sheets connection wrapper
│   ├── debt.py             # Balance calculation logic
│   └── transactions.py     # Transaction filtering logic
└── .streamlit/
    └── secrets.toml        # Configuration and credentials
```

## Design Decisions

### 1. Multi-Page Architecture

**Choice**: Used Streamlit's native `st.navigation()` API for multi-page app structure.

**Rationale**: I want every page to do something different and it made it much easier to reason about the state of the app at any given time. 

### 2. Google Sheets as Database

**Choice**: Direct integration with Google Sheets instead of traditional database.

**Rationale**:
- No server infrastructure needed
- The database doesn't need to be that big because it's just for personal use
- Data can be viewed/edited directly in the spreadsheet if needed
- Easy backup and export capabilities

**Trade-offs**:
- Slower than traditional databases
- No complex query capabilities
- Requires internet connection

### 3. Balance Calculation Algorithm

**Implementation** (in `utils/debt.py`):

The balance calculation follows this logic:
1. Sum what each person has paid out
2. Calculate what each person has spent (their individual expenses + half of "Both" expenses)
3. Compute the net balance: `balance = paid - spent`
4. The person with positive balance is owed money; negative balance means they owe money

### 4. Data Schema

**Google Sheets Columns**:
| Column | Type | Purpose |
|--------|------|---------|
| Date | String (DD/MM/YYYY) | When expense occurred |
| Description | String | What was purchased |
| Value | Float | Amount in GBP |
| Paid by | Enum (Ellen/Alex) | Who made the payment |
| Paid for | Enum (Both/Ellen/Alex) | Who benefits from expense |

**Design Choices**:
- Date stored as string for Google Sheets compatibility; converted to datetime in Python
- "Paid for" = "Both" splits cost equally (50/50)
- No category field initially (kept simple for MVP)

## Key Features Implementation

### Balance Overview (`pages/balance.py`)

**Purpose**: Immediately show who owes whom.

**Design**:
- No caching to ensure accuracy
- Friendly phrasing ("Ellen owes Alex" vs raw numbers)

### Transaction History (`pages/transactions.py`)

**Purpose**: Browse and filter past expenses.

**Design**:
- Collapsible filter popover keeps UI clean
- Multi-select filters for "Paid by" and "Paid for"
- Full dataframe display (Streamlit's native table)
- Date normalisation handles inconsistent formats
- Filters default to showing you everything

### Add Expense Form (`pages/add_expense.py`)

**Purpose**: Quick expense entry.

**Design**:
- Auto-fills today's date
- Immediate feedback on success
- Appends to existing sheet (no overwrites)

**Current Limitations**:
- No data validation (TODO comment exists)
- No error handling for invalid amounts
- No duplicate detection

## Security Considerations

### Secrets Management

- All credentials in `.streamlit/secrets.toml`
- File excluded via `.gitignore`
- Service account with minimal permissions (only access to specific sheet)


### Data Privacy

- Google Sheets shared only with service account, Alex and Ellen
- No public access to spreadsheet
- Streamlit app runs locally (not deployed)

## Conclusion

This expense tracker demonstrates a pragmatic approach to solving a personal finance problem. By leveraging Streamlit's simplicity and Google Sheets' accessibility, the application achieves its core goal (tracking shared expenses) without unnecessary complexity. The modular design allows for future enhancements while maintaining clarity and ease of maintenance.

The application is ideal for:
- Two-person households tracking shared expenses
- Personal use cases with low transaction volume
- Users comfortable with Python but not wanting database overhead
- Rapid prototyping of expense tracking concepts

Trade-offs were consciously made to prioritize development speed and simplicity over enterprise-grade features, which aligns perfectly with the application's intended use case.
