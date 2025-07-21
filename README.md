# ShipBlu Orders API

A simple Django REST API for managing customer orders and tracking their status.

> This project was created as part of a backend technical task.

---

## 🚀 Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/SubestaRomany/ShipBlu-Orders-API.git
cd ShipBlu-Orders-API

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Apply database migrations
python manage.py migrate

5. Run the development server
python manage.py runserver


📬 API Endpoints
Base URL: http://localhost:8000/api/orders/

➕ Create a new order
curl -X POST http://localhost:8000/api/orders/ \
-H "Content-Type: application/json" \
-d '{
  "tracking_number": "ORD123456",
  "status": "CREATED",
  "customer": {
    "name": "John Doe",
    "phone_number": "+201234567890"
  }
}'

📄 List all orders (with optional filters)
curl http://localhost:8000/api/orders/?status=CREATED
curl http://localhost:8000/api/orders/?customer_name=John

🔄 Update order status
curl -X PATCH http://localhost:8000/api/orders/1/ \
-H "Content-Type: application/json" \
-d '{"status": "PICKED"}'

🔍 Retrieve order details
curl http://localhost:8000/api/orders/1/

❌ Delete an order
curl -X DELETE http://localhost:8000/api/orders/1/


✨ Bonus Features Implemented
✅ Tracks status changes using the OrderTrackingEvent model

✅ Pagination enabled for listing orders (10 per page)

✅ Only valid status transitions allowed: CREATED → PICKED → DELIVERED

✅ Built using Django REST Framework’s class-based views (ModelViewSet)


📝 Assumptions
tracking_number is unique per order.

Only the following status transitions are valid:

CREATED → PICKED

PICKED → DELIVERED

Each status change is logged in OrderTrackingEvent.

A customer is auto-created if they don’t already exist during order creation.


🛠️ Tech Stack
Python 3

Django 5

Django REST Framework

SQLite (for local development)


✅ Features Covered
Create, list, retrieve, update, and delete orders

Unique tracking number validation

Filter orders by customer name and status

Track order status history

Enforce valid status transitions

Pagination

Follows DRF best practices using class-based views (ModelViewSet)
