# 🧠 Finance Q&A Chatbot 💰  
A rule-based Python chatbot that answers financial questions such as **revenue, net income, assets, liabilities, cash flow, and year-over-year (YoY) growth** for multiple companies and years.

---

## 📌 Project Overview  : 

This project demonstrates how **data preprocessing + rule-based NLP** can be combined to build an intelligent financial question-answering system without using machine learning or large language models.

This project is a rule-based Finance Q&A Chatbot that answers company-specific financial questions such as revenue, net income, assets, liabilities, cash flow, and year-over-year growth.

The workflow includes a data preprocessing stage where the raw financial dataset (FinanceData.xlsx) is cleaned and enriched inside a Jupyter notebook, and then exported as a structured CSV file. 

The chatbot (bot.py) reads this processed dataset and responds to user queries based on keyword matching, allowing users to ask questions like "Tesla revenue 2021" or "Amazon net income growth 2020". 

This project demonstrates how data engineering and simple NLP logic can be combined to build an interactive, data-driven chatbot without using machine learning or large language models.

## 📈 Dataset Columns  : 

Column              	Description

Company	              Company name
Year	                Financial year
Total_Revenue       	Annual revenue
Net_Income	          Annual profit
Total_Assets	        Total assets
Total_Liabilities   	Total liabilities
Cash_Flow_Operations	Cash flow from operations
Total_Revenue_YoY_%	  Revenue growth %
Net_Income_YoY_%	    Profit growth %

## 🚀  Further Enhancements  : 


✅ Add Streamlit / Flask UI

✅ Add fuzzy matching (NLP improvements)

✅ Add database backend (PostgreSQL / MongoDB)

✅ Add financial charts & dashboards (Matplotlib / Power BI)

✅ Convert to voice chatbot using speech recognition

✅ Replace rule-based logic with AI (LLM)

## 👤 Author : 


📌 Umasankar Gudivada 

📧 umashankargudivada@gmail.com

🔗 LinkedIn : :   https://www.linkedin.com/in/umasankar-g-27791b280/
