This is a full delivery app backend system 
## 🔐 Authentication & Roles

This API uses **JWT (JSON Web Tokens)** for authentication.

Every protected endpoint requires a valid Bearer token in the `Authorization` header.

### Roles

| Role    | Description                                      |
|---------|--------------------------------------------------|
| `admin` | Full access — manage users, drivers, orders      |
| `shop`  | Place and track their orders                     |
| `driver`| Accept assigned deliveries and update status     |
