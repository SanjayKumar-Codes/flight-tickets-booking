
# ✈️ Flight Demand Trends — Real-Time Airline Market Insights

A lightweight Python web app to track real-time **flight demand trends worldwide**. This project fetches live airline data, processes actionable insights, and visualizes trends with interactive charts and tables — all built using open tools and free APIs.



## 🔧 Features

✅ Real-time flight data via **OpenSky Network API**
✅ Total flights tracked with **country-wise breakdown**
✅ Filter flights by **origin country** with live results
✅ Detect **high-demand airspace regions** using simple grid clustering
✅ Interactive **bar chart** for top 5 countries by flight count
✅ Responsive, interactive **UI with attractive design**
✅ Clean footer with **contact details**



## 🖥️ Tech Stack

* **Python 3.11+**
* **FastAPI** 🚀
* **Pandas** 📊
* **Google Charts**
* **HTML, CSS** — Fully Responsive UI

 

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SanjayKumar-Codes/flight-tickets-booking.git  
cd flight-tickets-booking  
```

### 2. Create and Activate Virtual Environment

**For Windows:**

```bash
python -m venv fitick  
.\fitick\Scripts\activate  
```

**For macOS/Linux:**

```bash
python3 -m venv fitick  
source fitick/bin/activate  
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt  
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload  
```

Visit the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

 

## 📁 Project Structure

```
flight-tickets-booking/  
│  
├── app/  
│   ├── __init__.py  
│   ├── main.py               # FastAPI entry point  
│   ├── processor.py          # Data processing logic  
│   ├── scraper.py            # Data fetching from OpenSky API  
│   ├── static/               # Static files  
│   │   ├── flight1.jpeg  
│   │   ├── flight2.jpeg  
│   │   ├── flight3.jpeg  
│   │   └── style.css  
│   └── templates/  
│       └── index.html         # Main HTML template  
│  
├── fitick/                    # Virtual environment (excluded from Git)  
├── README.md                   # Project documentation  
├── requirements.txt            # Python dependencies  
```

 

## 🛫 About

This project was developed to help **hostel businesses in Australia** monitor airline market demand trends. Built entirely with open-source tools and free APIs, it provides a fast, lightweight, and intuitive solution for tracking global demand patterns.

 

## 📊 Sample Insights

* Total number of flights tracked
* Current flights in air vs on ground
* Top 5 countries by flight count
* Filter flights by origin country
* High-demand airspace regions table
* Interactive bar chart for visual trends

 

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to explore the [Issues Page](https://github.com/SanjayKumar-Codes/flight-tickets-booking/issues).

 

## 📝 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

 

## 👨‍💻 Developer Contact

* [LinkedIn - Sanjay Kumar](https://www.linkedin.com/in/sanjay-kumarai)

**Project Link:** [https://github.com/SanjayKumar-Codes/flight-tickets-booking](https://github.com/SanjayKumar-Codes/flight-tickets-booking)
