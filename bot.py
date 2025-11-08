import pandas as pd

# Load dataset
data = pd.read_csv("financial_data_with_yoy.csv")

def simple_chatbot(user_query):
    user_query = user_query.lower()

    # --- Revenue ---
    if "revenue" in user_query and "growth" not in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s revenue in {year} is {row.iloc[0]['Total_Revenue']:,}"

    # --- Net Income ---
    if "net income" in user_query and "growth" not in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s net income in {year} is {row.iloc[0]['Net_Income']:,}"

    # --- Assets ---
    if "assets" in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s assets in {year} are {row.iloc[0]['Total_Assets']:,}"

    # --- Liabilities ---
    if "liabilities" in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s liabilities in {year} are {row.iloc[0]['Total_Liabilities']:,}"

    # --- Cash Flow ---
    if "cash flow" in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s cash flow in {year} is {row.iloc[0]['Cash_Flow_Operations']:,}"

    # --- Revenue Growth ---
    if "revenue growth" in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s revenue growth in {year} is {row.iloc[0]['Total_Revenue_YoY_%']:.2f}%"

    # --- Net Income Growth ---
    if "net income growth" in user_query:
        for company in data['Company'].unique():
            if company.lower() in user_query:
                for year in data['Year'].unique():
                    if str(year) in user_query:
                        row = data[(data['Company'] == company) & (data['Year'] == year)]
                        if not row.empty:
                            return f"{company}'s net income growth in {year} is {row.iloc[0]['Net_Income_YoY_%']:.2f}%"

    return "Sorry, I can only answer financial questions like revenue, net income, assets, liabilities, cash flow, and growth."

# --- Run chatbot ---
print("Chatbot 🤖: Hello! Ask me about financials (type 'bye' to quit).")
while True:
    query = input("You: ")
    if query.lower() == "bye":
        print("Chatbot 🤖: Goodbye 👋")
        break
    print("Chatbot 🤖:", simple_chatbot(query))
