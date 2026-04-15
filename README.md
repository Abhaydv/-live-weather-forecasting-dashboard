# -live-weather-forecasting-dashboard
 🌦 Live Weather Forecasting & Analytics Dashboard

A full-stack weather analytics project that fetches real-time weather data using a Flask API and visualizes it through an interactive dashboard and Power BI.

---

## 🚀 Features

* 🌍 Real-time weather data (city-based search)
* 📊 Interactive analytics dashboard (charts + KPIs)
* 📈 Power BI integration for advanced visualization
* 🌐 Live deployment (Frontend + Backend)
* 🔄 Dynamic API-based data fetching

---

## 🛠 Tech Stack

* **Frontend:** HTML, CSS, JavaScript, Chart.js
* **Backend:** Python (Flask), REST API
* **Data Source:** Weather API
* **Visualization:** Microsoft Power BI
* **Deployment:** Render (Backend), Netlify (Frontend)

---

## 🌐 Live Demo
* 🔗 **Frontend:** https://splendid-khapse-2f1978.netlify.app
* 🔗 **Backend API:** https://live-weather-forecasting-dashboard.onrender.com

---

## 📊 Dashboard Preview

![Dashboard](screenshots/"Picture162430.png")

---

## 📈 Power BI Dashboard Insights

The Power BI dashboard includes:

* 🌡 Average, Maximum & Minimum Temperature KPIs
* 💧 Humidity Analysis
* 📈 Temperature Trend over time
* 🌤 Weather Condition Distribution
* 🎛 Interactive filters for better insights

---

## ⚙️ How It Works

1. User enters a city name on the frontend
2. Frontend calls the Flask API
3. Backend fetches data from Weather API
4. Data is processed and returned as JSON
5. Dashboard visualizes the data using charts and Power BI

---

## 🧪 API Endpoint

```bash
GET /api/weather?city=CityName
```

### Example:

```bash
https://live-weather-forecasting-dashboard.onrender.com/api/weather?city=Delhi
```

---

## 📁 Project Structure

```
weather-forecasting-dashboard/
│
├── app.py
├── weatherApi.py
├── requirements.txt
├── Procfile
├── index.html
├── screenshots/
│   └── dashboard.png
└── README.md
```

---

## ⚠️ Notes

* Power BI dashboard is not publicly embedded due to authentication restrictions
* Use screenshots or live demo for visualization reference

---

## 💼 Use Case

This project demonstrates:

* Full-stack development
* API integration
* Data analytics & visualization
* Real-world deployment

---

## 👨‍💻 Author

**Abhay Yadav**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
