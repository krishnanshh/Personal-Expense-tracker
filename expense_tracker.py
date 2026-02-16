import os
import sqlite3
from datetime import date, datetime, timedelta
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

DB_PATH = "expenses.db"
CSV_PATH = "expenses.csv"

# Main categories
CATEGORIES = [
    "Travel",
    "Food-Order",
    "Outing",
    "Shopping",
    "Entertainment",
    "Food-Supplies",
    "Rent",
    "Bills",
    "Utilities",
    "Other"
]

# Subcategory mapping
SUBCATEGORIES = {
    "Travel": ["Uber", "Rapido", "Metro", "Auto", "Other"],
    "Food-Supplies": ["Blinkit", "Instamart", "Offline Market", "Other"],
    "Food-Order": ["Zomato", "Swiggy", "Other"],
    "Outing": ["Movies", "Cafe", "Drinks", "Other"],
    "Shopping": ["Clothes", "Amazon", "Flipkart", "Other"],
    "Entertainment": ["Netflix", "Spotify", "Games", "Other"],
    "Rent": ["House Rent"],
    "Bills": ["Electricity", "Water", "Internet", "Other"],
    "Utilities": ["Gas", "Maintenance", "Other"],
    "Other": ["Misc"]
}

PAY_MODES = ["UPI", "Cash", "Card", "Wallet"]

# Category emoji mapping for better mobile UX
CATEGORY_EMOJI = {
    "Travel": "🚗",
    "Food-Order": "🍕",
    "Outing": "🎉",
    "Shopping": "🛍️",
    "Entertainment": "🎬",
    "Food-Supplies": "🛒",
    "Rent": "🏠",
    "Bills": "💡",
    "Utilities": "🔧",
    "Other": "📝"
}

def init_db():
    """Initialize database with expenses table"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_date TEXT NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT NOT NULL,
                payment_mode TEXT NOT NULL,
                amount REAL NOT NULL,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def insert_row(d, cat, subcat, pay, amt, notes):
    """Insert a new expense record"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """INSERT INTO expenses 
               (expense_date, category, subcategory, payment_mode, amount, notes) 
               VALUES (?, ?, ?, ?, ?, ?)""",
            (d.isoformat(), cat, subcat, pay, float(amt), notes)
        )

def load_df():
    """Load all expenses as DataFrame"""
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(
            """SELECT id, expense_date, category, subcategory, 
                      payment_mode, amount, notes 
               FROM expenses 
               ORDER BY expense_date DESC, id DESC""",
            conn
        )
    if not df.empty:
        df['expense_date'] = pd.to_datetime(df['expense_date'])
    return df

def delete_expense(expense_id):
    """Delete an expense by ID"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

def export_csv(df):
    """Export DataFrame to CSV"""
    df.to_csv(CSV_PATH, index=False)

def get_summary_stats(df):
    """Calculate summary statistics"""
    if df.empty:
        return {
            'total': 0,
            'today': 0,
            'week': 0,
            'month': 0,
            'avg_daily': 0
        }
    
    today = pd.Timestamp.now().normalize()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    
    return {
        'total': df['amount'].sum(),
        'today': df[df['expense_date'] >= today]['amount'].sum(),
        'week': df[df['expense_date'] >= week_ago]['amount'].sum(),
        'month': df[df['expense_date'] >= month_ago]['amount'].sum(),
        'avg_daily': df[df['expense_date'] >= month_ago]['amount'].sum() / 30
    }

