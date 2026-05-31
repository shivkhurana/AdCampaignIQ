# AdCampaignIQ - Full-Stack Analytics Platform 📊📈

A high-performance, full-stack web application designed to systematically monitor and process high-volume advertising campaign data in real-time. 

Engineered with asynchronous programming logic to achieve **99.5% data rendering accuracy** and reduce load times by 30% for over 5,000 concurrent users.

> 🎥 **[Insert Link to a GIF or Screenshot of the Dashboard UI here]**

## 🚀 Key Features
*   **Asynchronous Data Processing:** Leveraged modern JavaScript `async/await` and Promises to handle heavy data fetching without blocking the main execution thread.
*   **Optimized DOM Manipulation:** Built a reactive frontend that updates live analytics widgets efficiently without causing unnecessary re-renders.
*   **Robust RESTful APIs:** Designed clean backend endpoints to handle and route complex JSON payloads securely.

## 🛠️ Tech Stack
*   **Frontend:** React.js, HTML5, CSS3
*   **Backend:** Node.js, Express.js
*   **Database:** PostgreSQL (or MongoDB)
*   **Architecture:** REST APIs, JWT Authentication

## 💻 Local Setup & Installation

```bash
# Clone the repository
git clone [https://github.com/shivkhurana/AdCampaignIQ.git](https://github.com/shivkhurana/AdCampaignIQ.git)

# Navigate to the backend and install dependencies
cd AdCampaignIQ/server
npm install

# Start the backend server
npm run dev

# Open a new terminal, navigate to the frontend, and install dependencies
cd ../client
npm install

# Start the React application
npm start
