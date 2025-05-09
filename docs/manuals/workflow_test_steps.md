# Workflow Test Steps & Example cURL Commands

This document provides step-by-step instructions and cURL examples to manually test all main workflows and API endpoints in the SENA_TEST project.

---

## 1. Authentication

### Login
```sh
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
```
- Save the returned `access_token` for use in the `Authorization` header:  
  `-H "Authorization: Bearer <access_token>"`

---

## 2. User Management

### Create User (admin only)
```sh
curl -X POST http://localhost:8000/users \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "pass", "email": "user1@example.com"}'
```

### List Users (admin only)
```sh
curl -X GET http://localhost:8000/users \
  -H "Authorization: Bearer <token>"
```

### Update User (admin only)
```sh
curl -X PUT http://localhost:8000/users/1 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "email": "newmail@example.com"}'
```

### Delete User (admin only)
```sh
curl -X DELETE http://localhost:8000/users/1 \
  -H "Authorization: Bearer <token>"
```

---

## 3. Product Management

### Create Product (admin only)
```sh
curl -X POST http://localhost:8000/products \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "Tomato", "price": 1000, "stock": 50}'
```

### List Products
```sh
curl -X GET http://localhost:8000/products \
  -H "Authorization: Bearer <token>"
```

### Update Product (admin only)
```sh
curl -X PUT http://localhost:8000/products/1 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "Tomato", "price": 1200, "stock": 40}'
```

### Delete Product (admin only)
```sh
curl -X DELETE http://localhost:8000/products/1 \
  -H "Authorization: Bearer <token>"
```

---

## 4. Inventory & Multi-Warehouse

### List Inventory
```sh
curl -X GET http://localhost:8000/inventory \
  -H "Authorization: Bearer <token>"
```

### Create Inventory Item (admin only)
```sh
curl -X POST http://localhost:8000/inventory \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "warehouse": "Main", "quantity": 100}'
```

### Transfer Inventory Between Warehouses (admin only)
```sh
curl -X POST http://localhost:8000/warehouses/transfer \
  -H "Authorization: Bearer <token>" \
  -d "warehouse_from=Main&warehouse_to=Sub1&product_id=1&quantity=10"
```

### List Warehouses
```sh
curl -X GET http://localhost:8000/warehouses \
  -H "Authorization: Bearer <token>"
```

### Get Inventory Alerts
```sh
curl -X GET http://localhost:8000/inventory/alerts \
  -H "Authorization: Bearer <token>"
```

---

## 5. Sales Management

### Register Sale
```sh
curl -X POST http://localhost:8000/sales \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "quantity": 5, "price": 1200, "customer": "John Doe"}'
```

### List Sales
```sh
curl -X GET http://localhost:8000/sales \
  -H "Authorization: Bearer <token>"
```

### Update Sale (admin only)
```sh
curl -X PUT http://localhost:8000/sales/1 \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "quantity": 6, "price": 1200, "customer": "John Doe"}'
```

### Delete Sale (admin only)
```sh
curl -X DELETE http://localhost:8000/sales/1 \
  -H "Authorization: Bearer <token>"
```

---

## 6. Invoice Management

### Create Invoice (admin only)
```sh
curl -X POST http://localhost:8000/invoices \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"sale_id": 1, "customer": "John Doe", "total": 6000}'
```

### List Invoices
```sh
curl -X GET http://localhost:8000/invoices \
  -H "Authorization: Bearer <token>"
```

---

## 7. Notifications

### List Notifications
```sh
curl -X GET http://localhost:8000/notifications \
  -H "Authorization: Bearer <token>"
```

### Create Notification (admin only)
```sh
curl -X POST http://localhost:8000/notifications \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"message": "Stock low for product X", "type": "alert"}'
```

---

## 8. Reports & Analytics

### Get Reports
```sh
curl -X GET "http://localhost:8000/reports?period=2025-05" \
  -H "Authorization: Bearer <token>"
```

### Export Reports (Excel/PDF)
```sh
curl -X GET "http://localhost:8000/reports/export?format=excel" \
  -H "Authorization: Bearer <token>"
```

### Get Analytics
```sh
curl -X GET "http://localhost:8000/analytics?group_by=product" \
  -H "Authorization: Bearer <token>"
```

### Export Analytics (Excel/PDF)
```sh
curl -X GET "http://localhost:8000/analytics/export?format=pdf" \
  -H "Authorization: Bearer <token>"
```

---

## 9. Transaction History

### List Transaction History
```sh
curl -X GET http://localhost:8000/transactions \
  -H "Authorization: Bearer <token>"
```

---

## 10. Offline Sync

### Download Data for Offline Use
```sh
curl -X GET http://localhost:8000/sync/download \
  -H "Authorization: Bearer <token>"
```

### Upload Data for Sync
```sh
curl -X POST http://localhost:8000/sync/upload \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"products": [...], "sales": [...], "inventory": [...]}'
```

---

**Note:**  
- Replace `<token>` with your actual JWT access token.
- Adjust IDs and payloads as needed for your test data.
- For endpoints requiring admin privileges, use an admin token.

---