POST /api/reporters/ — Positive Cases

# 1. Create a valid reporter
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Alice", "email": "alice@example.com", "team": "Backend"}'

# 2. Create a second reporter
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d '{"id": 2, "name": "Bob", "email": "bob@company.io", "team": "Frontend"}'

---

POST /api/reporters/ — Negative Cases

# 3. Invalid JSON body
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d 'not valid json'

# 4. Missing required fields (no name, no email)
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "team": "QA"}'

# 5. Empty name (fails validation)
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "name": "", "email": "test@example.com", "team": "QA"}'

# 6. Invalid email — missing @ (fails validation)
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "name": "Charlie", "email": "invalid-email", "team": "QA"}'

# 7. Empty body
curl -X POST http://127.0.0.1:8000/api/reporters/ \
  -H "Content-Type: application/json" \
  -d ''

---


GET /api/reporters/ — Positive Cases

# 8. Get all reporters
curl http://127.0.0.1:8000/api/reporters/

# 9. Get reporter by ID
curl "http://127.0.0.1:8000/api/reporters/?id=1"


---


GET /api/reporters/ — Negative Cases

# 10. Get reporter with non-existent ID
curl "http://127.0.0.1:8000/api/reporters/?id=999"

---

POST /api/issues/ — Positive Cases

# 11. Create a regular issue (medium priority — uses base Issue class)
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Fix login bug", "description": "Login fails on Safari", "status": "open", "priority": "medium", "reporter_id": 1}'

# 12. Create a critical issue (uses CriticalIssue subclass)
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 2, "title": "Database down", "description": "Production DB unreachable", "status": "open", "priority": "critical", "reporter_id": 1}'

# 13. Create a low priority issue (uses LowPriorityIssue subclass)
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "title": "Update footer text", "description": "Typo in footer", "status": "open", "priority": "low", "reporter_id": 2}'

# 14. Create a high priority issue (uses base Issue class)
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 4, "title": "Memory leak", "description": "Memory grows over time", "status": "in_progress", "priority": "high", "reporter_id": 1}'

# 15. Create an issue with "resolved" status
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 5, "title": "Old CSS issue", "description": "Already fixed", "status": "resolved", "priority": "low", "reporter_id": 2}'

# 16. Create an issue with "closed" status
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 6, "title": "Won'\''t fix", "description": "Not a real bug", "status": "closed", "priority": "medium", "reporter_id": 1}'

---

POST /api/issues/ — Negative Cases

# 17. Invalid JSON body
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d 'bad json'

# 18. Missing required fields (no title, no status)
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 7, "description": "Something", "priority": "high", "reporter_id": 1}'

# 19. Empty title (fails validation)
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 7, "title": "", "description": "No title", "status": "open", "priority": "high", "reporter_id": 1}'

# 20. Invalid status value
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 7, "title": "Test", "description": "Bad status", "status": "pending", "priority": "high", "reporter_id": 1}'

# 21. Invalid priority value
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"id": 7, "title": "Test", "description": "Bad priority", "status": "open", "priority": "urgent", "reporter_id": 1}'

# 22. Empty body
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d ''

---

GET /api/issues/ — Positive Cases

# 23. Get all issues
curl http://127.0.0.1:8000/api/issues/

# 24. Get issue by ID
curl "http://127.0.0.1:8000/api/issues/?id=1"

# 25. Filter issues by status
curl "http://127.0.0.1:8000/api/issues/?status=open"

# 26. Filter by another status
curl "http://127.0.0.1:8000/api/issues/?status=in_progress"


---


GET /api/issues/ — Negative Cases

# 27. Get issue with non-existent ID
curl "http://127.0.0.1:8000/api/issues/?id=999"

# 28. Filter by status that has no matches (returns empty list, not an error)
curl "http://127.0.0.1:8000/api/issues/?status=cls"