# ---------------- UI ----------------
st.set_page_config(
    page_title="Expense Tracker",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for mobile optimization
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 1.1em;
        font-weight: 600;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.2em;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1em;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        margin: 0.2em 0;
    }
    .metric-label {
        font-size: 0.9em;
        opacity: 0.9;
    }
    /* Make dataframe more mobile friendly */
    .stDataFrame {
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

st.title("💸 Expense Tracker")

init_db()

# Tabs for better organization on mobile
tab1, tab2, tab3 = st.tabs(["➕ Add", "📊 Stats", "📋 History"])

with tab1:
    st.subheader("Add New Expense")
    
    with st.form("entry_form", clear_on_submit=True):
        d = st.date_input("📅 Date", value=date.today())
        
        cat = st.selectbox(
            "🏷️ Category",
            CATEGORIES,
            format_func=lambda x: f"{CATEGORY_EMOJI.get(x, '')} {x}"
        )
        
        subcat = st.selectbox(
            "📑 Subcategory",
            SUBCATEGORIES.get(cat, ["Other"])
        )
        
        col1, col2 = st.columns(2)
        with col1:
            pay = st.selectbox("💳 Payment", PAY_MODES)
        with col2:
            amt = st.number_input(
                "💰 Amount (₹)",
                min_value=0.0,
                step=50.0,
                format="%.2f"
            )
        
        notes = st.text_input("📝 Notes (optional)")
        
        submitted = st.form_submit_button("💾 Save Expense", use_container_width=True)
    
    if submitted:
        if amt <= 0:
            st.error("⚠️ Amount must be greater than 0.")
        else:
            insert_row(d, cat, subcat, pay, amt, notes)
            st.success("✅ Expense saved!")
            st.balloons()

with tab2:
    st.subheader("Summary Statistics")
    
    df = load_df()
    stats = get_summary_stats(df)
    
    # Display metrics in cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Today's Spending</div>
            <div class="metric-value">₹{stats['today']:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <div class="metric-label">This Week</div>
            <div class="metric-value">₹{stats['week']:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <div class="metric-label">This Month</div>
            <div class="metric-value">₹{stats['month']:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <div class="metric-label">Avg Daily (30d)</div>
            <div class="metric-value">₹{stats['avg_daily']:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    if not df.empty:
        st.subheader("Spending by Category")
        
        # Category breakdown
        category_sum = df.groupby('category')['amount'].sum().reset_index()
        category_sum = category_sum.sort_values('amount', ascending=False)
        
        fig = px.pie(
            category_sum,
            values='amount',
            names='category',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            showlegend=False,
            height=400,
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Daily spending trend
        st.subheader("Daily Spending Trend")
        daily_sum = df.groupby('expense_date')['amount'].sum().reset_index()
        daily_sum = daily_sum.sort_values('expense_date')
        
        fig2 = px.line(
            daily_sum,
            x='expense_date',
            y='amount',
            markers=True
        )
        fig2.update_layout(
            xaxis_title="Date",
            yaxis_title="Amount (₹)",
            height=300,
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Expense History")
    
    df = load_df()
    
    if not df.empty:
        # Filters
        col1, col2 = st.columns(2)
        with col1:
            filter_cat = st.multiselect(
                "Filter by Category",
                options=CATEGORIES,
                default=[]
            )
        with col2:
            date_range = st.date_input(
                "Date Range",
                value=(df['expense_date'].min().date(), df['expense_date'].max().date()),
                max_value=date.today()
            )
        
        # Apply filters
        filtered_df = df.copy()
        if filter_cat:
            filtered_df = filtered_df[filtered_df['category'].isin(filter_cat)]
        if len(date_range) == 2:
            filtered_df = filtered_df[
                (filtered_df['expense_date'].dt.date >= date_range[0]) &
                (filtered_df['expense_date'].dt.date <= date_range[1])
            ]
        
        st.markdown(f"**Total:** ₹{filtered_df['amount'].sum():,.2f} | **Count:** {len(filtered_df)}")
        
        # Display with emoji
        display_df = filtered_df.copy()
        display_df['Category'] = display_df['category'].apply(
            lambda x: f"{CATEGORY_EMOJI.get(x, '')} {x}"
        )
        display_df['Date'] = display_df['expense_date'].dt.strftime('%Y-%m-%d')
        display_df['Amount'] = display_df['amount'].apply(lambda x: f"₹{x:,.2f}")
        
        show_cols = ['Date', 'Category', 'subcategory', 'payment_mode', 'Amount', 'notes']
        st.dataframe(
            display_df[show_cols],
            hide_index=True,
            use_container_width=True
        )
        
        # Export button
        if st.button("📥 Export to CSV", use_container_width=True):
            export_csv(filtered_df)
            st.success(f"✅ Exported to {CSV_PATH}")
        
        # Delete functionality
        st.subheader("Delete Expense")
        expense_to_delete = st.selectbox(
            "Select expense to delete",
            options=filtered_df['id'].tolist(),
            format_func=lambda x: f"ID {x}: {filtered_df[filtered_df['id']==x].iloc[0]['category']} - ₹{filtered_df[filtered_df['id']==x].iloc[0]['amount']:.2f}"
        )
        
        if st.button("🗑️ Delete Selected", use_container_width=True):
            delete_expense(expense_to_delete)
            st.success("✅ Expense deleted!")
            st.rerun()
    else:
        st.info("No expenses recorded yet. Add your first expense in the 'Add' tab!")

# Footer
st.divider()
st.caption(f"📂 Database: `{os.path.abspath(DB_PATH)}`")
