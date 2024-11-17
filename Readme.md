This project is a recommendation engine designed for a B2C platform, such as an e-commerce platform selling 
beauty products.  The engine provides personalized product recommendations based on user interactions 
and preferences, using a microservices architecture with caching for improved performance.

# Components:
Flask App: Handles API routing.
SQLAlchemy: Manages relational databases for user and product data.
Redis: Caches recommendations to improve performance.
Recommendation Logic: A placeholder that can later be replaced with an algorithm for collaborative filtering or content-based recommendation.

# Installation
1. git clone https://github.com/your-username/recommendation-engine.git
   cd recommendation-engine
2. Install dependencies: pip install -r requirements.txt
3. Initialize DB:
    flask db init
    flask db migrate
    flask db upgrade
4. python run.py


# Example Usage:
Adding Users and Products to the Database (For Testing)
Fetching Recommendations:
    GET http://localhost:5000/recommendations/<user_id>
