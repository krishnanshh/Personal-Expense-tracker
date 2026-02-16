# Configuration File for Expense Tracker
# Edit this file to customize your expense tracker

# ============================================
# CURRENCY SETTINGS
# ============================================
CURRENCY_SYMBOL = "₹"  # Change to $, €, £, etc.
CURRENCY_NAME = "INR"   # USD, EUR, GBP, etc.

# ============================================
# CATEGORIES & SUBCATEGORIES
# ============================================
# You can add, remove, or modify categories here
# Format: "Category Name": ["Subcategory 1", "Subcategory 2", ...]

CUSTOM_CATEGORIES = {
    "Travel": ["Uber", "Rapido", "Metro", "Auto", "Bus", "Train", "Flight", "Other"],
    "Food-Order": ["Zomato", "Swiggy", "Uber Eats", "Other"],
    "Outing": ["Movies", "Cafe", "Drinks", "Restaurant", "Other"],
    "Shopping": ["Clothes", "Amazon", "Flipkart", "Myntra", "Grocery", "Other"],
    "Entertainment": ["Netflix", "Spotify", "Prime Video", "Games", "Books", "Other"],
    "Food-Supplies": ["Blinkit", "Instamart", "Big Basket", "Offline Market", "Other"],
    "Rent": ["House Rent", "Parking", "Storage"],
    "Bills": ["Electricity", "Water", "Internet", "Phone", "Other"],
    "Utilities": ["Gas", "Maintenance", "Repairs", "Other"],
    "Health": ["Doctor", "Medicines", "Gym", "Supplements", "Other"],
    "Education": ["Courses", "Books", "Subscriptions", "Other"],
    "Personal Care": ["Salon", "Grooming", "Spa", "Other"],
    "Gifts": ["Birthday", "Anniversary", "Festival", "Other"],
    "Investment": ["SIP", "Stocks", "Crypto", "Other"],
    "Other": ["Misc"]
}

# ============================================
# PAYMENT MODES
# ============================================
CUSTOM_PAYMENT_MODES = [
    "UPI",
    "Cash",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet (Paytm/PhonePe)",
    "Other"
]

# ============================================
# BUDGET LIMITS (Optional - for future use)
# ============================================
MONTHLY_BUDGET = {
    "Travel": 5000,
    "Food-Order": 3000,
    "Outing": 2000,
    "Shopping": 5000,
    "Entertainment": 1000,
    "Food-Supplies": 8000,
    # Add more as needed
}

# ============================================
# DISPLAY SETTINGS
# ============================================
# Number of recent entries to show by default
DEFAULT_RECENT_ENTRIES = 50

# Date format for display
DATE_FORMAT = "%Y-%m-%d"  # Change to "%d-%m-%Y" for DD-MM-YYYY

# Default sorting (options: "date", "amount", "category")
DEFAULT_SORT = "date"
DEFAULT_SORT_ORDER = "DESC"  # or "ASC"

# ============================================
# COLOR SCHEME
# ============================================
# CSS gradient colors for metric cards
METRIC_COLORS = {
    "primary": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "secondary": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
    "tertiary": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
    "quaternary": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"
}

# ============================================
# CATEGORY EMOJIS
# ============================================
CATEGORY_EMOJIS = {
    "Travel": "🚗",
    "Food-Order": "🍕",
    "Outing": "🎉",
    "Shopping": "🛍️",
    "Entertainment": "🎬",
    "Food-Supplies": "🛒",
    "Rent": "🏠",
    "Bills": "💡",
    "Utilities": "🔧",
    "Health": "⚕️",
    "Education": "📚",
    "Personal Care": "💅",
    "Gifts": "🎁",
    "Investment": "📈",
    "Other": "📝"
}

# ============================================
# DATABASE SETTINGS
# ============================================
DB_PATH = "expenses.db"
CSV_EXPORT_PATH = "expenses_export.csv"

# Auto-backup database (creates backup every N days)
AUTO_BACKUP_ENABLED = True
AUTO_BACKUP_DAYS = 7  # Backup every 7 days
BACKUP_FOLDER = "backups"

# ============================================
# NOTIFICATION SETTINGS (Future feature)
# ============================================
# Daily spending limit alert
DAILY_LIMIT_ALERT = 1000
WEEKLY_LIMIT_ALERT = 5000
MONTHLY_LIMIT_ALERT = 20000

# ============================================
# ADVANCED SETTINGS
# ============================================
# Show developer mode features
DEVELOPER_MODE = False

# Enable debug logging
DEBUG_MODE = False

# Default timezone
TIMEZONE = "Asia/Kolkata"  # Change to your timezone

# ============================================
# NOTES
# ============================================
# To use this config file in your app, import it:
# from config import *
# 
# Then replace hardcoded values with these variables
# Example: Replace CATEGORIES with CUSTOM_CATEGORIES
