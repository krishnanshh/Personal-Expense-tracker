# 💸 Personal Expense Tracker

A mobile-friendly expense tracking app built with Streamlit that you can access from your iPhone. Track your daily expenses, view spending patterns, and analyze your financial habits - all from your phone!

## ✨ Features

### Core Functionality
- ➕ **Quick Expense Entry**: Add expenses with category, subcategory, payment mode, and notes
- 📊 **Visual Analytics**: View spending trends with interactive charts
- 💰 **Real-time Statistics**: Today, week, month totals and daily averages
- 📱 **Mobile Optimized**: Large buttons, responsive layout, emoji indicators
- 🗑️ **Expense Management**: Filter, search, and delete entries
- 📥 **Export Data**: Download your expense history as CSV

### Categories Included
- 🚗 Travel (Uber, Rapido, Metro, Auto)
- 🍕 Food Orders (Zomato, Swiggy)
- 🛒 Food Supplies (Blinkit, Instamart, Markets)
- 🎉 Outing (Movies, Cafe, Drinks)
- 🛍️ Shopping (Clothes, Amazon, Flipkart)
- 🎬 Entertainment (Netflix, Spotify, Games)
- 🏠 Rent
- 💡 Bills (Electricity, Water, Internet)
- 🔧 Utilities (Gas, Maintenance)
- 📝 Other

### Payment Modes
- UPI
- Cash
- Card
- Wallet

## 📱 Mobile Access

This app is designed to be accessed from your iPhone. See detailed setup instructions in:
- **Quick start**: `QUICKSTART.md`
- **Detailed guide**: `MOBILE_SETUP.md`

### Three Ways to Use:
1. **Local Network** - Access on same WiFi (easiest)
2. **Cloud Deployment** - Access from anywhere (Streamlit Cloud)
3. **Tailscale** - Secure remote access to your computer

## 🚀 Installation

### Requirements
- Python 3.8 or higher
- iPhone with Safari or Chrome

### Setup Steps

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   # Mac/Linux
   ./start_tracker.sh
   
   # Windows
   start_tracker.bat
   
   # Or manually
   streamlit run expense_tracker.py --server.address 0.0.0.0
   ```

4. **Access from iPhone:**
   - Look for the URL in the terminal output
   - Open Safari and go to `http://YOUR_IP:8501`
   - Add to Home Screen for app-like experience

## 📸 Screenshots

### Add Expense Tab
- Clean, mobile-friendly form
- Date picker
- Category selection with emojis
- Amount input with currency symbol

### Statistics Tab
- Colorful metric cards showing spending
- Pie chart for category breakdown
- Line chart for daily trends

### History Tab
- Filterable expense list
- Date range selector
- Category filters
- Delete functionality
- CSV export

## 📊 Data Storage

- **Database**: SQLite (`expenses.db`)
- **Location**: Same directory as the app
- **Backup**: Export to CSV regularly
- **Privacy**: All data stored locally (unless using cloud deployment)

## 🛠️ Technical Details

### Built With
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **Plotly** - Interactive charts
- **SQLite** - Database

### Database Schema
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_date TEXT NOT NULL,
    category TEXT NOT NULL,
    subcategory TEXT NOT NULL,
    payment_mode TEXT NOT NULL,
    amount REAL NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## 🔒 Security & Privacy

### Local Deployment
- Data never leaves your computer
- Accessible only on your local network
- No cloud storage involved

### Cloud Deployment (Optional)
- Use private GitHub repository
- Database stored on Streamlit Cloud servers
- Secured with HTTPS
- Password protect your Streamlit Cloud account

## 🎯 Usage Tips

### For Best Experience:
1. **Add to iPhone Home Screen**
   - Makes it feel like a native app
   - Quick access without browser UI

2. **Regular Backups**
   - Export to CSV weekly
   - Copy `expenses.db` file

3. **Set Spending Goals**
   - Use daily average to track progress
   - Monitor category breakdowns

4. **Quick Entry**
   - Keep notes brief
   - Use consistent subcategories
   - Enter expenses daily

### iPhone Tips:
- Use Safari AutoFill for faster entry
- Create a Shortcut to open the app
- Enable "Request Desktop Website" if needed
- Bookmark the URL for quick access

## 📈 Future Enhancements

Potential features to add:
- [ ] Budget limits per category
- [ ] Recurring expense tracking
- [ ] Multiple user support
- [ ] Receipt photo uploads
- [ ] Monthly reports
- [ ] Goal setting
- [ ] Expense predictions
- [ ] Category customization
- [ ] Multi-currency support
- [ ] Dark mode

## 🐛 Troubleshooting

### Can't Connect from iPhone?
1. Check both devices are on same WiFi
2. Verify the app is running on computer
3. Check firewall settings (allow port 8501)
4. Use `http://` not `https://`
5. Try your computer's IP address

### Database Issues?
1. Check file permissions
2. Ensure SQLite is working: `python -c "import sqlite3"`
3. Delete `expenses.db` to start fresh (backup first!)

### App Not Loading?
1. Clear browser cache
2. Restart the Streamlit app
3. Check Python version (3.8+)
4. Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## 📝 Customization

### Add New Categories:
Edit the `CATEGORIES` and `SUBCATEGORIES` lists in `expense_tracker.py`

### Change Currency:
Replace `₹` with your currency symbol throughout the code

### Adjust Date Range:
Modify the statistics calculations in the `get_summary_stats()` function

### Custom Colors:
Update the CSS in the `st.markdown()` section for different color schemes

## 📄 License

This project is open source and available for personal use. Feel free to modify and adapt it to your needs!

## 🤝 Contributing

Found a bug or have a feature suggestion? Feel free to:
1. Report issues
2. Suggest improvements
3. Submit pull requests

## 📧 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the mobile setup guide
3. Ensure all dependencies are installed

---

**Made with ❤️ for personal finance tracking**

Start tracking your expenses today! 💸📱
